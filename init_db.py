from app import app, db
from models import User, Product

# Crée un contexte d'application et initialise la base de données
with app.app_context():
    db.create_all()
    print("Toutes les tables ont été créées.")
