from flask import jsonify

class UserController:

    def registration(self):
        try:
            # Логика регистрации пользователя
            return jsonify({"message": "User registration successful"})
            
        except Exception as e:
            # Обработка ошибок
            return jsonify({"error": str(e)})

    def login(self):
        try:
            # Логика входа пользователя
            return jsonify({"message": "User logged in successfully"})
            
        except Exception as e:
            # Обработка ошибок
            return jsonify({"error": str(e)})

    def logout(self):
        try:
            # Логика выхода пользователя
            return jsonify({"message": "User logged out successfully"})
            
        except Exception as e:
            # Обработка ошибок
            return jsonify({"error": str(e)})
            
    def activate(self, link):
        try:
            # Логика активации пользователя
            return jsonify({"message": f"User with link '{link}' has been activated."})
            
        except Exception as e:
            # Обработка ошибок
            return jsonify({"error": str(e)})

    def refresh(self):
        try:
            # Возвращаем данные в формате JSON
            return jsonify({"message": "Refresh Token successfully"})
            
        except Exception as e:
            # Обработка ошибок
            return jsonify({"error": str(e)})
        
    def get_users(self):
        try:
            users = {'123': '456', '789': '012'}  # Пример данных пользователей
            # Возвращаем данные в формате JSON
            return jsonify(users)
            
        except Exception as e:
            # Обработка ошибок
            return jsonify({"error": str(e)})
