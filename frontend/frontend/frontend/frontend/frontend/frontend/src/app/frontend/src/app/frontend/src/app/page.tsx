import Conversation from '../components/Conversation';

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center p-24">
      <h1 className="text-4xl font-bold text-deep-brown">Lazy AI</h1>
      <Conversation />
    </main>
  );
}
