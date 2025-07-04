from flask import Blueprint
from app.controllers.description_controller import get_description

description_bp = Blueprint('description', __name__)

description_bp.route('/get-description', methods=['GET'])(get_description)
