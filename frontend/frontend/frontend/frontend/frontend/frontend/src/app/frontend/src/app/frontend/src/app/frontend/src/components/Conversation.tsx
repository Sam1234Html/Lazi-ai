import React, { useState } from 'react';

const Conversation: React.FC = () => {
  const [messages, setMessages] = useState<{ user: string; ai: any }[]>([]);
  const [input, setInput] = useState('');

  const handleSend = async () => {
    try {
      // TODO: Replace with actual API endpoint
      const response = await fetch('/api/conversation', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input, user_id: 'user123', curriculum_level: 'high-school' }),
      });
      const data = await response.json();
      setMessages([...messages, { user: input, ai: data }]);
      setInput('');
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="chat-container max-w-2xl w-full">
      {messages.map((msg, idx) => (
        <div key={idx} className="mb-4">
          <p className="font-bold">User: {msg.user}</p>
          <p>AI: {JSON.stringify(msg.ai)}</p> {/* TODO: Format guidance, references, skeleton */}
        </div>
      ))}
      <input
        className="w-full p-2 border border-deep-brown"
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <button
        className="mt-2 bg-warm-brown text-white p-2 rounded"
        onClick={handleSend}
      >
        Send
      </button>
    </div>
  );
};

export default Conversation;
