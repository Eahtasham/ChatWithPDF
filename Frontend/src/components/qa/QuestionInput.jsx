import React, { useState } from 'react';
import { Send, Loader2 } from 'lucide-react';
import { usePDFContext } from '../../context/PDFContext';
import { askQuestion } from '../../services/api';

const QuestionInput = ({ onNewAnswer }) => {
  const [question, setQuestion] = useState('');
  const [loading, setLoading] = useState(false);
  const { documentId } = usePDFContext();   //using custom  hook to get documentId from context


  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!question.trim()) return;
    
    setLoading(true);
    try {
      const data = await askQuestion(documentId, question);
      onNewAnswer({ question, answer: data.answer });
      setQuestion('');
    } catch (err) {
      console.error('Failed to get answer:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <form onSubmit={handleSubmit} className="flex gap-4">
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask a question about the document..."
          className="flex-1 p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500"
          disabled={loading}
        />
        <button
          type="submit"
          disabled={loading || !question.trim()}
          className="px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700 disabled:cursor-not-allowed flex items-center gap-2"
        >
          {loading ? (
            <Loader2 className="w-4 h-4 animate-spin" />
          ) : (
            <Send className="w-4 h-4" />
          )}
          Ask
        </button>
      </form>
    </div>
  );
};

export default QuestionInput;