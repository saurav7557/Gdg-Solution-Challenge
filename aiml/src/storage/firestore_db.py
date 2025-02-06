from firebase_admin import credentials, firestore, initialize_app

class FirestoreDB:
    def __init__(self, credentials_file='serviceAccountKey.json'):
        cred = credentials.Certificate(credentials_file)
        initialize_app(cred)
        self.db = firestore.client()

    def save_video_metadata(self, video):
        doc_ref = self.db.collection('videos').document(video['id'])
        doc_ref.set(video)
