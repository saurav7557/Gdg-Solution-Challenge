import pytest
from api.youtube_scraper import YouTubeScraper

def test_search_videos():
    youtube_scraper = YouTubeScraper(api_key="YourAPIKeyHere")
    videos = youtube_scraper.search_videos("AI technology")
    assert len(videos) > 0
