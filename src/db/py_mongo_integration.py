import pprint

from bson import ObjectId
from pymongo import MongoClient

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'testdb'
COLLECTION_NAME = 'collection_1'


class MongoUtil():
    db = None

    def __init__(self):
        client = MongoClient(MONGODB_HOST, MONGODB_PORT)
        self.db = client.DB_NAME

    def connect_to_mongo(self):
        return self.db

    def print_collection(self, coll_name):
        col = self.db[coll_name]
        print(col)

    def insert_document(self, coll_name, document=None):
        mycol = self.db[coll_name]
        mycol.insert_one(document)

    def update_document(self, coll_name, obj_id):
        mycol = self.db[coll_name]
        mycol.update_one({'_id': ObjectId(obj_id)}, {"$set": {"title": "abc"}})

    def print_all_docs(self, coll_name):
        mycol = self.db[coll_name]
        for post in mycol.find():
            pprint.pprint(post)

    def count_documents(self, coll_name):
        mycol = self.db[coll_name]
        count = mycol.count_documents({})
        print(count)


instance = MongoUtil()
instance.print_collection(COLLECTION_NAME)
data = {
    'title': 'My First MongoDB document',
    'author': 'Saransh Bansal',
    'likes': 100,
}

# instance.insert_document(COLLECTION_NAME, data)

instance.print_all_docs(COLLECTION_NAME)

instance.count_documents(COLLECTION_NAME)

# instance.update_document(COLLECTION_NAME, '5d2c87e03c30f6680050c521')
