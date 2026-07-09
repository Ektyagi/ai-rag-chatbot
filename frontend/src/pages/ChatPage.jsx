import { useState } from "react";

import Sidebar from "../components/Sidebar";
import Header from "../components/Header";
import ChatWindow from "../components/ChatWindow";
import ChatInput from "../components/ChatInput";

import useConversations from "../hooks/useConversations";

import { sendMessage } from "../services/api";

export default function ChatPage() {
  const [loading, setLoading] = useState(false);

  const {
    conversations,
    activeConversation,
    activeId,
    setActiveId,
    createConversation,
    updateMessages,
    renameConversation,
  } = useConversations();

  const messages = activeConversation.messages;

  const handleSend = async (text) => {
    if (!text.trim()) return;

    // User message
    const userMessage = {
      role: "user",
      content: text,
    };

    const updatedMessages = [...messages, userMessage];

    updateMessages(updatedMessages);

    // Rename conversation after first message
    if (
      activeConversation.title === "New Chat" &&
      updatedMessages.length === 1
    ) {
      renameConversation(
        text.length > 35 ? text.substring(0, 35) + "..." : text,
      );
    }

    setLoading(true);

    try {
      // Send conversation ID and question
      const response = await sendMessage(
        activeConversation.id.toString(),
        text,
      );

      const assistantMessage = {
        role: "assistant",
        content:
          response.answer ||
          response.response ||
          response.message ||
          "No response received.",
        sources: response.sources || [],
      };

      updateMessages([...updatedMessages, assistantMessage]);
    } catch (error) {
      console.error(error);

      updateMessages([
        ...updatedMessages,
        {
          role: "assistant",
          content: "⚠️ Unable to connect to the backend.",
          sources: [],
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex h-screen bg-slate-900 text-white">
      <Sidebar
        conversations={conversations}
        activeId={activeId}
        onSelectConversation={setActiveId}
        onNewChat={createConversation}
      />

      <div className="flex flex-col flex-1">
        <Header />

        <ChatWindow messages={messages} loading={loading} />

        <ChatInput onSend={handleSend} loading={loading} />
      </div>
    </div>
  );
}
