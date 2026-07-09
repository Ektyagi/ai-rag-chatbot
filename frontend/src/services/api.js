import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

// ===============================
// Chat API
// ===============================

export const sendMessage = async (conversationId, question) => {
  const response = await api.post("/v1/chat", {
    conversation_id: conversationId,
    question,
  });

  return response.data;
};

// ===============================
// Upload PDF API
// ===============================

export const uploadPdf = async (file) => {
  const formData = new FormData();

  formData.append("file", file);

  const response = await api.post(
    "/v1/upload",
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
};

export default api;