# ChatWithPDF

A React application that allows users to upload PDF documents and ask questions about their content. The application features a modern, responsive UI with real-time feedback and error handling.

## Features

- PDF document upload with drag-and-drop support
- Interactive Q&A interface
- Real-time feedback and loading states
- Responsive design for all devices
- Error handling and validation
- Clean and modern UI

## Prerequisites

Before you begin, ensure you have installed:
- [Node.js](https://nodejs.org/) (version 14.0.0 or higher)
- npm (usually comes with Node.js)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Eahtasham/ChatWithPDF.git
cd pdf-qa-app
```

2. Install dependencies:
```bash
npm install
```

This will install the following dependencies:
- React (Core framework)
- Vite (Build tool)
- Tailwind CSS (Styling)
- Lucide React (Icons)
- Other development dependencies

## Project Setup

1. Set up Tailwind CSS:
```bash
npx tailwindcss init -p
```

2. Configure your environment variables (if needed):
```bash
cp .env.example .env
```

3. Update the API endpoint in `src/services/api.js` if necessary:
```javascript
const API_BASE_URL = 'http://127.0.0.1:8000/api';
```

## Development

To start the development server:

```bash
npm run dev
```

The application will be available at `http://localhost:3000`

## Building for Production

To create a production build:

```bash
npm run build
```

To preview the production build:

```bash
npm run preview
```

## Project Structure

```
pdf-qa-app/
├── public/
├── src/
│   ├── components/
│   │   ├── layout/
│   │   │   └── Header.jsx        # Application header
│   │   ├── pdf/
│   │   │   ├── PDFUploader.jsx   # PDF upload component
│   │   │   └── FilePreview.jsx   # PDF preview component
│   │   └── qa/
│   │       ├── QuestionInput.jsx # Question input form
│   │       └── AnswerList.jsx    # Q&A display component
│   ├── context/
│   │   └── PDFContext.jsx        # PDF state management
│   ├── services/
│   │   └── api.js                # API service functions
│   ├── styles/
│   │   └── index.css             # Global styles
│   ├── App.jsx                   # Main application component
│   └── main.jsx                  # Application entry point
├── index.html
├── vite.config.js
├── tailwind.config.js
└── package.json
```

## API Endpoints

The application interacts with two main endpoints:

1. PDF Upload:
   - Endpoint: `POST /api/upload-pdf/`
   - Body: FormData with 'file' key containing the PDF

2. Ask Question:
   - Endpoint: `GET /api/ask-question/{document_id}?question={question}`
   - Parameters: 
     - document_id: ID received from upload
     - question: URL-encoded question text

## Dependencies

Main dependencies:
```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "lucide-react": "^0.263.1"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.0.0",
    "autoprefixer": "^10.4.14",
    "postcss": "^8.4.24",
    "tailwindcss": "^3.3.2",
    "vite": "^4.3.9"
  }
}
```

## Development Guidelines

1. **Component Structure**: 
   - Each component should be in its own file
   - Use functional components with hooks
   - Keep components focused and single-responsibility

2. **Styling**:
   - Use Tailwind CSS classes for styling
   - Follow mobile-first approach
   - Keep styles modular and reusable

3. **State Management**:
   - Use Context API for global state
   - Use local state for component-specific data
   - Keep state updates clean and predictable

4. **Error Handling**:
   - Implement proper error boundaries
   - Show user-friendly error messages
   - Log errors appropriately

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details

## Contact

Eahtasham Ummam - eahtashamummam@gmail.com
Project Link: https://github.com/Eahtasham/ChatWithPDF
