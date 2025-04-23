# Import some very crucial libs.
import os
import time
import pytz
import OpusClip as OC

# Import the rest of the libs and install them if not installed!
try:
    import requests
    import datetime
    from Google import Create_Service
    from googleapiclient.http import MediaFileUpload
except ImportError:
    OC.Installer()

# Clear the terminal.
OC.Clear()

# [!] Very important for clearing all the videos up!
def Cleanup():
    directory_path = "Videos"
    files = os.listdir(directory_path)
    for file in files:
        file_path = os.path.join(directory_path, file)
        os.remove(file_path)

# Just for backing up the videos (:
def SendToWebhook():
    webhook_url = "YOUR-WEBHOOK-URL"
    directory_path = "Videos"
    mp4_files = [f for f in os.listdir(directory_path) if f.endswith(".mp4")]

    for mp4_file in mp4_files:
        file_path = os.path.join(directory_path, mp4_file)
        
        with open(file_path, "rb") as file:
            payload = {"file": file}
            response = requests.post(webhook_url, files=payload)
            print(f"File '{mp4_file}' sent to webhook. Response: {response.status_code}")

# Create a function to upload everything to Youtube
def UploadToYTAPI():
    CLIENT_SECRET_FILE = 'Assets/Youtube.json'
    API_NAME = 'youtube'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    # Get a list of all .mp4 files in the "Videos" directory
    video_files = [f for f in os.listdir('Videos') if f.endswith('.mp4')]

    for video_file in video_files:
        # Construct the full file path
        file_path = os.path.join('Videos', video_file)

        # Get the title by removing the file extension (.mp4)
        title = os.path.splitext(video_file)[0]

        # Set the upload date time to the current time
        upload_date_time = datetime.datetime.now().isoformat() + '.000Z'

        # Construct the request body for each video
        # Change these settings if you want
        request_body = {
            'snippet': {
                'categoryId': 25,  # News and Politics
                'title': title,   # Set the title!
                'description': '#shorts',
            },
            'status': {
                'privacyStatus': 'public',
                'selfDeclaredMadeForKids': False,
            },
            'notifySubscribers': True
        }

        mediaFile = MediaFileUpload(file_path)

        # Upload the video
        response_upload = service.videos().insert(
            part='snippet,status',
            body=request_body,
            media_body=mediaFile
        ).execute()

        print(f"Video '{title}' uploaded to YouTube. Video ID: {response_upload.get('id')}")

        # Sleep for 15 seconds before uploading the next video
        time.sleep(15)

# Create a function to upload all the videos to Instagram.
def UploadToInstagram():
    pass

# Create a function to upload all the videos to Facebook.
def UploadToFacebook():
    pass

# Create a function to upload all the videos to Kick.
def UploadToKick():
    pass

# Create a function to upload all the videos to TikTok.
def UploadToTikTok():
    pass

def DoAll():
    SendToWebhook()
    UploadToYTAPI()
    UploadToInstagram()
    UploadToFacebook()
    UploadToKick()
    UploadToTikTok()
    Cleanup()

# If ran on UploadVideos.py then run it all well (;
if __name__ == "__main__":
    DoAll()
