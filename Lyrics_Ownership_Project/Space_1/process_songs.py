import pandas as pd
from fetch_lyrics import setup_csv, fetch_and_save_lyrics

def process_songs(song_list_file):
    """
    Process each song in the song list, fetch lyrics, and count failures.
    """
    setup_csv()  # Clear the database at the start
    not_found_count = 0  # Counter for songs with missing lyrics

    try:
        song_list = pd.read_csv(song_list_file)
    except FileNotFoundError:
        print(f"Error: File '{song_list_file}' not found.")
        return

    for _, row in song_list.iterrows():
        song_title = row["song_title"]
        artist_name = row["artist_name"]
        print(f"Processing: {song_title} by {artist_name}")
        result = fetch_and_save_lyrics(song_title, artist_name)

        if "Lyrics not found" in result or "No matching song found" in result:
            not_found_count += 1  # Increment if lyrics are not found

        print(result)

    print(f"\nProcessing completed. Lyrics successfully saved in the database.")
    print(f"Total Songs: {len(song_list)}")
    print(f"Songs with missing lyrics: {not_found_count}")

def print_database(file_name):
    """
    Print a summary of the lyrics database.
    """
    try:
        df = pd.read_csv(file_name)
        if df.empty:
            print("The lyrics database is empty.")
        else:
            print("\nLyrics Database Summary:")
            print(df.head())  # Display the first few rows
            print(f"\nTotal Songs: {len(df)}")
    except Exception as e:
        print(f"Error reading the database: {e}")

if __name__ == "__main__":
    song_list_file = "d1.csv"  # Replace with the path to your song list
    database_file = "lyrics_database.csv"
    process_songs(song_list_file)
    print_database(database_file)