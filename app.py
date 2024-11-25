from flask import Flask, request, jsonify

app = Flask(__name__)

users = {"admin": "password123"}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        return jsonify({"message": "Login is successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
