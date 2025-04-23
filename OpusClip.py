# Import crucial libs.
import os
import platform
import webbrowser
import time
import socket

# Create a clear function.
def Clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Create a function to exit out.
def ExitHandler():
    time.sleep(1)
    Clear()
    exit("An error has occured.")

def NoInternet():
    if socket.create_connection(("www.google.com", 80)):
        print("Internet is connected!\nOpFundAI shall run!")
    else:
        exit("You have no internet connection ):\nOpFundAI is unable to work now!")

# Create a function to install everything PyOpus needs.
def Installer():
    # Install pip and upgrade it to the latest version (if not installed or if downgraded).
    system_platform = platform.system()
    if system_platform == "Windows":
        os.system("python -m ensurepip --default-pip")
        os.system("python -m pip install --upgrade pip")
    elif system_platform == "Darwin" or system_platform == "Linux":
        os.system("sudo apt-get install python3-pip")
        os.system("sudo yum install python3-pip") 
        os.system("sudo dnf install python3-pip")
        os.system("sudo pacman -S python-pip")
        os.system("python3 -m pip install --upgrade pip")
    elif system_platform == "Android":
        os.system("pip install --upgrade pip")
        os.system("pip3 install --upgrade pip")
    else:
        ExitHandler()
    
    # Install all libs.
    os.system("pip install Packaged.txt")
    os.system("pip3 install Packaged.txt")
    os.system("pip install --upgrade Packaged.txt")
    os.system("pip3 install --upgrade Packaged.txt")
    Clear()

# Define some very important stuff.
COOKIES = "Just sync with your browser bruh.."
ROBOT_ID = "YOUR-ROBOT-ID"
MONITOR_ID = "YOUR-ROBOT-ID"
API_KEY = "YOUR-API-KEY"
VERSION = "v2" # Change if the there is an API update.
URL = f"https://api.browse.ai/{VERSION}/"

# Import all needed libs that are 3rd party and install them if not installed.
try:
    import requests
except ImportError:
    Installer()

# Create a function to check the API stats.
def CheckAPIStats():
    url = f"https://api.browse.ai/{VERSION}/status"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.request("GET", url, headers=headers)
    print(response.text)

# Create a function to check how many robots you have.
def RobotAmount():
    url = f"https://api.browse.ai/{VERSION}/robots"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.request("GET", url, headers=headers)
    print(response.text)

# [!] Very useful function.
# This will allow you to change cookies, including session cookies, for logins and stuff.
def ChangeCookies():
    url = f"https://api.browse.ai/{VERSION}/robots/{ROBOT_ID}/monitors/{MONITOR_ID}"

    payload = {
        "name": "OpusClip",
        "inputParameters": {"originUrl": "https://clip.opus.pro/"},
        "schedule": "FREQ=HOURLY;INTERVAL=1;BYWEEKDAY=MO,TU,WE,TH,FR",
        "notifyOnCapturedScreenshotChange": False,
        "notifyOnCapturedTextChange": True,
        "capturedScreenshotNotificationThreshold": 16
    }
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.request("PATCH", url, json=payload, headers=headers)
    print(response.text)

# [!] Also a really useful function, not much context needed!
def GenerateVideo():
    url = f"https://api.browse.ai/{VERSION}/robots/{ROBOT_ID}/tasks"
    payload = {"inputParameters": {"originUrl": "https://clip.opus.pro/"}}
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.text)

# Useful for when making a PyAutoGUI screen scrape interaction!
def GetMousePosition():
    os.system("python3 Assets/Position.py")

# [!] VERY useful, as this will download the video generated through OpusAI!
def DownloadVideo():
    pass

def PyAutoDownload():
    pass

# Using BrowseAI i am able to make a BrowseAI account generator (: which auto re-creates the same robots (:
def BrowseAIGen():
    pass

# Create a function to manage webhooks.
def ChangeWebhook():
    # Couldn't find anything in the API docs about webhook managing with the API ):
    # So this will just take you to the webhook management page ):
    webbrowser.open_new_tab(f"https://dashboard.browse.ai/teams/personal/robots/{ROBOT_ID}/integration/webhooks")

# Create a function to manage intergrations.
def ManageIntergrations():
    # The same solution as ChangeWebhook() :/
    webbrowser.open_new_tab(f"https://dashboard.browse.ai/teams/personal/robots/{ROBOT_ID}/integration/")

# [!] Very useful function as well.
def ShuffleAccounts():
    pass

# Not a very good function at all, because BrowseAI automates everything in a cloud machine.
def UserAgentSpoofer():
    webbrowser.open_new_tab("https://chromewebstore.google.com/detail/user-agent-switcher-url-s/ljfpjnehmoiabkefmnjegmpdddgcdnpo?hl=en-GB")

# :/
def ProxyShuffle():
    webbrowser.open_new_tab("https://chromewebstore.google.com/detail/hoxx-vpn-proxy/nbcojefnccbanplpoffopkoepjmhgdgh?hl=en-GB")

# :/
def VPNShuffle():
    webbrowser.open_new_tab("https://chromewebstore.google.com/detail/hola-vpn-the-website-unbl/gkojfkhlekighikafcpjkiklfbnlmeio?hl=en-GB")
