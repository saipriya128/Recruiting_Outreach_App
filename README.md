# 🤖 Recruit AI - Recruiting Assistant

Recruit AI is an AI-driven recruiting outreach assistant that helps users craft personalized outreach sequences. It engages in a back-and-forth conversation to refine messaging, structure, and tone. Built with **Flask, OpenAI API, PostgreSQL, and CrewAI**, this application dynamically updates the sequence based on user interactions.

---

## 🚀 Features

- **Interactive Chat**: AI-driven conversation to guide users in creating effective outreach sequences.
- **Dynamic Updates**: AI continuously refines the sequence based on user input.
- **Flask Backend**: Handles chat processing and API integration.
- **PostgreSQL Database**: Stores user preferences and outreach sequences.
- **Modern UI**: Developed with **React + TypeScript + Vite** for an elegant, responsive experience.
- **CrewAI Integration**: AI-powered agent (`Helix`) enhances user experience with smart interactions.

---

## 🛠️ Installation & Setup

### 🔹 1️⃣ Clone the Repository
sh

git clone https://github.com/saipriya128/Recruiting_Outreach_App.git

cd Recruiting_Outreach_App

Setup the Backend (Flask + PostgreSQL)

Create and activate a virtual environment:

python -m venv venv

source venv/bin/activate  # Mac/Linux

venv\Scripts\activate     # Windows

Set up environment variables: Create a .env file in the backend/ directory and add:

OPENAI_API_KEY=your-openai-api-key

DATABASE_URL=postgresql://username:password@localhost/recruiting_db

Run the Flask backend:

python app.py

## Setup the Frontend (React + Vite)

Navigate to frontend directory:

cd frontend

Install dependencies:

npm install

Start the frontend:

npm run dev
