#!/usr/bin/env python3
"""
Basic Flask App
"""
from flask import Flask, render_template, jsonify, request
from user import User
from auth import Auth

app = Flask(__name__)
message = {"message": "Bienvenue"}
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """Root path"""
    return jsonify(message)


@app.route("/users", methods=["POST"], strict_slashes=False)
def register_user() -> str:
    """Register a new user."""
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = AUTH.register_user(email, password)
        message = {"email": user.email, "message": "User registered"}
        return jsonify(message), 201
    except ValueError:
        return jsonify({"message": "Email already registered"}), 400
    

@app.route('/sessions', methods=['POST'])
def login() -> str:
    """_summary_

    Returns:
        str: _description_
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not (AUTH.valid_login(email, password)):
        abort(401)
    else:
        # create a new session
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', session_id)

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
