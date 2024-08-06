from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User  # Importer les modèles depuis models.py

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Vérifier si l'utilisateur existe déjà
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'message': 'User already exists'}), 400
    
    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201
