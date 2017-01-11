from flask_restful import Resource

from theCode.models.store import StoreModel


class StoreList(Resource):
    def get(self):
        return {'stores': [x.json() for x in StoreModel.query.all()]}
