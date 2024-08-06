from flask import Blueprint, request, jsonify
from app import db
from models import Product

product_blueprint = Blueprint('products', __name__)

@product_blueprint.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    products_list = [{'id': p.id, 'name': p.name, 'description': p.description, 'quantity': p.quantity} for p in products]
    return jsonify(products_list)

@product_blueprint.route('/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify({'id': product.id, 'name': product.name, 'description': product.description, 'quantity': product.quantity})

@product_blueprint.route('/', methods=['POST'])
def create_product():
    data = request.json
    new_product = Product(name=data['name'], description=data.get('description', ''), quantity=data['quantity'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully'}), 201

@product_blueprint.route('/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    product = Product.query.get_or_404(id)
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.quantity = data.get('quantity', product.quantity)
    db.session.commit()
    return jsonify({'message': 'Product updated successfully'}), 200

@product_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 200
