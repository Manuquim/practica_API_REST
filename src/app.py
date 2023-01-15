from flask import Flask

# add the jsonify method to your Flask import
from flask import jsonify

from flask import request

# Para decodificar cualquier string json y convertirlo a un objeto de python podemos usar esta función
from flask import json

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def hello_world():
    # you can convert any variable into a json string like this
    json_text = jsonify(todos)
    # and then you can return it to the front end in the response body like this
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    decoded_object = json.loads(request.data)
    todos.append(decoded_object)
    print("Incoming request with the following body", request.data)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position)
    return jsonify(todos)

# Estas dos líneas siempre seben estar al final de tu archivo app.py.

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)