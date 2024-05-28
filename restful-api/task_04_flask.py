from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"name": "John", "age": 30, "city": "New York"}
}

# Endpoint to welcome message
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Endpoint to return all usernames
@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))

# Endpoint to check API status
@app.route('/status')
def check_status():
    return "OK"

# Endpoint to get user data by username
@app.route('/users/<username>')
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return "User not found", 404

# Endpoint to add a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    username = data.get('username')
    if username in users:
        return "User already exists", 400
    else:
        users[username] = data
        return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run()

