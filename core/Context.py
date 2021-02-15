class Context:
    def __init__(self, send_message, obj, upload_photo):
        print(obj)
        self.message = obj.copy()
        self.upload_photo = lambda path: upload_photo(path, self.message['from_id'])
        self.reply = lambda msg, *args: send_message(self.message['peer_id'], msg, args)
