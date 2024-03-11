from pymongo import MongoClient


def _get_db_handle():
    client = MongoClient(
        host='127.0.0.1',
        port=int(27017),
        username='root',
        password='root'
    )
    db_handle = client['fceadb']
    return db_handle


def _get_collection_handle(collection):
    db_handle = _get_db_handle()
    return _set_collection(db_handle, collection)


def _set_collection(db_handle, collection):
    return db_handle[collection]


def get_collection(collection, filter):
    collection_handle = _get_collection_handle(collection)
    return list(collection_handle.find(filter))


def insert_document(collection, data, filter):
    collection_handle = _get_collection_handle(collection)
    if collection_handle.find_one(filter):
        pass
    else:
        collection_handle.insert_one(data)


def update_value(collection, filter, update):
    collection_handle = _get_collection_handle(collection)
    collection_handle.update_one(filter, {'$set': update})
    return collection_handle.find_one(filter)
