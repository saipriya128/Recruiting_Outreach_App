import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:root123@localhost/recruiting_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENAI_API_KEY = os.getenv("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")
