import requests
from bs4 import BeautifulSoup
import pandas as pd

# Genius API key
GENIUS_API_KEY = "RsJ2W-nTlHhB0coz_JfP636kuTOJM2eUHvE-K3fs-mbPelASnGBLvFzo7SRDMs_x"

# CSV setup
OUTPUT_FILE = "lyrics_database.csv"

def setup_csv():
    """
    Create a CSV file with the appropriate headers if it doesn't already exist.
    """
    pd.DataFrame(columns=["song_title", "artist_name", "lyrics"]).to_csv(OUTPUT_FILE, index=False)
    print(f"Database '{OUTPUT_FILE}' has been cleared.")

def append_to_csv(song_title, artist_name, lyrics):
    """
    Append song data to the CSV file.
    """
    new_data = pd.DataFrame([{"song_title": song_title, "artist_name": artist_name, "lyrics": lyrics}])
    new_data.to_csv(OUTPUT_FILE, mode='a', header=False, index=False)
    print(f"'{song_title}' by '{artist_name}' successfully saved to database.")

def fetch_and_save_lyrics(song_title, artist_name):
    """
    Fetch the lyrics for a song and save to the database.

    Args:
        song_title (str): Title of the song.
        artist_name (str): Name of the artist.

    Returns:
        str: Success or error message.
    """
    base_url = "https://api.genius.com"
    search_url = f"{base_url}/search"
    headers = {"Authorization": f"Bearer {GENIUS_API_KEY}"}
    params = {"q": f"{song_title} {artist_name}"}

    try:
        response = requests.get(search_url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            hits = data.get("response", {}).get("hits", [])
            if hits:
                song_url = hits[0]["result"]["url"]
                lyrics_page = requests.get(song_url)
                if lyrics_page.status_code == 200:
                    soup = BeautifulSoup(lyrics_page.text, 'html.parser')
                    lyrics_divs = soup.find_all('div', {'data-lyrics-container': 'true'})
                    if lyrics_divs:
                        lyrics = "\n".join([div.get_text(separator="\n") for div in lyrics_divs])
                        append_to_csv(song_title, artist_name, lyrics)
                        return f"Lyrics for '{song_title}' successfully saved."
                return f"Lyrics not found for '{song_title}'."
            return f"No matching song found for '{song_title}' by '{artist_name}'."
        return f"Error with Genius API (Status Code: {response.status_code})."
    except Exception as e:
        return f"An error occurred: {e}"