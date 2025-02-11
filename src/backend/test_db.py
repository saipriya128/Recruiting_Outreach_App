from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:root123@localhost/recruiting_db"

try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    print("PostgreSQL connection successful!")
    connection.close()
except Exception as e:
    print("PostgreSQL connection failed:", str(e))
