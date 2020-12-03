import os

from dotenv import load_dotenv

load_dotenv(verbose=True)
API_KEY = os.getenv('YOUTUBE_API_KEY')

DOWNLOADS_DIR = 'downloads'
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')
