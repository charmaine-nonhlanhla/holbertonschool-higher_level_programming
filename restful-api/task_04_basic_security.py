from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'  # Change this to a secure secret key
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Sample user data
users = {
    "user1": {"username": "user1", "password": "password", "role": "user"},
    "admin1": {"username": "admin1", "password": "adminpassword", "role": "admin"}
}

# Basic authentication
@auth.verify_password
def verify_password(username, password):
    if username in users and \
       users[username]["password"] == password:
        return username

# JWT token generation
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    if username in users and users[username]["password"] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

# Basic Auth protected route
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# JWT Token protected route
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# Admin only route
@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if users[current_user]["role"] == "admin":
        return "Admin Access: Granted"
    else:
        return jsonify({"error": "Admin access required"}), 403

if __name__ == "__main__":
    app.run()

