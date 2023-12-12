from flask import Flask, request, jsonify
from pydantic import ValidationError
from models import User

app = Flask(__name__)

@app.route("/")
def hello_world():
    my_user = User(name="Zia Khan", account_id=55)
    return my_user.dict()


# Define a Flask route that accepts a POST request with JSON data
@app.route('/users', methods=['POST'])
def create_user():
    try:
        # Parse the JSON data into a Pydantic model
        user = User.parse_raw(request.data)

        # Save the user to the database, etc.

        # Return a JSON response with the user data
        return user.dict()

    except ValidationError as e:
        # If the JSON data doesn't match the Pydantic model, return a 400 Bad Request response
        return jsonify({'error': str(e)}), 400


