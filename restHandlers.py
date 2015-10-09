from bson import ObjectId
from bson.json_util import dumps,loads


class MongoCrud:

    def __init__(self, collection):
        self.collection = collection

    # Returns the ObjectId of the newly created object
    def create(self, data):
        obj = loads(data)
        item = self.collection.insert(obj)
        return self.read(str(item))

    def update(self, item_id, update_data):
        update_obj = loads(update_data)
        self.collection.update({'_id': ObjectId(item_id)}, update_obj)
        return self.read(ObjectId(item_id))

    def delete(self, item_id):
        retval = self.collection.remove({'_id': ObjectId(item_id)})
        return dumps(retval)

    def drop(self):
        self.collection.drop()
        return dumps([])

    def read(self, item_id):
        if not item_id:
            # Return the entire list?
            rec = self.collection.find()
            return dumps(rec)
        else:
            rec = self.collection.find({'_id': ObjectId(item_id)})
            if rec:
                return dumps(rec)
            else:
                return "{}"
