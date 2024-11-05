import React, { createContext, useContext, useState } from 'react';

const PDFContext = createContext();

export const PDFProvider = ({ children }) => {
  const [documentId, setDocumentId] = useState(null);
  const [fileName, setFileName] = useState(null);

  return (
    <PDFContext.Provider value={{ 
      documentId, 
      setDocumentId, 
      fileName, 
      setFileName 
    }}>
      {children}
    </PDFContext.Provider>
  );
};

export const usePDFContext = () => {
  const context = useContext(PDFContext);
  if (!context) {
    throw new Error('usePDFContext must be used within a PDFProvider');
  }
  return context;
};