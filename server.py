from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from router.routes import routes_Bp

load_dotenv()

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=os.getenv('CLIENT_URL'))
PORT = int(os.getenv('PORT', 5000))

# Регистрация Blueprint
app.register_blueprint(routes_Bp, url_prefix='/api')

# Создание объекта MongoClient
client = MongoClient(os.getenv('DB_URL'))

# Функция для проверки доступности сервера MongoDB
def check_mongo_server():
    try:
        ping_result = client.admin.command('ping')
        print("Успешный пинг сервера:", ping_result)
        return True
    except Exception as e:
        print("Сервер недоступен:", e)
        return False

# Функция для проверки подключения к базе данных
def check_db_connection():
    try:
        # Получение списка доступных баз данных
        database_names = client.list_database_names()
        # Вывод списка баз данных
        print("Список баз данных:", database_names)

        db = client['mydatabase']  # Замените 'your_database_name' на имя вашей базы данных
        collection = db['users']  # Замените 'your_collection_name' на имя вашей коллекции
        document = collection.find_one()
        if document:
            print("Подключение к базе данных успешно. Имя базы данных:", db.name)
            print("Подключение к коллекции успешно. Имя коллекции:", collection.name)
            return True
        else:
            print("Ошибка: Неверное имя коллекции или базы данных")
            return False
    except Exception as e:
        print("Ошибка при подключении к базе данных:", e)
        return False
    
# Функция для запуска приложения
def start():
    try:
        if check_mongo_server() and check_db_connection():
            print("Подключение к MongoDB и коллекции установлено")
            print(f"Сервер запущен на порте: {PORT}")
            app.run(debug=True, port=PORT) #!!! Удалить во время публикации debug=True
        else:
            print("Невозможно запустить сервер.")
    except Exception as e:
        print("Ошибка при запуске сервера:", e)
if __name__ == '__main__':
    start()
