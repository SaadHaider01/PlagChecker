import { useState } from "react";

const FileUpload = ({ onFileSelect }) => {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      setSelectedFile(file);
      onFileSelect(file);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center p-6 border-2 border-dashed border-gray-400 rounded-lg">
      <label className="cursor-pointer bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600">
        Upload Document
        <input
          type="file"
          accept=".doc, .docx, .txt, .pdf"
          onChange={handleFileChange}
          className="hidden"
        />
      </label>

      {selectedFile && (
        <p className="mt-3 text-gray-700">Selected File: {selectedFile.name}</p>
      )}
    </div>
  );
};

export default FileUpload;
