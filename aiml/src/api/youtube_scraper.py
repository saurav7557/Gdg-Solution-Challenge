from typing import List, Dict, Any
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import logging
from ..config import (
    YOUTUBE_API_KEY,
    YOUTUBE_API_VERSION,
    YOUTUBE_MAX_RESULTS,
    RECOGNIZED_CHANNEL_IDS
)

logger = logging.getLogger(__name__)

class YouTubeScraper:
    def __init__(self):
        """Initialize YouTube API client."""
        self.youtube = build('youtube', YOUTUBE_API_VERSION, developerKey=YOUTUBE_API_KEY)

    def search_videos(self, query: str, max_results: int = YOUTUBE_MAX_RESULTS) -> List[Dict[str, Any]]:
        """
        Search for videos using YouTube Data API.
        
        Args:
            query: Search query string
            max_results: Maximum number of results to return
            
        Returns:
            List of video data dictionaries
        """
        try:
            search_response = self.youtube.search().list(
                q=query,
                part='snippet',
                maxResults=max_results,
                type='video'
            ).execute()

            videos = search_response.get('items', [])
            return self._filter_unrecognized_channels(videos)

        except HttpError as e:
            logger.error(f"Error searching YouTube videos: {str(e)}")
            return []

    def _filter_unrecognized_channels(self, videos: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Filter out videos from recognized channels."""
        return [
            video for video in videos
            if video.get('snippet', {}).get('channelId') not in RECOGNIZED_CHANNEL_IDS
        ]

    def get_video_details(self, video_id: str) -> Dict[str, Any]:
        """Get detailed information about a specific video."""
        try:
            video_response = self.youtube.videos().list(
                part='snippet,contentDetails,statistics',
                id=video_id
            ).execute()

            if video_response.get('items'):
                return video_response['items'][0]
            return {}

        except HttpError as e:
            logger.error(f"Error getting video details: {str(e)}")
            return {}

    def batch_get_video_details(self, video_ids: List[str]) -> List[Dict[str, Any]]:
        """Get details for multiple videos in batch."""
        try:
            video_response = self.youtube.videos().list(
                part='snippet,contentDetails,statistics',
                id=','.join(video_ids)
            ).execute()

            return video_response.get('items', [])

        except HttpError as e:
            logger.error(f"Error getting batch video details: {str(e)}")
            return []