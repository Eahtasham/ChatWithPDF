# ChatWithPDF Documentation
## Overview
ChatWithPDF is a FastAPI-based application that enables users to upload PDF documents and interact with their contents through a question-answering interface. The application uses Google's Gemini AI model for text processing and FAISS for efficient vector similarity search.
## Features
- PDF document upload and processing
- Text extraction and vectorization
- Question-answering capability using AI
- Document management with PostgreSQL
- RESTful API endpoints
- Async operations for better performance
## Technical Stack
### Backend Framework
- FastAPI (async web framework)
- Uvicorn (ASGI server)
### AI and Machine Learning
- LangChain (for AI operations)
- Google Gemini AI (LLM model)
- FAISS (vector similarity search)
### Database
- PostgreSQL (document storage)
- AsyncPG (async PostgreSQL client)
### PDF Processing
- PyMuPDF (PDF text extraction)
### Development Tools
- Python 3.8+ (core language)
- Poetry or pip (dependency management)
## Installation
### Prerequisites
1. Python 3.8 or higher
2. PostgreSQL database
3. Google Cloud API key with Gemini AI access
### Step-by-Step Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Eahtasham/ChatWithPDF.git
   cd ChatWithPDF
   cd Backend
   ```
2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   
   # On Windows
   .\venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Create Environment File**
   Create a `.env` file in the root directory:
   ```plaintext
   GEMINI_API_KEY=your_gemini_api_key_here
   DATABASE_URL=postgresql://user:password@localhost:5432/dbname
   ```
5. **Set Up Database**
   ```sql
   CREATE TABLE documents (
       id SERIAL PRIMARY KEY,
       filename VARCHAR(255),
       content TEXT
   );
   ```
### Dependencies List
```plaintext
fastapi>=0.68.0
uvicorn>=0.15.0
python-multipart>=0.0.5
asyncpg>=0.25.0
python-dotenv>=0.19.0
PyMuPDF>=1.19.0
langchain>=0.1.0
langchain-google-genai>=0.0.7
faiss-cpu>=1.7.0
google-generativeai>=0.3.0
python-jose>=3.3.0
```
## Project Structure
```
pdf_app/
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI application entry point
│   ├── config.py          # Configuration settings
│   ├── db.py             # Database connection handling
│   ├── services/
│   │   ├── __init__.py
│   │   ├── pdf_service.py # PDF processing service
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── pdf_routes.py  # API endpoints
├── requirements.txt
├── .env
└── README.md
```
## API Endpoints
### 1. Upload PDF
```http
POST /upload-pdf/
Content-Type: multipart/form-data
file: [PDF File]
```
Response:
```json
{
    "message": "PDF uploaded and processed successfully",
    "document_id": 1,
    "filename": "example.pdf"
}
```
### 2. Get Document
```http
GET /documents/{document_id}
```
Response:
```json
{
    "document_id": 1,
    "filename": "example.pdf",
    "content": "extracted text content"
}
```
### 3. Ask Question
```http
GET /ask-question/{document_id}?question=your_question_here
```
Response:
```json
{
    "question": "your question",
    "answer": "AI-generated answer based on document content"
}
```
## Running the Application
1. **Start the Application**
   ```bash
   uvicorn App.main:app --reload
   ```
  Ther is capital 'A' in the app, keep notice of it. 
  
   The application will be available at `http://localhost:8000`
1. **Access API Documentation**
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`
## Key Components
### PDFService
The `PDFService` class handles:
- PDF text extraction
- Document vectorization
- Question-answering using Gemini AI
- Vector store management with FAISS
### Database Operations
- Async PostgreSQL connections
- Document storage and retrieval
- Error handling and connection management
## Error Handling
The application implements comprehensive error handling for:
- Invalid file types
- Database connection issues
- PDF processing errors
- AI model errors
- Missing documents
## Performance Considerations
- Uses async/await for non-blocking operations
- Implements document caching with vector store
- Chunk-based text processing for large documents
- Connection pooling for database operations
## Security Considerations
1. Input validation for uploaded files
2. Secure storage of API keys
3. Database connection security
4. Rate limiting (recommended for production)
## Development Guidelines
1. Follow PEP 8 style guide
2. Implement proper error handling
3. Use type hints
4. Write docstrings for functions
5. Log important operations
## Troubleshooting
### Common Issues
1. **PDF Upload Fails**
   - Check file size limits
   - Verify PDF file integrity
   - Ensure proper permissions on uploads directory
2. **Database Connection Issues**
   - Verify PostgreSQL service is running
   - Check connection string in .env
   - Ensure database user permissions
3. **AI Model Errors**
   - Verify Gemini API key
   - Check API quota limits
   - Ensure proper network connectivity
## Contributing
1. Fork this repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request
## License
This project is licensed under the MIT License - see the LICENSE file for details.
