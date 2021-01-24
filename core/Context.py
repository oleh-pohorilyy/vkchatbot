class Context:
    def __init__(self, send_message, obj):
        print(obj)
        self.message = obj.copy()
        self.reply = lambda msg: send_message(self.message['peer_id'], msg)