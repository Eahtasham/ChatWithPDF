# ChatWithPDF
## Description
**ChatWithPDF** is a full-stack application that enables users to interact with the contents of an uploaded PDF through a chat interface. By processing the PDF, the app allows users to ask questions and receive answers, simulating a conversational experience with the document.

## Repository Structure
This repository contains both frontend and backend components of the application. Detailed documentation for each component can be found in their respective directories:

- `/frontend` - React-based user interface
- `/backend` - FastAPI-based server application

Please refer to the README.md files in each directory for specific setup and installation instructions:
- [Backend Documentation](https://github.com/Eahtasham/ChatWithPDF/blob/main/Backend/README.md)
- [Frontend Documentation](https://github.com/Eahtasham/ChatWithPDF/blob/main/Frontend/README.md)

## Quick Start
1. **Fork the Repository**: Begin by forking this repository to your own GitHub account.
2. **Clone the Repository**: After forking, clone the repository to your local machine:
   ```bash
   git clone https://github.com/Eahtasham/ChatWithPDF.git
   cd ChatWithPDF
   ```

## Features
- **PDF Upload and Processing**: Easily upload a PDF file for analysis.
- **Interactive Chat**: Engage in a conversational Q&A format with the content of the uploaded PDF.
- **Answer Extraction**: Get answers extracted directly from the text of the PDF.

## Tech Stack
### Backend
- FastAPI
- PostgreSQL
- Google Gemini AI
- LangChain
- FAISS

### Frontend
- React
- TypeScript
- Tailwind CSS
- Material UI

## Project Setup
For detailed setup instructions, please refer to:
- Backend setup: See `/backend/README.md`
- Frontend setup: See `/frontend/README.md`

## Dependencies
The project is split into two main components, each with its own dependencies:

### Backend Dependencies
- FastAPI and related packages
- PostgreSQL client (asyncpg)
- PDF processing tools
- AI/ML libraries
- See `/backend/requirements.txt` for complete list

### Frontend Dependencies
- React and related packages
- UI component libraries
- State management tools
- See `/frontend/package.json` for complete list

## Configuration
Each component requires its own configuration:

### Backend Configuration
Create a `.env` file in the backend directory:
```plaintext
GEMINI_API_KEY=your_gemini_api_key_here
DATABASE_URL=your_postgresql_database_url_here
```

### Frontend Configuration
Configure the API endpoint in the frontend environment files.

## Usage
1. **Upload a PDF**: Start the app and upload a PDF document through the provided interface.
2. **Ask Questions**: After uploading, you can ask questions based on the content of the PDF.
3. **Receive Answers**: The application will analyze your queries and respond with relevant answers from the document's contents.

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under MIT. Please refer to the LICENSE file for more details.
