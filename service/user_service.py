from models.user_model import UserModel
import asyncio
import bcrypt

class UserService:
    async def registration(self, email, password):
        try:
            # Логика регистрации пользователя
            candidate = UserModel.find_one({"email": email})
            if candidate:
                raise Error(f"Пользователь c почтовым адресом {email} уже существует")
            
            hash_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        
            user = UserModel.create(email=email, password=hash_password)
            return ()
            
        except Exception as e:
            # Обработка ошибок
            return ()