import { useState } from "react";

const API_BASE_URL = "http://127.0.0.1:5000"; // Flask backend URL

export default function ChatBar({ onSendMessage }: { onSendMessage: (message: string, sender: string) => void }) {
    const [message, setMessage] = useState("");
    const [loading, setLoading] = useState(false);

    const handleSendMessage = async () => {
        if (!message.trim()) return;

        // Immediately add user's message to chat
        onSendMessage(message, "user");

        setMessage(""); // Clear input box
        setLoading(true);

        try {
            // Send message to Flask backend
            const response = await fetch(`${API_BASE_URL}/chat/`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message }),
            });

            if (!response.ok) {
                throw new Error(`Server error: ${response.status}`);
            }

            const data = await response.json();
            console.log("AI Response:", data);

            // Add AI response to chat
            onSendMessage(data.response, "ai");

        } catch (error) {
            console.error("Error communicating with AI:", error);
        }

        setLoading(false);
    };

    return (
        <div className="chat-input-container">
            <input
                type="text"
                className="chat-input"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Type a message..."
            />
            <button className="chat-send" onClick={handleSendMessage} disabled={loading}>
                {loading ? "Sending..." : "Send"}
            </button>
        </div>
    );
}
