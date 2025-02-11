import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from database import db
from routes.chat import chat_bp
from routes.sequence import sequence_bp

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # <-- Fix CORS issue

# Load Configurations
app.config.from_object("config.Config")

# Initialize Database
db.init_app(app)
migrate = Migrate(app, db)

# Register Blueprints
app.register_blueprint(chat_bp, url_prefix="/chat")
app.register_blueprint(sequence_bp, url_prefix="/sequence")

# Home Route
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Recruiting Outreach AI API!"}), 200

# Ensure API Key is Set
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("❌ OPENAI_API_KEY is missing! Set it in the .env file.")

if __name__ == "__main__":
    print("✅ Flask app is running at http://127.0.0.1:5000/")
    app.run(debug=True)
