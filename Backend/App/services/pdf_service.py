import fitz  # PyMuPDF
import logging
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from ..config import API_KEY

logging.basicConfig(level=logging.INFO)

class PDFService:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=API_KEY, temperature=0.3)
        self.embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=API_KEY)
        self.vector_store_cache = {}

    async def extract_text_from_pdf(self, pdf_path: str) -> str:
        """Extract text from the PDF file."""
        text = ""
        try:
            with fitz.open(pdf_path) as doc:
                for page in doc:
                    text += page.get_text()
            logging.info("Text extracted from PDF successfully.")
            return text
        except Exception as e:
            logging.error(f"Error extracting text from PDF: {str(e)}")
            raise

    async def load_documents(self, text_content: str, document_id: int):
        """Load documents into the vector store."""
        logging.info(f"Loading documents for document ID: {document_id}")
        
        if not text_content:
            raise ValueError("Text content cannot be empty.")

        text_splitter = RecursiveCharacterTextSplitter(
            separators=["\n\n", "\n", " ", ""],
            chunk_size=500,
            chunk_overlap=50,
            length_function=len
        )
        chunks = text_splitter.split_text(text_content)
        
        if document_id not in self.vector_store_cache:
            documents = [Document(page_content=chunk) for chunk in chunks]



            vector_store = FAISS.from_documents(documents, self.embeddings)
            self.vector_store_cache[document_id] = vector_store
            print(self.vector_store_cache)
            logging.info("Document loaded into vector store successfully.")

    async def answer_question(self, document_id: int, question: str) -> str:
        """Answer a question based on the content of the loaded document."""

        if document_id not in self.vector_store_cache:
            raise ValueError("Document not loaded. Please upload and load the document first.")
        


        retriever = self.vector_store_cache[document_id].as_retriever(search_type="similarity", search_kwargs={"k": 3})
        qa_chain = RetrievalQA.from_chain_type(llm=self.llm, chain_type="stuff", retriever=retriever)
        
        result = qa_chain({"query": question})
        return result["result"]
