from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TOKEN_AUTH_URL = "http://token_auth_service:5001"
PASSWORD_AUTH_URL = "http://password_auth_service:5000"

@app.route('/secure-data', methods=['POST'])
def secure_data():
    token = request.json.get('token')
    response = requests.post(f"{TOKEN_AUTH_URL}/validate-token", json={"token": token})
    if response.status_code == 200:
        return jsonify({"data": "Secure data with Token Auth"})
    return jsonify({"message": "Invalid token"}), 401

@app.route('/profile', methods=['POST'])
def profile():
    username = request.json.get('username')
    password = request.json.get('password')
    response = requests.post(f"{PASSWORD_AUTH_URL}/login", json={"username": username, "password": password})
    if response.status_code == 200:
        return jsonify({"profile": f"Welcome {username}"})
    return jsonify({"message": "Invalid credentials"}), 401


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
