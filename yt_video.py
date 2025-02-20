import yt_dlp
import os

def download_youtube_video(url, resolution="1080p", download_path="./"):
    try:
        # Ensure the download path exists
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        # Define the download options
        ydl_opts = {
            'format': f'bestvideo[height<={resolution[:-1]}]+bestaudio/best[height<={resolution[:-1]}]',
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }]
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Download the video
            ydl.download([url])
        
        print(f"Downloaded video successfully to {download_path}!")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# URL of the YouTube video to be downloaded
video_url = "Enter URL"

# Path where the video should be downloaded
download_path = "./downloads"

# Call the function to download the video
download_youtube_video(video_url, download_path=download_path)
