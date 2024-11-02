from fastapi import APIRouter, UploadFile, File, HTTPException
from App.db import execute_query
from ..services.pdf_service import extract_text_from_pdf  # You'll need to implement this

router = APIRouter()

@router.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    print("Received file:", file.filename) 
    if not file.content_type == "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are accepted"
        )
    
    try:
        # Read the file content
        contents = await file.read()
        
        # Extract text content (you'll need to implement this in pdf_service.py)
        # text_content = extract_text_from_pdf(contents)
        text_content="testing text to store on db"
        
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

