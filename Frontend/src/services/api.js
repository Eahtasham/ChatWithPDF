// Using relative URLs when using Vite proxy
const API_BASE = '/api';


//This  is the main entry point of your application when pdf is uploaded.

export const uploadPDF = async (file) => {
  const formData = new FormData();
  formData.append('file', file);   //Creating form data with the file as a key value pair to be  sent to the server.

  //handelling upload-pdf route of backend.
  const response = await fetch(`${API_BASE}/upload-pdf/`, {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    throw new Error('Upload failed');
  }

  return response.json();
};

export const askQuestion = async (documentId, question) => {
  const response = await fetch(
    `${API_BASE}/ask-question/${documentId}?question=${encodeURIComponent(question)}`  //Adding prams  to the url 
  );

  if (!response.ok) {
    throw new Error('Failed to get answer');
  }

  return response.json();
};