from flask import Flask

app = Flask(__name__)

list_tasks = ["Sample task 1", "Sample task 2"]

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return list_tasks

@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run()