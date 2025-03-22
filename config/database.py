import os
from dotenv import load_dotenv
import mysql.connector


def db_connection():
    # Load .env file from current directory
    load_dotenv()

    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE")
    )

    return conn
