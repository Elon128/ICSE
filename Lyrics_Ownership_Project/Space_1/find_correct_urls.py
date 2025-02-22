import requests
import pandas as pd

# Genius API key
GENIUS_API_KEY = "RsJ2W-nTlHhB0coz_JfP636kuTOJM2eUHvE-K3fs-mbPelASnGBLvFzo7SRDMs_x"

def fetch_correct_url(song_title, artist_name):
    """
    Search Genius for the correct URL of a given song.

    Args:
        song_title (str): The title of the song.
        artist_name (str): The name of the artist.

    Returns:
        str: The Genius URL for the song, or None if not found.
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
                # Return the first matching URL
                return hits[0]["result"]["url"]
            else:
                print(f"No matching URL found for '{song_title}' by '{artist_name}'.")
                return None
        else:
            print(f"Error fetching URL for '{song_title}' by '{artist_name}' (Status Code: {response.status_code}).")
            return None
    except Exception as e:
        print(f"An error occurred while fetching URL for '{song_title}' by '{artist_name}': {e}")
        return None

def update_mismatched_urls(mismatched_file, output_file):
    """
    Search for correct URLs for mismatched songs and update their entries.

    Args:
        mismatched_file (str): Path to the CSV file containing mismatched songs.
        output_file (str): Path to save the updated CSV file with correct URLs.
    """
    try:
        # Load the mismatched songs
        df = pd.read_csv(mismatched_file)

        if "lyrics_url" not in df.columns:
            print(f"Error: The file '{mismatched_file}' does not contain a 'lyrics_url' column.")
            return

        # Update URLs for mismatched songs
        for index, row in df.iterrows():
            song_title = row["song_title"]
            artist_name = row["artist_name"]
            print(f"Searching for correct URL for: {song_title} by {artist_name}")
            new_url = fetch_correct_url(song_title, artist_name)
            if new_url:
                df.at[index, "lyrics_url"] = new_url
                print(f"Updated URL for '{song_title}': {new_url}")
            else:
                print(f"Could not find a valid URL for '{song_title}' by '{artist_name}'.")

        # Save the updated DataFrame
        df.to_csv(output_file, index=False)
        print(f"Updated mismatched songs saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{mismatched_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    mismatched_file = "mismatched_songs.csv"  # File with mismatched songs
    output_file = "corrected_songs.csv"       # File to save updated songs with correct URLs

    update_mismatched_urls(mismatched_file, output_file)