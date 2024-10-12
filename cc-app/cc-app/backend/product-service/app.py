# product-service/app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

products = {}

@app.route('/products', methods=['POST'])
def create_product():
    product_data = request.get_json()
    product_id = product_data['id']
    products[product_id] = product_data
    return jsonify(product_data), 201
    
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(list(products.values())), 200

@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(product)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

