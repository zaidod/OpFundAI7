# Import all the libs needed.
import OpusClip as OC
import random
import platform
import time
import webbrowser
import urllib.request
import json
from datetime import datetime, timedelta

# Define some very important stuff.
api_key = 'YOUR-API-KEY' # api key for youtube (latest version, data youtube api)
robot_id = "YOUR-ROBOT-ID" # robot id for browseai

# Install all third party libs.
try:
    import pyautogui as pag
    from PIL import Image
    import pyperclip
except ImportError:
    OC.Installer()

# Cleanup the terminal.
OC.Clear()

# Create a function to test it out and try it on Divided's channel!
def Test():
    channel_id = 'UCKmm2-O4aWKYUlqdnvtogEQ'
    url = f'https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet,id&order=viewCount&maxResults=5'
    one_week_ago = (datetime.now() - timedelta(days=7)).isoformat() + 'Z'
    url += f'&publishedAfter={one_week_ago}'
    with urllib.request.urlopen(url) as response:
        data = response.read()
        resp = json.loads(data.decode('utf-8'))

    # List to store all video URLs
    video_urls = []

    for item in resp.get('items', []):
        title = item['snippet']['title']
        print(f'Title: {title}')
        video_id = item['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        
        # Pack the URL into a list and add a comment
        video_urls.append(video_url)  # Variable to store the video URL
        print(f'URL: {video_url}')

        statistics_url = f'https://www.googleapis.com/youtube/v3/videos?key={api_key}&part=statistics&id={video_id}'
        with urllib.request.urlopen(statistics_url) as stat_response:
            stat_data = stat_response.read()
            stat_resp = json.loads(stat_data.decode('utf-8'))
            likes = stat_resp['items'][0]['statistics']['likeCount']
            views = stat_resp['items'][0]['statistics']['viewCount']
            print(f'Likes: {likes}, Views: {views}')

        print('-' * 30)

    # Print all video URLs after the loop
    print("\nAll Video URLs:")
    for idx, url in enumerate(video_urls, start=1):
        print(f'Video {idx}: {url}')

    # Assign video URLs to variables
    video_url1 = video_urls[0] if len(video_urls) >= 1 else None
    video_url2 = video_urls[1] if len(video_urls) >= 2 else None
    video_url3 = video_urls[2] if len(video_urls) >= 3 else None
    video_url4 = video_urls[3] if len(video_urls) >= 4 else None
    video_url5 = video_urls[4] if len(video_urls) >= 5 else None
    
    # Upload them to OpusClip using BrowseAI (:
    #webbrowser.open_new_tab(f"https://dashboard.browse.ai/teams/personal/robots/{robot_id}/run")
    
    # Save video_url1 to the clipboard.
    pyperclip.copy(video_url1)
    
    # Open the URL and wait for the page to load, then scroll down lil bit, and click on the input bar.
    webbrowser.open_new_tab(f"https://dashboard.browse.ai/teams/personal/robots/{robot_id}/run")
    time.sleep(10)
    #for scroll in range(6):
        #pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.click(808, 385)
    
    # Paste video_url1, using a certain keyboard shortcut based on your operating system.
    if platform.system() == "Darwin":
        pag.hotkey('command', 'v')
    else:
        pag.hotkey('ctrl', 'v')
    
    # Press enter and go!
    time.sleep(3)
    pag.click(815, 453)
    
    # Now the video will be generating within OpusClip!

    # DOWNLOAD THE VIDEO!!!

    
    # From here it will have generated the video, now all ya need to do is download it!
    # Page with all the juicy download links (:

    # Open up the site, wait for it to load, click somewhere so we can scroll..
    webbrowser.open_new_tab("https://clip.opus.pro/dashboard")
    time.sleep(3600)
    pag.click(274, 641)

    # Scroll down a lil bit.
    for scroll in range(13):
        pag.press('down')

    # Double click on the generated video.
    for click in range(5):
        pag.click(274, 641)
    time.sleep(5)

    # From here it will have generated the video, now all ya need to do is download it!
    # Page with all the juicy download links (:
    pag.click(474, 215)

    # Move the mouse down.
    current_x, current_y = pag.position()

    # Choose how much to move the mouse down.
    distance_to_move = 573

    pag.move(0, distance_to_move, duration=0.5)

    # Download every other video!
    for finish in range(90):
        for scroll in range(1):
            pag.press('down')
        current_x, current_y = pag.position()
        pag.click(current_x, current_y)
        time.sleep(3)

    # NOW THEY HAVE BEEN DOWNLOADED
    # NOW WE NEED TO WRITE AN UPLOAD SCRIPT TO UPLOAD ALL THE VIDEOS TO YOUTUBE THROUGH THE API FROM THE DESKTOP DIRECTORY OR SMTH!!!
    pag.press('down')

# Create a function to scrape the top 5 most liked videos uploaded recently by Moon.
def ScrapeMoon():
    channel_id = 'UCmFeOdJI3IXgTBDzqBLD8qg'
    url = f'https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet,id&order=viewCount&maxResults=5'
    one_week_ago = (datetime.now() - timedelta(days=7)).isoformat() + 'Z'
    url += f'&publishedAfter={one_week_ago}'
    with urllib.request.urlopen(url) as response:
        data = response.read()
        resp = json.loads(data.decode('utf-8'))

    # List to store all video URLs
    video_urls = []

    for item in resp.get('items', []):
        title = item['snippet']['title']
        print(f'Title: {title}')
        video_id = item['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        
        # Pack the URL into a list and add a comment
        video_urls.append(video_url)  # Variable to store the video URL
        print(f'URL: {video_url}')

        statistics_url = f'https://www.googleapis.com/youtube/v3/videos?key={api_key}&part=statistics&id={video_id}'
        with urllib.request.urlopen(statistics_url) as stat_response:
            stat_data = stat_response.read()
            stat_resp = json.loads(stat_data.decode('utf-8'))
            likes = stat_resp['items'][0]['statistics']['likeCount']
            views = stat_resp['items'][0]['statistics']['viewCount']
            print(f'Likes: {likes}, Views: {views}')

        print('-' * 30)

    # Print all video URLs after the loop
    print("\nAll Video URLs:")
    for idx, url in enumerate(video_urls, start=1):
        print(f'Video {idx}: {url}')

    # Assign video URLs to variables
    video_url1 = video_urls[0] if len(video_urls) >= 1 else None
    video_url2 = video_urls[1] if len(video_urls) >= 2 else None
    video_url3 = video_urls[2] if len(video_urls) >= 3 else None
    video_url4 = video_urls[3] if len(video_urls) >= 4 else None
    video_url5 = video_urls[4] if len(video_urls) >= 5 else None

    # Upload them to OpusClip using BrowseAI (:
    #webbrowser.open_new_tab(f"https://dashboard.browse.ai/teams/personal/robots/{robot_id}/run")
    
    # Save video_url1 to the clipboard.
    pyperclip.copy(video_url1)
    
    # Open the URL and wait for the page to load, then scroll down lil bit, and click on the input bar.
    webbrowser.open_new_tab(f"https://dashboard.browse.ai/teams/personal/robots/{robot_id}/run")
    time.sleep(10)
    #for scroll in range(6):
        #pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.click(808, 385)

    # Paste video_url1, using a certain keyboard shortcut based on your operating system.
    if platform.system() == "Darwin":
        pag.hotkey('command', 'v')
    else:
        pag.hotkey('ctrl', 'v')
    
    # Press enter and go!
    time.sleep(3)
    pag.click(815, 453)
    
    # Now the video will be generating within OpusClip!

    # DOWNLOAD THE VIDEO!!!

    
    # From here it will have generated the video, now all ya need to do is download it!
    # Page with all the juicy download links (:

    # Open up the site, wait for it to load, click somewhere so we can scroll..
    webbrowser.open_new_tab("https://clip.opus.pro/dashboard")
    time.sleep(3600)
    pag.click(274, 641)

    # Scroll down a lil bit.
    for scroll in range(13):
        pag.press('down')

    # Double click on the generated video.
    for click in range(5):
        pag.click(274, 641)
    time.sleep(5)

    # From here it will have generated the video, now all ya need to do is download it!
    # Page with all the juicy download links (:
    pag.click(474, 215)

    # Move the mouse down.
    current_x, current_y = pag.position()

    # Choose how much to move the mouse down.
    distance_to_move = 573

    pag.move(0, distance_to_move, duration=0.5)

    # Download every other video!
    for finish in range(90):
        for scroll in range(1):
            pag.press('down')
        current_x, current_y = pag.position()
        pag.click(current_x, current_y)
        time.sleep(3)

    # NOW THEY HAVE BEEN DOWNLOADED
    # NOW WE NEED TO WRITE AN UPLOAD SCRIPT TO UPLOAD ALL THE VIDEOS TO YOUTUBE THROUGH THE API FROM THE DESKTOP DIRECTORY OR SMTH!!!
    pag.press('down')

# Create a function to scrape the top 5 most liked videos on PMU.
def ScrapePeirs():
    channel_id = 'UCatt7TBjfBkiJWx8khav_Gg'
    url = f'https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet,id&order=viewCount&maxResults=5'
    one_week_ago = (datetime.now() - timedelta(days=7)).isoformat() + 'Z'
    url += f'&publishedAfter={one_week_ago}'
    with urllib.request.urlopen(url) as response:
        data = response.read()
        resp = json.loads(data.decode('utf-8'))

    # List to store all video URLs
    video_urls = []

    for item in resp.get('items', []):
        title = item['snippet']['title']
        print(f'Title: {title}')
        video_id = item['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        
        # Pack the URL into a list and add a comment
        video_urls.append(video_url)  # Variable to store the video URL
        print(f'URL: {video_url}')

        statistics_url = f'https://www.googleapis.com/youtube/v3/videos?key={api_key}&part=statistics&id={video_id}'
        with urllib.request.urlopen(statistics_url) as stat_response:
            stat_data = stat_response.read()
            stat_resp = json.loads(stat_data.decode('utf-8'))
            likes = stat_resp['items'][0]['statistics']['likeCount']
            views = stat_resp['items'][0]['statistics']['viewCount']
            print(f'Likes: {likes}, Views: {views}')

        print('-' * 30)

    # Print all video URLs after the loop
    print("\nAll Video URLs:")
    for idx, url in enumerate(video_urls, start=1):
        print(f'Video {idx}: {url}')

    # Assign video URLs to variables
    video_url1 = video_urls[0] if len(video_urls) >= 1 else None
    video_url2 = video_urls[1] if len(video_urls) >= 2 else None
    video_url3 = video_urls[2] if len(video_urls) >= 3 else None
    video_url4 = video_urls[3] if len(video_urls) >= 4 else None
    video_url5 = video_urls[4] if len(video_urls) >= 5 else None

    # Upload them to OpusClip using BrowseAI (:
    #webbrowser.open_new_tab(f"https://dashboard.browse.ai/teams/personal/robots/{robot_id}/run")
    
    # Save video_url1 to the clipboard.
    pyperclip.copy(video_url1)
    
    # Open the URL and wait for the page to load, then scroll down lil bit, and click on the input bar.
    webbrowser.open_new_tab(f"https://dashboard.browse.ai/teams/personal/robots/{robot_id}/run")
    time.sleep(10)
    #for scroll in range(6):
        #pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.click(808, 385)
    
    # Paste video_url1, using a certain keyboard shortcut based on your operating system.
    if platform.system() == "Darwin":
        pag.hotkey('command', 'v')
    else:
        pag.hotkey('ctrl', 'v')
    
    # Press enter and go!
    time.sleep(3)
    pag.click(815, 453)
    
    # Now the video will be generating within OpusClip!

    # DOWNLOAD THE VIDEO!!!

    
    # From here it will have generated the video, now all ya need to do is download it!
    # Page with all the juicy download links (:

    # Open up the site, wait for it to load, click somewhere so we can scroll..
    webbrowser.open_new_tab("https://clip.opus.pro/dashboard")
    time.sleep(3600)
    pag.click(274, 641)

    # Scroll down a lil bit.
    for scroll in range(13):
        pag.press('down')

    # Double click on the generated video.
    for click in range(5):
        pag.click(274, 641)
    time.sleep(5)

    # From here it will have generated the video, now all ya need to do is download it!
    # Page with all the juicy download links (:
    pag.click(474, 215)

    # Move the mouse down.
    current_x, current_y = pag.position()

    # Choose how much to move the mouse down.
    distance_to_move = 573

    pag.move(0, distance_to_move, duration=0.5)

    # Download every other video!
    for finish in range(90):
        for scroll in range(1):
            pag.press('down')
        current_x, current_y = pag.position()
        pag.click(current_x, current_y)
        time.sleep(3)

    # NOW THEY HAVE BEEN DOWNLOADED
    # NOW WE NEED TO WRITE AN UPLOAD SCRIPT TO UPLOAD ALL THE VIDEOS TO YOUTUBE THROUGH THE API FROM THE DESKTOP DIRECTORY OR SMTH!!!
    pag.press('down')

# Create a function to scrape the top 5 most liked videos uploaded recently by BBC news.
def ScrapeBBC():
    channel_id = 'UC16niRr50-MSBwiO3YDb3RA'
    url = f'https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet,id&order=viewCount&maxResults=5'
    one_week_ago = (datetime.now() - timedelta(days=7)).isoformat() + 'Z'
    url += f'&publishedAfter={one_week_ago}'
    with urllib.request.urlopen(url) as response:
        data = response.read()
        resp = json.loads(data.decode('utf-8'))

    # List to store all video URLs
    video_urls = []

    for item in resp.get('items', []):
        title = item['snippet']['title']
        print(f'Title: {title}')
        video_id = item['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        
        # Pack the URL into a list and add a comment
        video_urls.append(video_url)  # Variable to store the video URL
        print(f'URL: {video_url}')

        statistics_url = f'https://www.googleapis.com/youtube/v3/videos?key={api_key}&part=statistics&id={video_id}'
        with urllib.request.urlopen(statistics_url) as stat_response:
            stat_data = stat_response.read()
            stat_resp = json.loads(stat_data.decode('utf-8'))
            likes = stat_resp['items'][0]['statistics']['likeCount']
            views = stat_resp['items'][0]['statistics']['viewCount']
            print(f'Likes: {likes}, Views: {views}')

        print('-' * 30)

    # Print all video URLs after the loop
    print("\nAll Video URLs:")
    for idx, url in enumerate(video_urls, start=1):
        print(f'Video {idx}: {url}')

    # Assign video URLs to variables
    video_url1 = video_urls[0] if len(video_urls) >= 1 else None
    video_url2 = video_urls[1] if len(video_urls) >= 2 else None
    video_url3 = video_urls[2] if len(video_urls) >= 3 else None
    video_url4 = video_urls[3] if len(video_urls) >= 4 else None
    video_url5 = video_urls[4] if len(video_urls) >= 5 else None
    # Upload them to OpusClip using BrowseAI (:
    #webbrowser.open_new_tab(f"https://dashboard.browse.ai/teams/personal/robots/{robot_id}/run")
    
    # Save video_url1 to the clipboard.
    pyperclip.copy(video_url1)
    
    # Open the URL and wait for the page to load, then scroll down lil bit, and click on the input bar.
    webbrowser.open_new_tab(f"https://dashboard.browse.ai/teams/personal/robots/{robot_id}/run")
    time.sleep(10)
    #for scroll in range(6):
        #pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.click(808, 385)
    
    # Paste video_url1, using a certain keyboard shortcut based on your operating system.
    if platform.system() == "Darwin":
        pag.hotkey('command', 'v')
    else:
        pag.hotkey('ctrl', 'v')
    
    # Press enter and go!
    time.sleep(3)
    pag.click(815, 453)
    
    # Now the video will be generating within OpusClip!

    # DOWNLOAD THE VIDEO!!!

    
    # From here it will have generated the video, now all ya need to do is download it!
    # Page with all the juicy download links (:

    # Open up the site, wait for it to load, click somewhere so we can scroll..
    webbrowser.open_new_tab("https://clip.opus.pro/dashboard")
    time.sleep(3600)
    pag.click(274, 641)

    # Scroll down a lil bit.
    for scroll in range(13):
        pag.press('down')

    # Double click on the generated video.
    for click in range(5):
        pag.click(274, 641)
    time.sleep(5)

    # From here it will have generated the video, now all ya need to do is download it!
    # Page with all the juicy download links (:
    pag.click(474, 215)

    # Move the mouse down.
    current_x, current_y = pag.position()

    # Choose how much to move the mouse down.
    distance_to_move = 573

    pag.move(0, distance_to_move, duration=0.5)

    # Download every other video!
    for finish in range(90):
        for scroll in range(1):
            pag.press('down')
        current_x, current_y = pag.position()
        pag.click(current_x, current_y)
        time.sleep(3)

    # NOW THEY HAVE BEEN DOWNLOADED
    # NOW WE NEED TO WRITE AN UPLOAD SCRIPT TO UPLOAD ALL THE VIDEOS TO YOUTUBE THROUGH THE API FROM THE DESKTOP DIRECTORY OR SMTH!!!
    pag.press('down')

# Create a function to scrape from CBS news.
def ScrapeCBS():
    channel_id = 'UC8p1vwvWtl6T73JiExfWs1g'
    url = f'https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet,id&order=viewCount&maxResults=5'
    one_week_ago = (datetime.now() - timedelta(days=7)).isoformat() + 'Z'
    url += f'&publishedAfter={one_week_ago}'
    with urllib.request.urlopen(url) as response:
        data = response.read()
        resp = json.loads(data.decode('utf-8'))

    # List to store all video URLs
    video_urls = []

    for item in resp.get('items', []):
        title = item['snippet']['title']
        print(f'Title: {title}')
        video_id = item['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        
        # Pack the URL into a list and add a comment
        video_urls.append(video_url)  # Variable to store the video URL
        print(f'URL: {video_url}')

        statistics_url = f'https://www.googleapis.com/youtube/v3/videos?key={api_key}&part=statistics&id={video_id}'
        with urllib.request.urlopen(statistics_url) as stat_response:
            stat_data = stat_response.read()
            stat_resp = json.loads(stat_data.decode('utf-8'))
            likes = stat_resp['items'][0]['statistics']['likeCount']
            views = stat_resp['items'][0]['statistics']['viewCount']
            print(f'Likes: {likes}, Views: {views}')

        print('-' * 30)

    # Print all video URLs after the loop
    print("\nAll Video URLs:")
    for idx, url in enumerate(video_urls, start=1):
        print(f'Video {idx}: {url}')

    # Assign video URLs to variables
    video_url1 = video_urls[0] if len(video_urls) >= 1 else None
    video_url2 = video_urls[1] if len(video_urls) >= 2 else None
    video_url3 = video_urls[2] if len(video_urls) >= 3 else None
    video_url4 = video_urls[3] if len(video_urls) >= 4 else None
    video_url5 = video_urls[4] if len(video_urls) >= 5 else None

    # Upload them to OpusClip using BrowseAI (:
    #webbrowser.open_new_tab(f"https://dashboard.browse.ai/teams/personal/robots/{robot_id}/run")
    
    # Save video_url1 to the clipboard.
    pyperclip.copy(video_url1)
    
    # Open the URL and wait for the page to load, then scroll down lil bit, and click on the input bar.
    webbrowser.open_new_tab(f"https://dashboard.browse.ai/teams/personal/robots/{robot_id}/run")
    time.sleep(10)
    #for scroll in range(6):
        #pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.click(808, 385)
    
    # Paste video_url1, using a certain keyboard shortcut based on your operating system.
    if platform.system() == "Darwin":
        pag.hotkey('command', 'v')
    else:
        pag.hotkey('ctrl', 'v')
    
    # Press enter and go!
    time.sleep(3)
    pag.click(815, 453)
    
    # Now the video will be generating within OpusClip!

    # DOWNLOAD THE VIDEO!!!

    
    # From here it will have generated the video, now all ya need to do is download it!
    # Page with all the juicy download links (:

    # Open up the site, wait for it to load, click somewhere so we can scroll..
    webbrowser.open_new_tab("https://clip.opus.pro/dashboard")
    time.sleep(3600)
    pag.click(274, 641)

    # Scroll down a lil bit.
    for scroll in range(13):
        pag.press('down')

    # Double click on the generated video.
    for click in range(5):
        pag.click(274, 641)
    time.sleep(5)

    # From here it will have generated the video, now all ya need to do is download it!
    # Page with all the juicy download links (:
    pag.click(474, 215)

    # Move the mouse down.
    current_x, current_y = pag.position()

    # Choose how much to move the mouse down.
    distance_to_move = 573

    pag.move(0, distance_to_move, duration=0.5)

    # Download every other video!
    for finish in range(90):
        for scroll in range(1):
            pag.press('down')
        current_x, current_y = pag.position()
        pag.click(current_x, current_y)
        time.sleep(3)

    # NOW THEY HAVE BEEN DOWNLOADED
    # NOW WE NEED TO WRITE AN UPLOAD SCRIPT TO UPLOAD ALL THE VIDEOS TO YOUTUBE THROUGH THE API FROM THE DESKTOP DIRECTORY OR SMTH!!!
    pag.press('down')

# Create a function to scrape from Fox news.
def ScrapeFoxNews():
    channel_id = 'UCXIJgqnII2ZOINSWNOGFThA'
    url = f'https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet,id&order=viewCount&maxResults=5'
    one_week_ago = (datetime.now() - timedelta(days=7)).isoformat() + 'Z'
    url += f'&publishedAfter={one_week_ago}'
    with urllib.request.urlopen(url) as response:
        data = response.read()
        resp = json.loads(data.decode('utf-8'))

    # List to store all video URLs
    video_urls = []

    for item in resp.get('items', []):
        title = item['snippet']['title']
        print(f'Title: {title}')
        video_id = item['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        
        # Pack the URL into a list and add a comment
        video_urls.append(video_url)  # Variable to store the video URL
        print(f'URL: {video_url}')

        statistics_url = f'https://www.googleapis.com/youtube/v3/videos?key={api_key}&part=statistics&id={video_id}'
        with urllib.request.urlopen(statistics_url) as stat_response:
            stat_data = stat_response.read()
            stat_resp = json.loads(stat_data.decode('utf-8'))
            likes = stat_resp['items'][0]['statistics']['likeCount']
            views = stat_resp['items'][0]['statistics']['viewCount']
            print(f'Likes: {likes}, Views: {views}')

        print('-' * 30)

    # Print all video URLs after the loop
    print("\nAll Video URLs:")
    for idx, url in enumerate(video_urls, start=1):
        print(f'Video {idx}: {url}')

    # Assign video URLs to variables
    video_url1 = video_urls[0] if len(video_urls) >= 1 else None
    video_url2 = video_urls[1] if len(video_urls) >= 2 else None
    video_url3 = video_urls[2] if len(video_urls) >= 3 else None
    video_url4 = video_urls[3] if len(video_urls) >= 4 else None
    video_url5 = video_urls[4] if len(video_urls) >= 5 else None

    # Upload them to OpusClip using BrowseAI (:
    #webbrowser.open_new_tab(f"https://dashboard.browse.ai/teams/personal/robots/{robot_id}/run")
    
    # Save video_url1 to the clipboard.
    pyperclip.copy(video_url1)
    
    # Open the URL and wait for the page to load, then scroll down lil bit, and click on the input bar.
    webbrowser.open_new_tab(f"https://dashboard.browse.ai/teams/personal/robots/{robot_id}/run")
    time.sleep(10)
    #for scroll in range(6):
        #pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.press('down')
    pag.click(808, 385)
    
    # Paste video_url1, using a certain keyboard shortcut based on your operating system.
    if platform.system() == "Darwin":
        pag.hotkey('command', 'v')
    else:
        pag.hotkey('ctrl', 'v')
    
    # Press enter and go!
    time.sleep(3)
    pag.click(815, 453)
    
    # Now the video will be generating within OpusClip!

    # DOWNLOAD THE VIDEO!!!

    
    # From here it will have generated the video, now all ya need to do is download it!
    # Page with all the juicy download links (:

    # Open up the site, wait for it to load, click somewhere so we can scroll..
    time.sleep(10000)
    webbrowser.open_new_tab("https://clip.opus.pro/dashboard")
    time.sleep(3600)
    pag.click(274, 641)

    # Scroll down a lil bit.
    for scroll in range(13):
        pag.press('down')

    # Double click on the generated video.
    for click in range(5):
        pag.click(274, 641)
    time.sleep(5)

    # From here it will have generated the video, now all ya need to do is download it!
    # Page with all the juicy download links (:
    pag.click(474, 215)

    # Move the mouse down.
    current_x, current_y = pag.position()

    # Choose how much to move the mouse down.
    distance_to_move = 573

    pag.move(0, distance_to_move, duration=0.5)

    # Download every other video!
    for finish in range(90):
        for scroll in range(1):
            pag.press('down')
        current_x, current_y = pag.position()
        pag.click(current_x, current_y)
        time.sleep(3)

    # NOW THEY HAVE BEEN DOWNLOADED
    # NOW WE NEED TO WRITE AN UPLOAD SCRIPT TO UPLOAD ALL THE VIDEOS TO YOUTUBE THROUGH THE API FROM THE DESKTOP DIRECTORY OR SMTH!!!
    pag.press('down')
    
# [!] VERY USEFUL, I DONT THINK THIS NEEDS CONTEXT!!!
# Obv it will exclude test :/
def ScrapeRandom():
    Channels = [ScrapeBBC(), ScrapeCBS(), ScrapeFoxNews(), ScrapeMoon(), ScrapePeirs()]
    random_channel = random.choice(Channels)
    random_channel()
