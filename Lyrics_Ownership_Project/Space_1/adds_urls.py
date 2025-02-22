import requests
import pandas as pd

# Genius API key
GENIUS_API_KEY = "RsJ2W-nTlHhB0coz_JfP636kuTOJM2eUHvE-K3fs-mbPelASnGBLvFzo7SRDMs_x"

def fetch_song_url(song_title, artist_name):
    """
    Fetch the Genius URL for the given song.

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
                return hits[0]["result"]["url"]
            else:
                print(f"No matching song found for '{song_title}' by '{artist_name}'.")
                return None
        else:
            print(f"Error fetching URL for '{song_title}' by '{artist_name}' (Status Code: {response.status_code}).")
            return None
    except Exception as e:
        print(f"An error occurred while fetching URL for '{song_title}' by '{artist_name}': {e}")
        return None

def add_urls_to_csv(input_file, output_file):
    """
    Add Genius lyrics URLs to the song list CSV.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the updated CSV file.
    """
    try:
        # Load the song list
        df = pd.read_csv(input_file)

        # Add a column for lyrics URLs
        df["lyrics_url"] = ""

        for index, row in df.iterrows():
            song_title = row["song_title"]
            artist_name = row["artist_name"]
            print(f"Fetching URL for: {song_title} by {artist_name}")
            url = fetch_song_url(song_title, artist_name)
            df.at[index, "lyrics_url"] = url

        # Save the updated DataFrame to a new file
        df.to_csv(output_file, index=False)
        print(f"Updated song list with URLs saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_csv = "d1.csv"  # Path to your original song list
    output_csv = "d1_with_urls.csv"  # Path to save the updated song list
    add_urls_to_csv(input_csv, output_csv)