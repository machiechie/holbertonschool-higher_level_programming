from flask import Flask, jsonify, request

app = Flask(__name__)

# Словарь пользователей в памяти
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Главная страница
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Список всех username
@app.route("/data")
def data():
    return jsonify(list(users.keys()))

# Статус API
@app.route("/status")
def status():
    return "OK"

# Информация о конкретном пользователе
@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404

# Добавление нового пользователя
@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        data = request.get_json()
    except:
        return jsonify({"error": "Invalid JSON"}), 400

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

# Запуск сервера
if __name__ == "__main__":
    app.run()
