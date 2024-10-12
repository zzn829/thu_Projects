# frontend/app.py
from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# 後端服務的URL
BACKEND_URLS = {
    'user-service': 'http://user-service:5000',
    'product-service': 'http://product-service:5001',
    'order-service': 'http://order-service:5002',
    'payment-service': 'http://payment-service:5003'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        user_data = {
            'id': request.form['id'],
            'name': request.form['name']
        }
        requests.post(f"{BACKEND_URLS['user-service']}/users", json=user_data)
        return redirect(url_for('users'))
    users = requests.get(f"{BACKEND_URLS['user-service']}/users").json()
    return render_template('users.html', users=users)

@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        product_data = {
            'id': request.form['id'],
            'name': request.form['name']
        }
        requests.post(f"{BACKEND_URLS['product-service']}/products", json=product_data)
        return redirect(url_for('products'))
    products = requests.get(f"{BACKEND_URLS['product-service']}/products").json()
    return render_template('products.html', products=products)

@app.route('/orders', methods=['GET', 'POST'])
def orders():
    if request.method == 'POST':
        order_data = {
            'id': request.form['id'],
            'product_id': request.form['product_id'],
            'quantity': request.form['quantity']
        }
        requests.post(f"{BACKEND_URLS['order-service']}/orders", json=order_data)
        return redirect(url_for('orders'))
    orders = requests.get(f"{BACKEND_URLS['order-service']}/orders").json()
    return render_template('orders.html', orders=orders)

@app.route('/payments', methods=['GET', 'POST'])
def payments():
    if request.method == 'POST':
        payment_data = {
            'id': request.form['id'],
            'order_id': request.form['order_id'],
            'amount': request.form['amount']
        }
        requests.post(f"{BACKEND_URLS['payment-service']}/payments", json=payment_data)
        return redirect(url_for('payments'))
    payments = requests.get(f"{BACKEND_URLS['payment-service']}/payments").json()
    return render_template('payments.html', payments=payments)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

