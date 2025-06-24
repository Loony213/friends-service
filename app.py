from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pyodbc

app = FastAPI()

# Permitir solicitudes desde cualquier origen (para desarrollo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes cambiar "*" por ["http://18.234.144.71"] si quieres limitarlo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuración de conexión a SQL Server
server = 'auth-db.cny206g4cz8c.us-east-1.rds.amazonaws.com'
database = 'auth_db'
username = 'admin'
password = 'Distribuida123'
connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"

def get_connection():
    return pyodbc.connect(connection_string)

class FriendRequest(BaseModel):
    user_email: str
    friend_email: str

@app.post("/add-friend")
def add_friend(data: FriendRequest):
    conn = get_connection()
    cursor = conn.cursor()

    # Verifica que ambos usuarios existan
    cursor.execute("SELECT id FROM users WHERE email = ?", data.user_email)
    user = cursor.fetchone()
    cursor.execute("SELECT id FROM users WHERE email = ?", data.friend_email)
    friend = cursor.fetchone()

    if not user or not friend:
        raise HTTPException(status_code=404, detail="Uno o ambos usuarios no existen")

    cursor.execute("INSERT INTO friends (user_id, friend_id) VALUES (?, ?)", user.id, friend.id)
    conn.commit()
    return {"message": "Amigo agregado correctamente"}

@app.get("/friends/{email}")
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
