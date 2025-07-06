from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.friends_api import router as friends_router

app = FastAPI()

# Agregar middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes de cualquier origen (modificar si es necesario)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Configuración de rutas
app.include_router(friends_router)
