import os
import csv
from api.youtube_scraper import YouTubeScraper
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def read_characters_from_csv(file_path):
    """
    Reads a CSV file containing character names and returns a list of characters.
    """
    characters = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                if row:  # Skip any empty rows
                    characters.append(row[0])  # Assuming characters are in the first column
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"Error reading the file: {e}")
    return characters

def search_and_display_videos(youtube_scraper, character):
    """
    Searches YouTube for videos related to a given character and displays the video details.
    """
    print(f"\nSearching videos for character: {character}")
    try:
        videos = youtube_scraper.search_videos(character)

        if not videos:
            print(f"No videos found for character: {character}")
        else:
            for video in videos:
                print(f"\nTitle: {video['snippet']['title']}")
                print(f"Description: {video['snippet']['description']}")
                print(f"Channel: {video['snippet']['channelTitle']}")
                print(f"Video ID: {video['id']['videoId']}")
                print(f"Published At: {video['snippet']['publishedAt']}")
                print(f"Video URL: https://www.youtube.com/watch?v={video['id']['videoId']}")
                print("=" * 50)
    except Exception as e:
        print(f"Error searching for videos: {e}")

def main():
    """
    Main function that initializes the YouTubeScraper, reads Disney characters from a CSV,
    and searches for videos related to each character.
    """
    # Fetch YouTube API key from environment variables
    api_key = os.getenv('YOUTUBE_API_KEY')

    if not api_key:
        raise ValueError("YouTube API key is missing in the environment variables.")
    
    # Initialize YouTubeScraper with API key
    youtube_scraper = YouTubeScraper(api_key=api_key)

    # Read characters from CSV
    characters = read_characters_from_csv("disney_characters.csv")

    # If no characters were found, exit early
    if not characters:
        print("No characters found in the CSV file.")
        return

    # Search for videos related to each character and display results
    for character in characters:
        search_and_display_videos(youtube_scraper, character)

if __name__ == '__main__':
    main()
