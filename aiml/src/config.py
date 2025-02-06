import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# YouTube API Configuration
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
YOUTUBE_API_VERSION = os.getenv('YOUTUBE_API_VERSION', 'v3')
YOUTUBE_MAX_RESULTS = int(os.getenv('YOUTUBE_MAX_RESULTS', 50))

# Firebase Configuration
FIREBASE_CONFIG = {
    'project_id': os.getenv('FIREBASE_PROJECT_ID'),
    'private_key': os.getenv('FIREBASE_PRIVATE_KEY'),
    'client_email': os.getenv('FIREBASE_CLIENT_EMAIL'),
    'database_url': os.getenv('FIREBASE_DATABASE_URL')
}

# AI Model Configuration
MODEL_PATH = os.getenv('MODEL_PATH', 'data/models/yolo_weights.onnx')
CONFIDENCE_THRESHOLD = float(os.getenv('CONFIDENCE_THRESHOLD', 0.5))
NMS_THRESHOLD = float(os.getenv('NMS_THRESHOLD', 0.4))

# Video Processing Configuration
MAX_FRAMES_PER_VIDEO = int(os.getenv('MAX_FRAMES_PER_VIDEO', 100))
FRAME_EXTRACTION_INTERVAL = int(os.getenv('FRAME_EXTRACTION_INTERVAL', 30))
VIDEO_DOWNLOAD_PATH = os.getenv('VIDEO_DOWNLOAD_PATH', 'data/raw_videos/')
PROCESSED_VIDEO_PATH = os.getenv('PROCESSED_VIDEO_PATH', 'data/processed_videos/')

# Logging Configuration
DEBUG_MODE = os.getenv('DEBUG_MODE', 'True').lower() == 'true'
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE_PATH = os.getenv('LOG_FILE_PATH', 'data/logs/scraper.log')

# API Rate Limiting
MAX_REQUESTS_PER_MINUTE = int(os.getenv('MAX_REQUESTS_PER_MINUTE', 60))
REQUEST_TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', 30))

# Recognized Channel IDs
RECOGNIZED_CHANNEL_IDS = os.getenv('RECOGNIZED_CHANNEL_IDS', '').split(',')