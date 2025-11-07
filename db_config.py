import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Load environment variables
load_dotenv()

def get_engine():
    """Creates a SQLAlchemy engine for MySQL."""
    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "bhavani09@")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "3306")
    database = os.getenv("DB_NAME", "moviesdb")

    # Encode password to handle special characters like @
    password = quote_plus(password)

    # Build connection string
    connection_str = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    print("🔗 Connection string used:", connection_str)

    try:
        engine = create_engine(connection_str)
        # Test connection immediately
        conn = engine.connect()
        print(" SQLAlchemy connection successful!")
        conn.close()
        return engine
    except Exception as e:
        print("SQLAlchemy connection failed:", e)
        raise
