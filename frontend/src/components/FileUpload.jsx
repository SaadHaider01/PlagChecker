import { useState } from "react";
import axios from "axios";
import { toast, Toaster } from "react-hot-toast";

const FileUpload = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [isDragging, setIsDragging] = useState(false);
  const [previewError, setPreviewError] = useState(false);
  const [uploading, setUploading] = useState(false);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      setSelectedFile(file);
      setPreviewError(false);
    }
  };

  const handleDrop = (event) => {
    event.preventDefault();
    setIsDragging(false);
    const file = event.dataTransfer.files[0];
    if (file) {
      setSelectedFile(file);
      setPreviewError(false);
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
      toast.error("Upload failed due to: " + (error.response?.data?.message || error.message));
    } finally {
      setUploading(false);
    }
  };

  const handleDragOver = (event) => {
    event.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = () => {
    setIsDragging(false);
  };

  const handleRemoveFile = () => {
    setSelectedFile(null);
    setPreviewError(false);
  };

  const renderPreview = () => {
    if (!selectedFile) return null;

    const type = selectedFile.type;

    if (type === "application/pdf") {
      return (
        <iframe
          src={URL.createObjectURL(selectedFile)}
          className="w-full h-64 mt-4 border rounded"
          onError={() => setPreviewError(true)}
        />
      );
    }

    if (type === "text/plain") {
      return (
        <iframe
          src={URL.createObjectURL(selectedFile)}
          className="w-full h-64 mt-4 border rounded"
        />
      );
    }

    return <p className="text-gray-500 mt-4">Preview not available for this file type.</p>;
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <Toaster />
      <div className="max-w-4xl mx-auto py-12 px-4">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold mb-2">Plagiarism Checker</h1>
          <p className="text-gray-600">Upload your document to check for plagiarism.</p>
        </div>

        <form
          className="bg-white rounded-lg shadow-md p-6 space-y-6"
          onSubmit={handleUpload}
        >
          <div
            className={`border-2 border-dashed rounded-lg p-6 text-center transition-colors ${
              isDragging ? "border-blue-500 bg-blue-50" : "border-gray-300"
            }`}
            onDrop={handleDrop}
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
          >
            <input
              type="file"
              accept=".doc,.docx,.txt,.pdf"
              className="hidden"
              id="file-upload"
              onChange={handleFileChange}
            />
            <label
              htmlFor="file-upload"
              className="cursor-pointer flex flex-col items-center justify-center"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-12 w-12 text-gray-400 mb-3"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                strokeWidth={2}
              >
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
                <polyline points="17 8 12 3 7 8" />
                <line x1="12" y1="3" x2="12" y2="15" />
              </svg>

              {selectedFile ? (
                <div className="text-gray-700 font-medium">
                  📄 {selectedFile.name}{" "}
                  <span className="text-gray-400">• {selectedFile.type.split("/")[1].toUpperCase()}</span>
                </div>
              ) : (
                <>
                  <span className="text-gray-600">Click to upload or drag and drop</span>
                  <span className="text-sm text-gray-500 mt-1">
                    Supported formats: DOC, DOCX, TXT, PDF
                  </span>
                </>
              )}
            </label>

            {selectedFile && (
              <button
                type="button"
                className="mt-4 text-sm text-red-500 hover:underline"
                onClick={handleRemoveFile}
              >
                Remove File
              </button>
            )}
          </div>

          <button
            type="submit"
            className={`w-full flex items-center justify-center py-2 px-4 rounded-md text-sm font-medium text-white shadow-sm ${
              selectedFile ? "bg-green-600 hover:bg-green-700" : "bg-gray-400 cursor-not-allowed"
            }`}
            disabled={!selectedFile || uploading}
          >
            {uploading ? (
              <>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="mr-2 h-5 w-5 animate-spin"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth={2}
                >
                  <path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7z" />
                  <path d="M14 2v4a2 2 0 0 0 2 2h4" />
                  <path d="M10 9H8" />
                  <path d="M10 13H8" />
                  <path d="M10 17H8" />
                </svg>
                Uploading...
              </>
            ) : (
              "Check for Plagiarism"
            )}
          </button>

          {/* Preview section below the button */}
          {selectedFile && (
            <div className="mt-6">
              <h2 className="text-md font-semibold text-gray-700 mb-2">Preview:</h2>
              {previewError ? (
                <div className="bg-red-100 text-red-700 p-3 rounded">⚠️ Failed to load preview.</div>
              ) : (
                renderPreview()
              )}
            </div>
          )}
        </form>
      </div>
    </div>
  );
};

export default FileUpload;
