from .database import get_db_connection


def check_user_credentials(username: str, password: str) -> bool:
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    SELECT COUNT(*) FROM users
    WHERE username = %s AND password = %s
    """
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    conn.close()
    return result[0] > 0