from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

# Flask-App erstellen
app = Flask(__name__)

# Simulierte Benutzerdatenbank
users_db = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    if username in users_db:
        return jsonify({"message": "Username already exists"}), 400

    hashed_password = generate_password_hash(password)
    users_db[username] = hashed_password

    return jsonify({"message": "User registered successfully"}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    if username not in users_db:
        return jsonify({"message": "Invalid username or password"}), 400

    if not check_password_hash(users_db[username], password):
        return jsonify({"message": "Invalid username or password"}), 400

    return jsonify({"message": "Login successful"}), 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
