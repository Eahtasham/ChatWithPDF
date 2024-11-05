import React, { useState } from 'react';
import { Upload, Loader2 } from 'lucide-react';
import { usePDFContext } from '../../context/PDFContext';
import { uploadPDF } from '../../services/api';
import FilePreview from './FilePreview';

const PDFUploader = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const { setDocumentId, setFileName } = usePDFContext();  //using  the context to get the state and update it


  const handleFileUpload = async (e) => {
    const file = e.target.files[0];
    if (file && file.type === 'application/pdf') {        //explicitly choosing filetype to pdf for  upload

      setLoading(true);
      try {
        const data = await uploadPDF(file);
        setDocumentId(data.document_id);
        setFileName(file.name);
        setError('');
      } catch (err) {
        setError('Failed to upload PDF. Please try again.');
      } finally {
        setLoading(false);
      }
    } else {
      setError('Please select a valid PDF file');
    }
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <div className="flex items-center justify-center w-full">
        <label className="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100">
          <div className="flex flex-col items-center justify-center pt-5 pb-6">
            {loading ? (
              <Loader2 className="w-12 h-12 text-gray-400 animate-spin" />
            ) : (
              <>
                <Upload className="w-12 h-12 text-green-600 mb-4" />
                <p className="mb-2 text-sm text-gray-500">
                  <span className="font-semibold">Click to upload</span>
                </p>
                <p className="text-xs text-gray-500">PDF files only</p>
              </>
            )}
          </div>
          <input
            type="file"
            className="hidden"
            accept=".pdf"
            onChange={handleFileUpload}
            disabled={loading}
          />
        </label>
      </div>
      <FilePreview />
      {error && (
        <div className="mt-4 p-4 bg-red-50 text-red-600 rounded-md">
          {error}
        </div>
      )}
    </div>
  );
};

export default PDFUploader;