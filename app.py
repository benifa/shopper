
from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from theCode.resources.item import Item
from theCode.resources.itemList import ItemList
from theCode.resources.store import Store
from theCode.resources.storeList import StoreList
from theCode.resources.userRegister import UserRegister
from theCode.security import authenticate, identify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
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
    from theCode.db import db
    db.init_app(app)
    app.run(port=5001, debug=True)
