from flask import Flask, jsonify

app = Flask(__name__)

tasks = [{
    "id": "task1",
    "content": "Sample task 1"
},{
    "id": "task2",
    "content": "Sample task 2"
}]

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200

@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)