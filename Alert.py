import time
import requests

Webhook = "YOUR-WEBHOOK-URL"
Name = "YOUR-USERNAME-HERE"

# Feel free to change the message.
def send_message():
    message_content = f'''
{Name}, it's time to upload to Youtube, the channel is no longer rate limited..
Or perhaps you should finally buy a temp number or a new phone + sim card.......
https://quackr.io/temporary-numbers | https://quackr.io/rent-sms-numbers
    '''
    message = {"content": message_content}
    requests.post(Webhook, json=message)

if __name__ == __name__:
    send_message()
    time.sleep(86400)