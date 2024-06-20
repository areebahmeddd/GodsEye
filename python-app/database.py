import firebase_admin
from firebase_admin import credentials, firestore

credential = credentials.Certificate('firebase-key.json')
firebase_admin.initialize_app(credential)
database = firestore.client()