import requests
import re
from Users import Users
from Context import Context
from pathlib import Path


class LongPoll:
    commands = {}

    def __init__(self, token, group_id, proxy):
        self.key = None
        self.server = None
        self.ts = 0
        self.wait = 20
        self.v = '5.80'
        self.token = token
        self.id = group_id

        self.session = requests.Session()
        if proxy["use_proxy"]:  # for Ukraine (configured in config.json)
            self.proxies = {
                'http': 'http://' + proxy["ip"],
                'https': 'http://' + proxy["ip"]
            }
            self.session.proxies.update(self.proxies)

        self.connect()

    def connect(self):
        response = self.method('groups.getLongPollServer', {'group_id': self.id})

        try:
            self.server = response['response']['server']
            self.key = response['response']['key']
            self.ts = response['response']['ts']
            print('[LongPoll] Connection TRUE!')
        except:
            print(response)

    def check(self):
        values = {
            'act': 'a_check',
            'key': self.key,
            'ts': self.ts,
            'wait': self.wait
        }

        response = self.session.get(
            self.server,
            params=values,
            timeout=25
        ).json()

        if 'failed' not in response:
            self.ts = response['ts']
            return response['updates']
        elif response['failed'] > 0:
            self.connect()

    def listen(self):
        while True:
            for event in self.check():
                yield event

    def start(self):
        for event in self.listen():
            if event['type'] == 'message_new' and event['object']["from_id"] > 0:
                context = Context(self.send_message, event['object'], self.upload_photo)
                text = context.message['text']
                matches = list(filter(lambda x: re.search(x, text) is not None, list(self.commands.keys())))
                if len(matches) != 0:
                    Users.check_registered(context)
                    self.commands[matches[0]](context)

    def command(self, regex, callback):
        callback_type = str(type(callback))
        if 'function' not in callback_type:
            raise Exception(f"Callback must be a function. Value: {callback_type}")

        self.commands[regex] = callback

    def method(self, method, values):

        values = values.copy() if values else {}
        values['access_token'] = self.token
        values['v'] = self.v
        response = self.session.post(
            'https://api.vk.com/method/' + method,
            values
        ).json()
        if 'error' in response:
            print('ERROR:\n' + response['error']['error_msg'])
            return False
        else:
            return dict(response)

    def upload_photo(self, photo_path, peer_id):
        upload_server_response = self.method('photos.getMessagesUploadServer', {"peer_id": peer_id, "scope": "photos"})
        upload_url = upload_server_response["response"]["upload_url"]

        with open(photo_path, 'rb') as photo:
            response = self.session.post(upload_url, files={'file1': photo})

        return self.method('photos.saveMessagesPhoto', dict(response.json()))

    def send_message(self, peer_id, text, attachment=None):

        values = {
            'peer_id': peer_id,
            'message': text
        }

        if attachment:
            values['attachment'] = attachment

        self.method('messages.send', values)
