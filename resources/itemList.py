from flask_restful import Resource

from theCode.models.itemModel import ItemModel


class ItemList(Resource):
    def get(self):
        return {'items': [x.json() for x in ItemModel.query.all()]}
