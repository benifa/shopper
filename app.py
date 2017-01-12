import os

from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.item import Item
from resources.itemList import ItemList
from resources.store import Store
from resources.storeList import StoreList
from resources.userRegister import UserRegister
from security import authenticate, identify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "beni"
api = Api(app)

jwt = JWT(app, authenticate, identify)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    app.run(port=5001, debug=True)
