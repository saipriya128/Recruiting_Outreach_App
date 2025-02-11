import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = openai.OpenAI(api_key="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")

def chat_with_openai(user_input):
    """Processes chat input and returns AI response using OpenAI API."""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert recruiting assistant. Guide users in crafting personalized outreach sequences for recruiting. A friendly AI that helps users create highly effective outreach sequences by asking smart follow-up questions."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

def process_chat(user_input):
    """Handles user messages and generates AI responses dynamically."""
    return chat_with_openai(user_input)

# Test the AI
if __name__ == "__main__":
    print("🤖 Helix AI is running! Type 'exit' to stop.")
    while True:
        user_message = input("User: ")
        if user_message.lower() == "exit":
            break
        response = process_chat(user_message)
        print(f"Helix: {response}")
