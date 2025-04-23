# Import all needed libs.
import time
import OpusClip as OC
import Scraper 
import UploadVideos as UV

# Set a delay.
Delay = 5

# Startup the bot!
try:
    while True:
        # Check if you have internet.
        OC.NoInternet()

        # Clear the terminal.
        OC.Clear()

        # Scrape all the channels.
        Scraper.ScrapeRandom()
        time.sleep(Delay)

        # Now upload the videos!
        UV.DoAll()
        time.sleep(Delay)
        
        # Now wait another 24 hours.
        time.sleep(86400)
except Exception as e:
    OC.Clear()
    print("\nUh oh!\nLooks like the Youtube API key has been exceeded ):\nor something else idk")
