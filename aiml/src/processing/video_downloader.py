import pytube
import logging

class VideoDownloader:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.downloaded_videos = []

    def download_video(self, video_url):
        try:
            yt = pytube.YouTube(video_url)
            video = yt.streams.get_highest_resolution()
            video.download(output_path='data/raw_videos/')
            self.downloaded_videos.append(yt.title)
            self.logger.info(f"Downloaded video: {yt.title}")
        except Exception as e:
            self.logger.error(f"Error downloading video: {e}")
