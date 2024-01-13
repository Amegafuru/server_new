from flask import Blueprint
from controllers.user_controller import UserController

user_controller = UserController()

routes_Bp = Blueprint('router', __name__)

@routes_Bp.route('/registration', methods=['POST'])
def registration():
    return user_controller.registration()

@routes_Bp.route('/login', methods=['POST'])
def login():
    return user_controller.login()

@routes_Bp.route('/logout', methods=['POST'])
def logout():
    return user_controller.logout()

@routes_Bp.route('/activate/<link>', methods=['GET'])
def activate(link):
    return user_controller.activate(link)

@routes_Bp.route('/refresh', methods=['GET'])
def refresh():
    return user_controller.refresh()

@routes_Bp.route('/users', methods=['GET'])
def get_users():
    return user_controller.get_users()
