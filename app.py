from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = []  # Store user data in a list

@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    users.append({"username": username, "password": password})
    print("All Registered Users:", users)  # Print users in the terminal

    return jsonify({"message": "User registered successfully!"})

@app.route("/get_users", methods=["GET"])
def get_users():
    return jsonify({"users": users})  # Returns all stored users

if __name__ == "__main__":
    app.run(debug=True)
