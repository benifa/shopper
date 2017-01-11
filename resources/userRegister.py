from flask_restful import Resource
from flask_restful import reqparse

from theCode.models.usermodel import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This Field cannot be blank")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This Field cannot be empty")

    def post(self):
        data = UserRegister.parser.parse_args()
        name = data['username']
        if UserModel.find_by_username(name):
            return {"message": "A username with name '{}' already exists.".format(name)}, 400
        user = UserModel(**data)
        user.save_to_db()
        return {"message": "User created successfully."}, 201
