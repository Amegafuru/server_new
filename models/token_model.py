from mongoengine import Document, StringField, ReferenceField

class Token(Document):
    user = ReferenceField('users') # Используется для связи с другими документами.
    refreshToken = StringField(required=True) 

    meta = {'collection': 'tokens'}  # Указываем название коллекции, если нужно отличное от имени класса
