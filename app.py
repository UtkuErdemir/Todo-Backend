from flask import Flask, request, jsonify
import json

app = Flask(__name__)

todos = []


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
    todos.append({"id": len(todos),
                  "todo_name": todo_name})
    return jsonify(success=True,
                   message="Todo "+todo_name+" named is saved.",
                   statusCode=200)


if __name__ == '__main__':
    app.run()
