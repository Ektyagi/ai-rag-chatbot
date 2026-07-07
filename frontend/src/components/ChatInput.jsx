import { useState } from "react";
import { Send } from "lucide-react";

export default function ChatInput({ onSend, loading }) {
  const [text, setText] = useState("");

  const handleSend = () => {
    if (!text.trim()) return;

    onSend(text);

    setText("");
  };

  return (
    <div className="border-t border-slate-700 p-6">
      <div className="flex max-w-4xl mx-auto">
        <input
          value={text}
          onChange={(e) => setText(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              handleSend();
            }
          }}
          placeholder="Ask anything about your documents..."
          className="flex-1 bg-slate-800 rounded-l-xl px-5 outline-none h-12"
        />

        <button
          onClick={handleSend}
          disabled={loading}
          className="bg-blue-600 px-6 rounded-r-xl disabled:bg-gray-600"
        >
          <Send size={18} />
        </button>
      </div>
    </div>
  );
}
