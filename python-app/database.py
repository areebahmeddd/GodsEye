import firebase_admin
from firebase_admin import credentials, firestore

credential = credentials.Certificate('firebase-key.json')
firebase_admin.initialize_app(credential)
database = firestore.client()

news_reference = database.collection('news')

def database_history(document_name, data):
    try:
        news_document = news_reference.document(document_name)
        news_data = news_document.get().to_dict()

        if news_data == data:
            print(f'[Database] News data for "{document_name}" already exists.')
            return

        news_document.set({
            'news_data': data
        }, merge=True)
        print(f'[Database] News data for "{document_name}" stored.')
    except Exception as exc:
        print(f'Firestore storage error:\n {exc}')
