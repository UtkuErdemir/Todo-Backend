from flask import Flask, request, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


todos = [{"id": 0, "todo_name": "Sample Todo"}]


@app.after_request
def apply_caching(response):
    response.headers["Content-Type"] = "application/json"
    return response


@app.route('/')
def hello_world():
    return 'Todo API - Developed by Utku Erdemir!'


@app.route('/todos', methods=['GET'])
def get_todos():
    result = {"success": True,
              "data":todos}
    return json.dumps(result, indent=4, sort_keys=True)


@app.route('/todos', methods=['POST'])
def save_todo():
    global todos
    todo_name = request.form.get('todo_name')
    if todo_name is None or todo_name == "":
        return jsonify(success=False,message="Todo name cannot be empty."), 400
    todo_id = len(todos)
    todos.append({"id": todo_id,
                  "todo_name": todo_name})
    return jsonify(success=True,
                   message="Todo "+todo_name+" named is saved.",
                   todo_id=todo_id), 201


if __name__ == '__main__':
    app.run()
