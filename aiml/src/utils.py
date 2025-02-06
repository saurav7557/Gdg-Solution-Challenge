import logging
import os
from datetime import datetime
from typing import Any, Dict, List

def setup_logging() -> None:
    """Set up logging configuration."""
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL),
        format=log_format,
        handlers=[
            logging.FileHandler(LOG_FILE_PATH),
            logging.StreamHandler()
        ]
    )

def create_directory_if_not_exists(path: str) -> None:
    """Create directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def format_timestamp(timestamp: float) -> str:
    """Format timestamp to readable string."""
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def sanitize_filename(filename: str) -> str:
    """Sanitize filename by removing invalid characters."""
    return "".join(c for c in filename if c.isalnum() or c in (' ', '-', '_')).rstrip()

def chunk_list(lst: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split a list into chunks of specified size."""
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def format_video_metadata(video_data: Dict[str, Any]) -> Dict[str, Any]:
    """Format video metadata for storage."""
    return {
        'video_id': video_data.get('id', {}).get('videoId', ''),
        'title': video_data.get('snippet', {}).get('title', ''),
        'channel_id': video_data.get('snippet', {}).get('channelId', ''),
        'channel_title': video_data.get('snippet', {}).get('channelTitle', ''),
        'description': video_data.get('snippet', {}).get('description', ''),
        'published_at': video_data.get('snippet', {}).get('publishedAt', ''),
        'processed': False,
        'detection_results': [],
        'created_at': datetime.now().isoformat()
    }