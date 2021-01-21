import requests
import re


class Context:

    def __init__(self, sendMessage, obj):
        print(obj)
        self.message = obj.copy()
        self.reply = lambda msg: sendMessage(self.message['peer_id'], msg)


class LongPoll:
    commands = {}

    def __init__(self, token, group_id):
        #  PROXYREMOVE  #
        self.ip = 'olegpogorili_mail_ru:5e60882a6a@45.13.192.215:30009'
        self.proxies = {
            'http': 'http://' + self.ip,
            'https': 'http://' + self.ip
        }
        #  PROXYREMOVE END #
        self.key = None
        self.server = None
        self.ts = 0
        self.wait = 20
        
        self.session = requests.Session()
        #  PROXYREMOVE  #
        self.session.proxies.update(self.proxies)
        #  PROXYREMOVE END  #
        self.v = '5.80'
        self.token = token
        self.id = group_id
        
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
            if event['type'] == 'message_new':
                text = event['object']['text']
                matches = list(filter(lambda x: re.search(x, text) is not None, list(self.commands.keys())))
                if len(matches) != 0:
                    self.commands[matches[0]](Context(self.sendMessage, event['object']))

    def create_context(self, obj):
        return {
            "reply": lambda msg: self.sendMessage(obj['peer_id'], msg),
            "message": obj.copy()
        }

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
            return response
            
    def sendMessage(self, user_id, text):
        values = {
            'user_id': user_id,
            'message': text
        }
        
        self.method('messages.send', values)
