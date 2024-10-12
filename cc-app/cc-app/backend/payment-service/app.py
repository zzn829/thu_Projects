# payment-service/app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

payments = {}

@app.route('/payments', methods=['POST'])
def create_payment():
    payment_data = request.get_json()
    payment_id = payment_data['id']
    payments[payment_id] = payment_data
    return jsonify(payment_data), 201
    
@app.route('/payments', methods=['GET'])
def get_payments():
    return jsonify(list(payments.values())), 200

@app.route('/payments/<payment_id>', methods=['GET'])
def get_payment(payment_id):
    payment = payments.get(payment_id)
    if not payment:
        return jsonify({'error': 'Payment not found'}), 404
    return jsonify(payment)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)

