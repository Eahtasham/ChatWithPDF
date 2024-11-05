import React from 'react';
import { FileText } from 'lucide-react';
import { usePDFContext } from '../../context/PDFContext';

const FilePreview = () => {
  const { fileName } = usePDFContext();    //using custome hook  to get the fileName from context


  if (!fileName) return null;

  return (
    <div className="mt-4 p-4 bg-green-50 flex items-center gap-2 text-sm text-green-600">
        <p>Uploaded PDF: </p>
      <FileText className="w-4 h-4" />
      <span>{fileName}</span>
    </div>
  );
};

export default FilePreview;