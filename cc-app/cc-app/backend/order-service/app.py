# order-service/app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

orders = {}

@app.route('/orders', methods=['POST'])
def create_order():
    order_data = request.get_json()
    order_id = order_data['id']
    orders[order_id] = order_data
    return jsonify(order_data), 201
    
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(list(orders.values())), 200

@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    order = orders.get(order_id)
    if not order:
        return jsonify({'error': 'Order not found'}), 404
    return jsonify(order)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

