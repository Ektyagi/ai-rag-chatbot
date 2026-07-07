import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

export const sendMessage = async (question, history = []) => {
  const response = await api.post("/v1/chat", {
    question,
    history,
  });

  return response.data;
};

export default api;