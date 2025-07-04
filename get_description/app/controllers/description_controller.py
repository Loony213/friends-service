from flask import request, jsonify
from app.services.description_service import fetch_description

def get_description():
    email = request.args.get('email')
    if not email:
        return jsonify({'error': 'Email requerido'}), 400

    result = fetch_description(email)
    if result:
        return jsonify({'description': result})
    return jsonify({'error': 'Usuario no encontrado'}), 404
