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

#This class is mainly reponsible for handlling all backend operations. 

class PDFService:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=API_KEY, temperature=0.3) #Setting the model and api key
        self.embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=API_KEY)  #getting embeddings based on the model and apikey
        self.vector_store_cache = {}  #Dictonary to save the vector store and document id. 

    # Function to extract text from the uploaded pdf.
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
    # This function handles all the  backend operations. 
    # It takes the text, question and the document id as input and first creates chunks then vector store.
    async def load_documents(self, text_content: str, document_id: int):
        """Load documents into the vector store."""
        logging.info(f"Loading documents for document ID: {document_id}")
        
        if not text_content:
            raise ValueError("Text content cannot be empty.")
        
        #splitting the whole text into small chunks
        text_splitter = RecursiveCharacterTextSplitter(
            separators=["\n\n", "\n", " ", ""],
            chunk_size=500,
            chunk_overlap=50,
            length_function=len
        )
        chunks = text_splitter.split_text(text_content)
        

        #Creating the vector store only when the document  id is not in the cache.
        if document_id not in self.vector_store_cache:
            documents = [Document(page_content=chunk) for chunk in chunks]

            #passing the all chunks as the documents to Faiss vector db (It works locally)
            vector_store = FAISS.from_documents(documents, self.embeddings)
            self.vector_store_cache[document_id] = vector_store
            # print(self.vector_store_cache)  #This is used in debuggin.
            logging.info("Document loaded into vector store successfully.")

    async def answer_question(self, document_id: int, question: str) -> str:
        """Answer a question based on the content of the loaded document."""

        if document_id not in self.vector_store_cache:
            raise ValueError("Document not loaded. Please upload and load the document first.")
        

        #performing similarity search on the stored vector store and passing the ranked result to chain.
        retriever = self.vector_store_cache[document_id].as_retriever(search_type="similarity", search_kwargs={"k": 3})
        qa_chain = RetrievalQA.from_chain_type(llm=self.llm, chain_type="stuff", retriever=retriever)
        
        #Chain created and  now we can pass the question to it to get the answer.
        result = qa_chain({"query": question})
        return result["result"]
