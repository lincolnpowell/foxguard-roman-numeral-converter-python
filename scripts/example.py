class Example:
    def __init__(self, message):
        if message == "":
            raise ValueError("Invalid message")
        self._message = message

    def get_message(self):
        return self._message
