from flask import Flask
from flask_cors import CORS
from app.routes.description_routes import description_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(description_bp)
    return app
