import Message from "./Message";

export default function ChatWindow({ messages, loading }) {
  return (
    <div className="flex-1 overflow-auto p-8">
      <div className="max-w-4xl mx-auto">
        {messages.length === 0 ? (
          <div className="text-center mt-40">
            <h2 className="text-3xl font-bold">ROMEO</h2>

            <p className="mt-4 text-gray-400">
              Upload a PDF and ask questions.
            </p>
          </div>
        ) : (
          <>
            {messages.map((msg, index) => (
              <Message
                key={index}
                role={msg.role}
                content={msg.content}
                sources={msg.sources || []}
              />
            ))}

            {loading && (
              <Message role="assistant" content="Thinking..." sources={[]} />
            )}
          </>
        )}
      </div>
    </div>
  );
}
