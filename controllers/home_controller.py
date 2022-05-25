from flask import request

from controllers import mech_controller
from exceptions.resource_not_found import ResourceNotFound
from Class.User import User
from Repo.User_repo import UserRepo
from services.User_service import UserServices

ur = UserRepo()
us = UserServices(ur)

user = us.get_user(1)


def route(app):

    @app.route('/login', methods=['POST'])
    def login():
        try:
            body = request.json
            global user
            user = us.login(body['username'], body['password'])
            print(user)
            return {
                'message': 'Successfully Logged In'
                   }, 200
        except ResourceNotFound as e:
            return 'Invalid Login', 401

    @app.route('/current_user', methods=['GET'])
    def current_user():
        if user.u_id != 0:
            return user.json(), 200
        else:
            return {'message': 'No User Logged In'}, 400
