// Using relative URLs when using Vite proxy
const API_BASE = '/api';

export const uploadPDF = async (file) => {
  const formData = new FormData();
  formData.append('file', file);

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
    `${API_BASE}/ask-question/${documentId}?question=${encodeURIComponent(question)}`
  );

  if (!response.ok) {
    throw new Error('Failed to get answer');
  }

  return response.json();
};