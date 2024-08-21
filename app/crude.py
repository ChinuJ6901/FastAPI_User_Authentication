# app/crud.py
from app.database import get_db_connection


def check_user_credentials(username: str, password: str):
    conn = get_db_connection()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        return result is not None
    finally:
        conn.close()
