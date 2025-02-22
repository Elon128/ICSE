import requests
from bs4 import BeautifulSoup
import pandas as pd

def verify_lyrics(song_title, artist_name, song_url):
    """
    Verify if the lyrics URL corresponds to the correct song based on the song title.

    Args:
        song_title (str): The title of the song.
        artist_name (str): The name of the artist.
        song_url (str): The Genius URL for the song.

    Returns:
        bool: True if the lyrics correspond to the song, False otherwise.
    """
    try:
        # Fetch the lyrics page
        response = requests.get(song_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract the lyrics and page title
            lyrics_divs = soup.find_all('div', {'data-lyrics-container': 'true'})
            page_title = soup.find('title').get_text() if soup.find('title') else ""
            
            # Combine lyrics content and page title into one searchable text
            lyrics = "\n".join([div.get_text(separator="\n") for div in lyrics_divs]).lower() if lyrics_divs else ""
            content_to_check = (lyrics + " " + page_title).lower()

            # Break the song title into words and check if any word is in the content
            song_title_words = song_title.lower().split()
            for word in song_title_words:
                if word in content_to_check:
                    return True

            print(f"Lyrics mismatch for '{song_title}' by '{artist_name}'. URL: {song_url}")
            return False
        else:
            print(f"Error fetching page for URL {song_url} (Status Code: {response.status_code}).")
            return False
    except Exception as e:
        print(f"Error verifying lyrics for '{song_title}' by '{artist_name}': {e}")
        return False

def verify_urls_in_csv(input_file, output_file, mismatched_file):
    """
    Verify all URLs in the song list CSV based on the song title words and save mismatched songs.

    Args:
        input_file (str): Path to the input CSV file with songs and URLs.
        output_file (str): Path to save the verified songs.
        mismatched_file (str): Path to save the mismatched songs.
    """
    try:
        # Load the song list
        df = pd.read_csv(input_file)

        if "lyrics_url" not in df.columns:
            print(f"Error: The input file '{input_file}' does not contain a 'lyrics_url' column.")
            return

        verified_songs = []
        mismatched_songs = []

        # Verify each song
        for _, row in df.iterrows():
            song_title = row["song_title"]
            artist_name = row["artist_name"]
            song_url = row["lyrics_url"]

            print(f"Verifying: {song_title} by {artist_name}")
            if verify_lyrics(song_title, artist_name, song_url):
                verified_songs.append(row)
            else:
                mismatched_songs.append(row)

        # Save verified songs to a new CSV file
        pd.DataFrame(verified_songs).to_csv(output_file, index=False)
        print(f"Verified songs saved to '{output_file}'.")

        # Save mismatched songs to a new CSV file
        if mismatched_songs:
            mismatched_df = pd.DataFrame(mismatched_songs)
            mismatched_df.to_csv(mismatched_file, index=False)
            print(f"Mismatched songs saved to '{mismatched_file}'.")
        else:
            print("\nAll URLs verified successfully. No mismatched songs found.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_csv = "d1_with_urls.csv"       # Updated file with URLs
    output_csv = "verified_songs.csv"    # Verified song list file
    mismatched_file = "mismatched_songs.csv"  # Mismatched song list file

    verify_urls_in_csv(input_csv, output_csv, mismatched_file)