# SIMPLE MESSAGE CLASS TO EXPLAIN UNIT-TESTING CONCEPTS
# Santiago Garcia Arango


class SimpleMessage:
    def __init__(self, sender, receiver, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message

    def get_message(self):
        return "Sender: {}\nReceiver: {}\nMessage: {}".format(
            self.sender, self.receiver, self.message
        )
