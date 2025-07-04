from flask import Blueprint
from app.controllers.name_controller import get_name

name_bp = Blueprint('name', __name__)
name_bp.route('/get-name', methods=['GET'])(get_name)
