import os
from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from App.db import execute_query
from ..services.pdf_service import PDFService
import tracemalloc

tracemalloc.start()
router = APIRouter()

# Provide the path to your credentials JSON file, your Google Cloud project ID, and the model name
CREDENTIALS_PATH = r"C:\Users\eahta\Downloads\chatpdf-440713-3e2b62dd8f3a.json"
PROJECT_ID = "chatpdf-440713"
MODEL_NAME = "textembedding-gecko@001"  # Specify the model name here if needed

# Initialize the PDFService instance with credentials
pdf_service = PDFService(credentials_path=CREDENTIALS_PATH, project_id=PROJECT_ID, model_name=MODEL_NAME)


@router.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    print("Received file:", file.filename) 
    if not file.content_type == "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are accepted"
        )
    
    # Define the uploads directory
    uploads_dir = "./uploads"
    
    # Check if the uploads directory exists, if not, create it
    if not os.path.exists(uploads_dir):
        os.makedirs(uploads_dir)

    # Save PDF to local filesystem
    pdf_path = os.path.join(uploads_dir, file.filename)
    with open(pdf_path, "wb") as pdf_file:
        pdf_file.write(await file.read())  # Use await here to read the file content

    try:
        # Extract text content from the PDF file
        text_content = await pdf_service.extract_text_from_pdf(pdf_path)  # Pass the path to the PDF file
        print(text_content)

        # Insert into database
        insert_query = """
            INSERT INTO documents (filename, content) 
            VALUES ($1, $2)
            RETURNING id
        """
        result = await execute_query(
            insert_query, 
            (file.filename, text_content)
        )
        
        document_id = result[0]['id'] if result else None

        await pdf_service.load_documents(text_content, document_id)
        
        return {
            "message": "PDF uploaded and processed successfully",
            "document_id": document_id,
            "filename": file.filename
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing PDF: {str(e)}"
        )

@router.get("/documents/{document_id}")
async def get_document(document_id: int):
    query = "SELECT filename, content FROM documents WHERE id = $1"
    result = await execute_query(query, (document_id,))
    
    if not result:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )
        
    document = result[0]
    return {
        "document_id": document_id,
        "filename": document['filename'],
        "content": document['content']
    }


@router.get("/ask-question/{document_id}")
async def ask_question(document_id: int, question: str = Query(...)):
    try:
        answer = await pdf_service.answer_question(document_id, question)
        return {"question": question, "answer": answer}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error answering question: {str(e)}")
