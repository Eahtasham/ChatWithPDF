import React, { useState } from 'react';
import Header from './components/layout/Header';
import PDFUploader from './components/pdf/PDFUploader';
import QuestionInput from './components/qa/QuestionInput';
import AnswerList from './components/qa/AnswerList';
import { usePDFContext } from './context/PDFContext';
import FilePreview from './components/pdf/FilePreview';

function App() {
  const [qaList, setQAList] = useState([]);
  const { documentId } = usePDFContext();

  const handleNewAnswer = (qa) => {
    setQAList([...qaList, qa]);
  };

  return (
    <div className="min-h-screen bg-gray-50 p-4 md:p-8">
      <div className="max-w-4xl mx-auto space-y-8">
        <Header />
        <PDFUploader />
        {documentId && <QuestionInput onNewAnswer={handleNewAnswer} />}
        {qaList.length > 0 && <AnswerList qaList={qaList} />}
      </div>
    </div>
  );
}

export default App;