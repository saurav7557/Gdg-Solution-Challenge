from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import logging

logger = logging.getLogger(__name__)

class YouTubeScraper:
    def __init__(self, api_key: str):
        """Initialize YouTube API client."""
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def search_videos(self, query: str, max_results: int = 50):
        """Search for videos using YouTube Data API."""
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

    def _filter_unrecognized_channels(self, videos):
        """Filter out videos from recognized channels."""
        recognized_channel_ids = ["some_channel_id1", "some_channel_id2"]  # Example channel IDs
        return [
            video for video in videos
            if video.get('snippet', {}).get('channelId') not in recognized_channel_ids
        ]

    def get_video_details(self, video_id):
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

    def batch_get_video_details(self, video_ids):
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
