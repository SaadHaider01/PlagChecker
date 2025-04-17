import { useState } from "react";
import axios from "axios";
import { toast } from "sonner";

const FileUpload = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [previewURL, setPreviewURL] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      setSelectedFile(file);
      setPreviewURL(URL.createObjectURL(file));
    }
  };

  const handleUpload = async (e) => {
    e.preventDefault();
    if (!selectedFile) {
      toast.error("Please select a file first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      setUploading(true);
      const response = await axios.post("http://localhost:5000/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      toast.success(response.data.message || "File uploaded successfully!");
    } catch (error) {
      console.error(error);
      toast.error("Error uploading file.");
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-4xl mx-auto py-12 px-4">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold mb-2">Plagiarism Checker</h1>
          <p className="text-gray-600">Upload your document to check for plagiarism.</p>
        </div>

        <div className="bg-white rounded-lg shadow-md p-6 mb-8">
          <form onSubmit={handleUpload} className="space-y-4">
            <div className="border-2 border-dashed border-gray-300 rounded-lg p-6 text-center">
              <input
                type="file"
                accept=".doc,.docx,.txt,.pdf"
                className="hidden"
                id="file-upload"
                onChange={handleFileChange}
              />
              <label htmlFor="file-upload" className="cursor-pointer flex flex-col items-center justify-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="lucide lucide-upload h-12 w-12 text-gray-400 mb-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
                  <polyline points="17 8 12 3 7 8" />
                  <line x1="12" x2="12" y1="3" y2="15" />
                </svg>
                <span className="text-gray-600">Click to upload or drag and drop</span>
                <span className="text-sm text-gray-500 mt-1">Supported: DOC, DOCX, TXT, PDF</span>
              </label>
            </div>

            {selectedFile && (
              <p className="text-center text-gray-700">Selected File: {selectedFile.name}</p>
            )}

            <button
              type="submit"
              className={`w-full flex items-center justify-center py-2 px-4 rounded-md text-white shadow-sm text-sm font-medium ${
                uploading ? "bg-gray-400 cursor-not-allowed" : "bg-blue-600 hover:bg-blue-700"
              }`}
              disabled={uploading}
            >
              {uploading ? (
                <>
                  <svg className="animate-spin mr-2 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z" />
                  </svg>
                  Uploading...
                </>
              ) : (
                <>
                  <svg className="-ml-1 mr-2 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7z" />
                    <path d="M14 2v4a2 2 0 0 0 2 2h4" />
                    <path d="M10 9H8M10 13H8M10 17H8" />
                  </svg>
                  <span>Check for Plagiarism</span>
                </>
              )}
            </button>
          </form>
        </div>

        {previewURL && selectedFile?.type === "application/pdf" && (
          <div className="bg-white p-4 rounded-md shadow-md">
            <h2 className="text-xl font-semibold mb-2">File Preview:</h2>
            <iframe src={previewURL} className="w-full h-96 border" title="PDF Preview"></iframe>
          </div>
        )}
      </div>
    </div>
  );
};

export default FileUpload;
