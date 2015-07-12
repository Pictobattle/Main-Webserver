import time
import requests

staticReturnUrl="https://www.pictobattle.com/areWeOnline"
serverStatus=False
previousServerStatus=False
presenceUrl="https://slack.com/api/users.setPresence"
postMessageUrl="https://slack.com/api/chat.postMessage"
botKey="xoxb-7546556583-ICe26Ly9gsWqzoju8EuLt0Q8"
botName="webserver"
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
            # presence set
            payload = {'token': botKey, 'presence': 'auto'}
            r = requests.post(presenceUrl, data=payload)
            print(r.text)
            # message post
            payload = {'token': botKey, 'channel': channelName, 'text': 'Web Server Online', 'as_user': 'true'} #'username': botName}
            r = requests.post(postMessageUrl, data=payload)
            print(r.text)
        else: #changed to False
            #message post
            payload = {'token': botKey, 'channel': channelName, 'text': 'Web Server Offline', 'as_user': 'true'} #'username': botName}
            r = requests.post(postMessageUrl, data=payload)
            print(r.text)

            # presence set
            payload = {'token': botKey, 'presence': 'away'}
            r = requests.post(presenceUrl, data=payload)
            print(r.text)
        previousServerStatus = serverStatus
