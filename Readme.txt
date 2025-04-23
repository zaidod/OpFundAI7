BrowseAI Project Name: OpFundAI
Robot ID: YOUR-ROBOT-ID
Monitor ID: YOUR-MONITOR-ID (You don't really need one)
API Key: YOUR-API-KEY
Webhook: YOUR-WEBHOOK-URL (If you want error logging and testing to be setup to be done)

Google Project Name: OpFundAI
Project ID: YOUR-PROJECT-ID
Project Number: YOUR-PROJECT-NUMBER
Client ID: YOUR-CLIENT-ID
Youtube API Key: YOUR-YOUTUBE-API-KEY
JSON Filename: Youtube.json

Built to run on a cloud machine!

I would suggest using Linode or Google Cloud.

Make sure Python is installed on the cloud machine, the code should auto install any dependencies needed, but if you run into any errors try: pip install -r Assets/Packaged.txt
If that doesn't work then do pip3 instead.

Then modify 'OpusClip.py' with your code editor, and go to the definitions section, and replace everything with yours, then do the same for 'Scraper.py' then do the same for 'UploadVideos.py'.

To get your 'Videos.json' file, it will be in your Google project and Google will give it to you when you generate the client ID, there will be a download button and you should save it as 'Youtube.json', then add it to /Assets

Also, make sure in the browser settings on the cloud machine, that it is up to date and has the downloads directory set to 'OpFundAI7/Videos'

Now, run 'App.py' modify anything you want, it is all for you to play and have fun with!

Any problems still occurring then please contact us at WiiCode@proton.me

Planning to add in a built in video editing soon, that adds in the most popular music scraped from TikTok with certain requests and stuff, but anyone will be able to define this as 'True' or 'False'

It will also add a special effect randomised by the code to the video!

I might also try and re-write the whole thing to C, for enhanced performance and for easy porting, but if I can't then it will be Lua or Java.

There will soon also be a configs.json file that allows you to set everything, and potentially in the future, a GUI tool for running the bot and confiuring everything.

-Divided
(github.com/DividedRanYou)