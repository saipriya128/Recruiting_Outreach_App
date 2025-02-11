import { useState } from "react";
import ChatBar from "./ChatBar";

export default function DynamicWorkspace() {
    const [messages, setMessages] = useState<{ text: string; sender: string }[]>([]);

    const handleNewMessage = (text: string, sender: string) => {
        setMessages((prevMessages) => [...prevMessages, { text, sender }]);
    };

    return (
        <div className="workspace-container">
            <div className="workspace-header">Recruiting Outreach AI</div>
            <div className="chat-messages">
                {messages.map((msg, index) => (
                    <div key={index} className={msg.sender === "user" ? "user-message" : "ai-message"}>
                        {msg.text}
                    </div>
                ))}
            </div>
            <ChatBar onSendMessage={handleNewMessage} />
        </div>
    );
}
