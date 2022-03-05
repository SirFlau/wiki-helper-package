import firebase_admin
from firebase_admin import credentials, firestore
import pathlib


def get_db_connection():
    if not firebase_admin._apps:
        cred = credentials.Certificate(f"{pathlib.Path(__file__).parent.resolve()}/firebase_credentials.json")
        firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db
