import time
import requests

staticReturnUrl="https://www.pictobattle.com/areWeOnline"
serverStatus=False
previousServerStatus=False
presenceUrl="https://slack.com/api/users.setPresence"
postMessageUrl="https://slack.com/api/chat.postMessage"
botKey="xoxb-7546556583-hJSRQbEwKTNchrCdeEfsPxMT"
channelName='webserverstatus'

while True:
    time.sleep(1)
    print("beginning...")
    r = requests.get(staticReturnUrl)
    content = r.text
    if content=="we must be...":
        serverStatus=True
        print("online")
    else:
        serverStatus=False
        print("offline")

    if not serverStatus == previousServerStatus:
        '''
        messagePayload= {'token': botKey, 'channel': channelName, 'text': 'Web Server Offline'}
        if serverStatus:
            presencePayload = {'token': botKey, 'presence': 'auto'}
            r = requests.post(presenceUrl, data=presencePayload)
            messagePayload = {'token': botKey, 'channel': channelName, 'text': 'Web Server Online'}

        r = requests.post(postMessageUrl, data=messagePayload)
        else:
            presencePayload= {'token': botKey, 'presence': 'away'}
            r = requests.post(presenceUrl, data=presencePayload)

        '''
        #Version above errored on seperated else

        if serverStatus: #changed to True
            # presence set
            payload = {'token': botKey, 'presence': 'auto'}
            r = requests.post(presenceUrl, data=payload)

            # message post
            payload = {'token': botKey, 'channel': 'webserverstatus', 'text': 'Web Server Online'}
            r = requests.post(postMessageUrl, data=payload)
        else: #changed to False
            #message post
            payload = {'token': botKey, 'channel': 'webserverstatus', 'text': 'Web Server Offline'}
            r = requests.post(postMessageUrl, data=payload)

            # presence set
            payload = {'token': botKey, 'presence': 'away'}
            r = requests.post(presenceUrl, data=payload)
