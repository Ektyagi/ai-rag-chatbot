import { Plus, Upload, MessageSquare } from "lucide-react";

export default function Sidebar({
  conversations = [],
  activeId,
  onSelectConversation,
  onNewChat,
}) {
  return (
    <div className="w-72 bg-slate-950 border-r border-slate-700 p-5 flex flex-col">
      {/* New Chat */}
      <button
        onClick={onNewChat}
        className="w-full flex items-center justify-center gap-2 bg-blue-600 rounded-lg py-3 hover:bg-blue-700 transition"
      >
        <Plus size={18} />
        New Chat
      </button>

      {/* Upload */}
      <button className="w-full flex items-center justify-center gap-2 mt-4 border border-slate-600 rounded-lg py-3 hover:bg-slate-800 transition">
        <Upload size={18} />
        Upload PDF
      </button>

      {/* Conversations */}
      <div className="mt-8 flex-1 overflow-y-auto">
        <h2 className="text-gray-400 text-sm mb-3">Recent Chats</h2>

        <div className="space-y-2">
          {conversations.length === 0 && (
            <p className="text-gray-500 text-sm">No conversations yet.</p>
          )}

          {conversations.map((conversation) => (
            <button
              key={conversation.id}
              onClick={() => onSelectConversation(conversation.id)}
              className={`w-full flex items-center gap-3 text-left px-3 py-3 rounded-lg transition ${
                activeId === conversation.id
                  ? "bg-slate-700"
                  : "hover:bg-slate-800"
              }`}
            >
              <MessageSquare size={16} />

              <span className="truncate">{conversation.title}</span>
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}
