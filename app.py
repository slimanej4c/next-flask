from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from database import db


app = Flask(__name__, static_folder='static/build')
# Configuration de la base de données
basedir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(basedir, 'instance', 'database.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation de SQLAlchemy
db.init_app(app)
CORS(app, origins=['http://localhost:3000'])

# Vérifier si la base de données existe, sinon la créer
if not os.path.exists(database_path):
    if not os.path.exists(os.path.join(basedir, 'instance')):
        os.makedirs(os.path.join(basedir, 'instance'))
    with app.app_context():
        db.create_all()
        print("Base de données créée.")

# Importation des blueprints et enregistrement
from routes.auth_routes import auth_blueprint
app.register_blueprint(auth_blueprint)

# Route pour servir les fichiers statiques
@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

@app.route('/', methods=['GET'])
def index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
