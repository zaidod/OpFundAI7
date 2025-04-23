import os
import json
import time
try:
    import requests
    from googleapiclient.discovery import build
except ImportError:
    os.system("pip install requests")
    os.system("pip3 install requests")
    os.system("pip install googleapiclient.discovery")
    os.system("pip3 install googleapiclient.discovery")
YOUTUBE_API_KEY = 'YOUR-API-KEY'
DISCORD_WEBHOOK_URL = 'YOUR-WEBHOOK-URL'
CHANNEL_ID = 'YOUR-CHANNEL-URL'
DATA_FILE = 'sent_videos.json'
def load_sent_videos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    else:
        return set()
def save_sent_videos(sent_videos):
    with open(DATA_FILE, 'w') as file:
        json.dump(list(sent_videos), file)
def get_latest_video_url(api_key, channel_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.search().list(
        part='id',
        channelId=channel_id,
        order='date',
        type='video',
        maxResults=1
    )
    response = request.execute()
    if 'items' in response and len(response['items']) > 0:
        video_id = response['items'][0]['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        return video_url
    else:
        return None
def send_to_discord_webhook(webhook_url, video_url):
    payload = {'content': video_url}
    response = requests.post(webhook_url, json=payload)
    return response.status_code
if __name__ == '__main__':
    sent_videos = load_sent_videos()
    while True:
        latest_video_url = get_latest_video_url(YOUTUBE_API_KEY, CHANNEL_ID)
        if latest_video_url and latest_video_url not in sent_videos:
            status_code = send_to_discord_webhook(DISCORD_WEBHOOK_URL, latest_video_url)
            if status_code == 204:
                sent_videos.add(latest_video_url)
                save_sent_videos(sent_videos)
                print('Video URL sent to Discord successfully!')
            else:
                print(f'Failed to send video URL to Discord. Status code: {status_code}')
        time.sleep(3600)
