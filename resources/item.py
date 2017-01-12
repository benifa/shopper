from flask_jwt import jwt_required
from flask_restful import Resource

from models.itemModel import ItemModel


class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": "An item with name '{}' already exists.".format(name)}, 400

        data = ItemModel.getparser().parse_args()

        item = ItemModel(name, data["price"], data['store_id'])
        try:
            item.insert()
        except:
            return {"message": "An error occured inserting the item."}, 500

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"message": 'Item deleted'}

    def put(self, name):
        data = ItemModel.getparser().parse_args()

        item = ItemModel.find_by_name(name)
        update_item = ItemModel(name, data["price"], data['store_id'])

        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']
        item.insert()
        return update_item.json()
