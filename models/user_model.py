from mongoengine import Document, StringField, BooleanField

class UserModel(Document):
    email = StringField(unique=True, required=True)
    password = StringField(required=True)
    isActivated = BooleanField(default=False)
    activationLink = StringField()

    meta = {'collection': 'users'}  # Указываем название коллекции, если нужно отличное от имени класса
