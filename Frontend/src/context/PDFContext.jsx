//Instead of passing props everywhere, 
//we are using a context to share data between components

import React, { createContext, useContext, useState } from 'react';

const PDFContext = createContext();

//pdfprovider to  wrap the app
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

//custom  hook to get the context


export const usePDFContext = () => {
  const context = useContext(PDFContext);
  if (!context) {
    throw new Error('usePDFContext must be used within a PDFProvider');
  }
  return context;
};