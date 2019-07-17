import pprint

import pymongo
from bson import ObjectId
from pymongo import MongoClient

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'testdb'
COLLECTION_TEST = 'collection_1'
COLLECTION_PROFILES = 'profiles'

test_data = {
    'title': 'My First MongoDB document',
    'author': 'Saransh Bansal',
    'likes': 100,
}

user_profiles = [{'user_id': 211, 'name': 'Luke'}, {'user_id': 212, 'name': 'Ziltoid'}]


class MongoUtil():
    db = None

    def __init__(self):
        client = MongoClient(MONGODB_HOST, MONGODB_PORT)
        self.db = client.DB_NAME

    def connect_to_mongo(self):
        return self.db

    def print_collection(self, coll_name):
        mycol = self.db[coll_name]
        print(mycol)

    def insert_document(self, coll_name, document=None):
        mycol = self.db[coll_name]
        mycol.insert_one(document)

    def update_document(self, coll_name, obj_id):
        mycol = self.db[coll_name]
        mycol.update_one({'_id': ObjectId(obj_id)}, {"$set": {"title": "abc"}})

    def print_all(self, coll_name):
        results = self.db[coll_name].find()
        for node in results:
            pprint.pprint(node)

    def count_documents(self, coll_name):
        mycol = self.db[coll_name]
        count = mycol.count_documents({})
        print(count)

    def create_profiles(self, coll_name):
        self.db[coll_name].insert_many(user_profiles)

    def create_index(self, coll_name, index_col):
        self.db[coll_name].create_index([(index_col, pymongo.ASCENDING)],
                                        unique=True)
        print(sorted(list(self.db[coll_name].index_information())))


instance = MongoUtil()

instance.print_collection(COLLECTION_TEST)

# instance.insert_document(COLLECTION_TEST, test_data)

# instance.create_profiles(COLLECTION_PROFILES)

instance.print_all(COLLECTION_TEST)

print('\n')

instance.print_all(COLLECTION_PROFILES)

print('\n')

instance.count_documents(COLLECTION_TEST)

# instance.update_document(COLLECTION_TEST, '5d2c87e03c30f6680050c521')

instance.create_index(COLLECTION_PROFILES, 'user_id')
