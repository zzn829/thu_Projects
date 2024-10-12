# user-service/app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    user_id = user_data['id']
    users[user_id] = user_data
    return jsonify(user_data), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200
    
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

