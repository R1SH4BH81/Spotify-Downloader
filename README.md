# Spotify-Downloader


# Spotify-to-YouTube Downloader

This Python script allows you to download the audio of a song from Spotify by providing its Spotify link. It utilizes the Spotipy and Pytube libraries to interact with the Spotify API and download the audio from YouTube.

## Prerequisites
1. **Spotipy:** Ensure you have the Spotipy library installed. You can install it using:
    ```
    pip install spotipy
    ```

2. **Pytube:** Make sure you have the Pytube library installed. You can install it with:
    ```
    pip install pytube
    ```

## Usage
1. **Spotify Authentication:**
    - Replace `'your_client_id'` and `'your_client_secret'` with your Spotify API credentials. If you don't have them, you can obtain them by creating a Spotify Developer account.

2. **Run the Script:**
    - Execute the script and enter the Spotify song link when prompted.

3. **Download:**
    - The script will fetch information about the song from Spotify and then search for it on YouTube. It will download the highest quality audio stream available.

## Note
- Make sure to comply with the terms of service of both Spotify and YouTube when using this script. Downloading content without permission may violate their policies.

## Disclaimer
This script is intended for educational and personal use only. The developer is not responsible for any misuse or violation of terms of service.

Feel free to modify and enhance the script according to your needs. If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.
