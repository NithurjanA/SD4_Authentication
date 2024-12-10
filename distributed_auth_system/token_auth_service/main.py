from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
secret_key = "supersecretkey"

def create_token():
    payload = {
        'iat': datetime.datetime.utcnow(),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

def validate_token(token):
    try:
        decoded = jwt.decode(token, secret_key, algorithms=['HS256'])
        return decoded
    except jwt.ExpiredSignatureError:
        return "Token expired"
    except jwt.InvalidTokenError:
        return "Invalid token"

@app.route('/generate-token', methods=['POST'])
def generate_token():
    token = create_token()
    return jsonify({"token": token})

@app.route('/validate-token', methods=['POST'])
def validate():
    data = request.get_json()
    token = data.get('token')
    if not token:
        return jsonify({"message": "Token is required"}), 400

    validation_result = validate_token(token)
    if isinstance(validation_result, dict):
        exp_date = datetime.datetime.utcfromtimestamp(validation_result['exp']).strftime('%Y-%m-%d %H:%M:%S')
        iat_date = datetime.datetime.utcfromtimestamp(validation_result['iat']).strftime('%Y-%m-%d %H:%M:%S')
        return jsonify({
            "message": "Token is valid",
            "decoded": {"iat": iat_date, "exp": exp_date}
        })
    else:
        return jsonify({"message": validation_result}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
