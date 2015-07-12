import time
import requests

staticReturnUrl="https://www.pictobattle.com/areWeOnline"
serverStatus=False
previousServerStatus=False
setActiveUrl="https://slack.com/api/users.setActive"
setAwayUrl="https://slack.com/api/users.setPresence"
postMessageUrl="https://slack.com/api/chat.postMessage"
botKey="xoxb-7546556583-hJSRQbEwKTNchrCdeEfsPxMT"
channelName='C07G385RD'

while True:
    time.sleep(1)
    print("beginning...")
    r = requests.get(staticReturnUrl, verify=False)
    content = r.text
    if content=="we must be...":
        serverStatus=True
        print("online")
    else:
        serverStatus=False
        print("offline")

    if not serverStatus == previousServerStatus:
        if serverStatus: #changed to True
            # active set
            payload = {'token': botKey}
            r = requests.post(setActiveUrl, data=payload)
            print(r.text)
            # message post
            payload = {'token': botKey, 'channel': channelName, 'text': 'Web Server Online'}
            r = requests.post(postMessageUrl, data=payload)
            print(r.text)
        else: #changed to False
            #message post
            payload = {'token': botKey, 'channel': channelName, 'text': 'Web Server Offline'}
            r = requests.post(postMessageUrl, data=payload)
            print(r.text)

            # away set
            payload = {'token': botKey, 'presence': 'away'}
            r = requests.post(setAwayUrl, data=payload)
            print(r.text)
        previousServerStatus = serverStatus
