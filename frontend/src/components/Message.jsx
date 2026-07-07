export default function Message({ role, content, sources = [] }) {
  const isUser = role === "user";

  return (
    <div className={`flex mb-6 ${isUser ? "justify-end" : "justify-start"}`}>
      <div
        className={`max-w-3xl px-5 py-3 rounded-2xl whitespace-pre-wrap ${
          isUser ? "bg-blue-600 text-white" : "bg-slate-800 text-gray-100"
        }`}
      >
        {/* Message */}
        <div>{content}</div>

        {/* Sources (AI messages only) */}
        {!isUser && sources.length > 0 && (
          <div className="mt-4 border-t border-slate-700 pt-3">
            <h4 className="text-sm font-semibold text-gray-300 mb-2">
              📄 Sources
            </h4>

            <div className="space-y-2">
              {sources.map((source, index) => (
                <div
                  key={index}
                  className="rounded-lg border border-slate-600 bg-slate-700 p-3"
                >
                  <div className="font-semibold text-white">
                    📄 {source.source}
                  </div>

                  <div className="mt-1 text-gray-300">
                    <strong>Relevant Chunks:</strong> {source.chunks.length}
                  </div>

                  <div className="mt-1 text-gray-400 text-xs">
                    {source.chunks.join(", ")}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
