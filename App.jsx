import React, { useState } from 'react';

function App() {
  const [messages, setMessages] = useState([
    { role: 'ai', text: 'Hello! I am AROMI. How can I help you with your health today?' }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!input.trim()) return;

    // 1. Add User Message to UI
    const userMsg = { role: 'user', text: input };
    setMessages([...messages, userMsg]);
    setInput('');
    setLoading(true);

    try {
      // 2. Call your FastAPI Backend
      const response = await fetch('http://localhost:8000/api/chat/aromi-chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input }),
      });
      const data = await response.json();

      // 3. Add AI Response to UI
      setMessages(prev => [...prev, { role: 'ai', text: data.response }]);
    } catch (error) {
      setMessages(prev => [...prev, { role: 'ai', text: 'Error: Is the backend running?' }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <header style={styles.header}>ArogyaMitra AI</header>
      
      <div style={styles.chatBox}>
        {messages.map((msg, i) => (
          <div key={i} style={msg.role === 'user' ? styles.userRow : styles.aiRow}>
            <div style={msg.role === 'user' ? styles.userBubble : styles.aiBubble}>
              {msg.text}
            </div>
          </div>
        ))}
        {loading && <p style={{ color: '#888' }}>AROMI is typing...</p>}
      </div>

      <div style={styles.inputArea}>
        <input 
          style={styles.input}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSend()}
          placeholder="Ask me about diet or workouts..."
        />
        <button style={styles.button} onClick={handleSend}>Send</button>
      </div>
    </div>
  );
}

// Simple styles in plain JavaScript
const styles = {
  container: { height: '100vh', display: 'flex', flexDirection: 'column', backgroundColor: '#f5f5f5' },
  header: { backgroundColor: '#2c3e50', color: 'white', padding: '15px', textAlign: 'center', fontSize: '20px' },
  chatBox: { flex: 1, overflowY: 'auto', padding: '20px', display: 'flex', flexDirection: 'column', gap: '10px' },
  userRow: { display: 'flex', justifyContent: 'flex-end' },
  aiRow: { display: 'flex', justifyContent: 'flex-start' },
  userBubble: { backgroundColor: '#3498db', color: 'white', padding: '10px', borderRadius: '15px 15px 0 15px', maxWidth: '70%' },
  aiBubble: { backgroundColor: '#ecf0f1', color: '#333', padding: '10px', borderRadius: '15px 15px 15px 0', maxWidth: '70%', border: '1px solid #ddd' },
  inputArea: { padding: '20px', display: 'flex', gap: '10px', backgroundColor: 'white' },
  input: { flex: 1, padding: '10px', borderRadius: '5px', border: '1px solid #ddd', outline: 'none' },
  button: { padding: '10px 20px', backgroundColor: '#27ae60', color: 'white', border: 'none', borderRadius: '5px', cursor: 'pointer' }
};

export default App;
