import pyodbc
from fastapi import HTTPException

# Configuración de conexión a SQL Server
server = 'auth-db.cnck2sieyjue.us-east-1.rds.amazonaws.com'
database = 'auth_db'
username = 'admin'
password = 'Distribuida123'
connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"

def get_connection():
    return pyodbc.connect(connection_string)

def get_friends(email: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE email = ?", email)
    user = cursor.fetchone()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    cursor.execute("""
        SELECT u.email FROM friends f
        JOIN users u ON u.id = f.friend_id
        WHERE f.user_id = ?
    """, user.id)
    friends = [row.email for row in cursor.fetchall()]
    return friends
