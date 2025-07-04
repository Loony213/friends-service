from flask import request, jsonify
from app.services.name_service import fetch_name

def get_name():
    email = request.args.get('email')
    if not email:
        return jsonify({'error': 'Email requerido'}), 400

    result = fetch_name(email)
    if result:
        return jsonify({'name': result})
    return jsonify({'error': 'Usuario no encontrado'}), 404
