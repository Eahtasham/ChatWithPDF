
# ChatWithPDF

## Description
**ChatWithPDF** is a full-stack application that enables users to interact with the contents of an uploaded PDF through a chat interface. By processing the PDF, the app allows users to ask questions and receive answers, simulating a conversational experience with the document.

## Installation for Backend

To get started, follow these steps:

1. **Fork the Repository**: Begin by forking this repository to your own GitHub account.
2. **Clone the Repository**: After forking, clone the repository to your local machine:
   ```bash
   git clone https://github.com/Eahtasham/ChatWithPDF.git
   cd ChatWithPDF
   ```
3. **Install Requirements**: Install the necessary Python packages listed in `requirements.txt`. Make sure you’re using Python 3.8 or higher.
   ```bash
   pip install -r requirements.txt

## Configuration

1. **API Keys**: Add your **Gemini API key** to the `.env` file in the project root.
2. **Database URL**: Specify your **PostgreSQL database URL** in the `.env` file for database connectivity.

Your `.env` file should look something like this:
   ```plaintext
   GEMINI_API_KEY=your_gemini_api_key_here
   DATABASE_URL=your_postgresql_database_url_here
   ```

## Usage

1. **Upload a PDF**: Start the app and upload a PDF document through the provided interface.
2. **Ask Questions**: After uploading, you can ask questions based on the content of the PDF.
3. **Receive Answers**: The application will analyze your queries and respond with relevant answers from the document’s contents.

## Features

- **PDF Upload and Processing**: Easily upload a PDF file for analysis.
- **Interactive Chat**: Engage in a conversational Q&A format with the content of the uploaded PDF.
- **Answer Extraction**: Get answers extracted directly from the text of the PDF.

## Dependencies

The project relies on the following libraries and packages:

- **fastapi**: For creating the API endpoints.
- **asyncpg**: Async PostgreSQL client for database interactions.
- **python-dotenv**: For environment variable management.
- **PyMuPDF**: Used for extracting text from PDF documents.
- **langchain**: For managing the language processing chain.
- **typing**: Built-in type hints support.
- **logging**: Standard logging library for debugging and monitoring.
- **dotenv**, **os**, **tracemalloc**: Various utilities for managing configurations and optimizing performance.

Install all dependencies with:
   ```bash
   pip install -r requirements.txt
   ```

## License

This project is licensed under MIT. Please refer to the LICENSE file for more details.
```
