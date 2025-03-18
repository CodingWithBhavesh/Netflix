from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

users = []  # Store user data

@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400
    
    # Check if user already exists
    if any(user["username"] == username for user in users):
        return jsonify({"message": "Username already exists"}), 400
    
    users.append({"username": username, "password": password})
    return jsonify({"message": "User registered successfully!"})

@app.route("/get_users", methods=["GET"])
def get_users():
    return jsonify({"users": users})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get port from environment for deployment
    app.run(host="0.0.0.0", port=port)
