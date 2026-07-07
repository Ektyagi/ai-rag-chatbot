import { useState } from "react";

export default function useConversations() {
  const [conversations, setConversations] = useState([
    {
      id: Date.now(),
      title: "New Chat",
      messages: [],
      createdAt: new Date(),
    },
  ]);

  const [activeId, setActiveId] = useState(conversations[0].id);

  const activeConversation =
    conversations.find((c) => c.id === activeId) || conversations[0];

  const createConversation = () => {
    const newConversation = {
      id: Date.now(),
      title: "New Chat",
      messages: [],
      createdAt: new Date(),
    };

    setConversations((prev) => [...prev, newConversation]);
    setActiveId(newConversation.id);
  };

  const updateMessages = (messages) => {
    setConversations((prev) =>
      prev.map((conversation) =>
        conversation.id === activeId
          ? {
              ...conversation,
              messages,
            }
          : conversation
      )
    );
  };

  const renameConversation = (title) => {
    setConversations((prev) =>
      prev.map((conversation) =>
        conversation.id === activeId
          ? {
              ...conversation,
              title,
            }
          : conversation
      )
    );
  };

  return {
    conversations,
    activeConversation,
    activeId,
    setActiveId,
    createConversation,
    updateMessages,
    renameConversation,
  };
}