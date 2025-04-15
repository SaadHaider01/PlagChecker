import { useState } from "react";
import axios from "axios";

const FileUpload = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadMessage, setUploadMessage] = useState("");

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      setSelectedFile(file);
    }
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      setUploadMessage("Please select a file first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await axios.post("http://localhost:5000/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      setUploadMessage(response.data.message);
    } catch (error) {
      setUploadMessage("Error uploading file.",error.message);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center p-6 border-2 border-dashed border-gray-400 rounded-lg">
      <label className="cursor-pointer bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600">
        Upload Document
        <input type="file" accept=".doc, .docx, .txt, .pdf" onChange={handleFileChange} className="hidden" />
      </label>

      {selectedFile && (
        <p className="mt-3 text-gray-700">Selected File: {selectedFile.name}</p>
      )}

      <button onClick={handleUpload} className="mt-4 bg-green-500 text-white py-2 px-4 rounded-md hover:bg-green-600">
        Submit
      </button>

      {uploadMessage && <p className="mt-3 text-gray-700">{uploadMessage}</p>}
    </div>
  );
};

export default FileUpload;
