import pytest
from storage.firestore_db import FirestoreDB

def test_save_video_metadata():
    firestore_db = FirestoreDB(credentials_file='serviceAccountKey.json')
    video_data = {"id": "1", "title": "Sample Video", "description": "Test video description"}
    firestore_db.save_video_metadata(video_data)
    assert True
