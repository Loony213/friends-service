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

def add_friend(user_email: str, friend_email: str):
    conn = get_connection()
    cursor = conn.cursor()

    # Verifica que ambos usuarios existan
    cursor.execute("SELECT id FROM users WHERE email = ?", user_email)
    user = cursor.fetchone()
    cursor.execute("SELECT id FROM users WHERE email = ?", friend_email)
    friend = cursor.fetchone()

    if not user or not friend:
        raise HTTPException(status_code=404, detail="Uno o ambos usuarios no existen")

    cursor.execute("INSERT INTO friends (user_id, friend_id) VALUES (?, ?)", user.id, friend.id)
    conn.commit()
    return {"message": "Amigo agregado correctamente"}
