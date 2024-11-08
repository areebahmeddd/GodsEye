from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
database = client['news_database']
news_collection = database['news']

def database_history(document_name, data):
    try:
        news_document = news_collection.find_one({'_id': document_name})
        if news_document and news_document.get('news_data') == data:
            print(f'[Database] News data for "{document_name}" already exists.')
            return

        news_collection.update_one(
            {'_id': document_name},
            {'$set': {'news_data': data}},
            upsert=True
        )

        print(f'[Database] News data for "{document_name}" stored.')
    except Exception as exc:
        print(f'MongoDB storage error:\n {exc}')
