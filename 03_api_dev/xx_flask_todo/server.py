from flask import Flask, request, jsonify
from pydantic import ValidationError
from models import TODOCreate, TODOUpdate
from domain import TodoDomain

app = Flask(__name__)

@app.route('/create', methods=['POST'])
def create_todo():
    try:
        # Parse the JSON data into a Pydantic model
        todoCreate: TODOCreate = TODOCreate.parse_raw(request.body)
        
        domain : TodoDomain = TodoDomain()
        res:TODOUpdate = domain.create_todo(todo=todoCreate)
        return res.dict()
    except ValidationError as e:
        # If the JSON data doesn't match the Pydantic model, return a 400 Bad Request response
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/update', methods=['POST'])
def update_todo():
    try:
        # Parse the JSON data into a Pydantic model
        todoUpdate: TODOCreate = TODOUpdate.parse_raw(request.body)
        
        domain : TodoDomain = TodoDomain()
        res:TODOUpdate = domain.create_todo(todo=todoCreate)
        return res.dict()
    except ValidationError as e:
        # If the JSON data doesn't match the Pydantic model, return a 400 Bad Request response
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400





