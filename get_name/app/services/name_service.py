from app.utils.db import get_db_connection

def fetch_name(email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT email FROM users WHERE email = ?", email)
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None
