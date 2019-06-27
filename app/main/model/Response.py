class Error:
    def __init__(self, reason):
        self.reason = reason
        self.confirmation = "Failed"

    def json(self):
        return {
            "confirmation": self.confirmation,
            "reason": self.reason
        }


class Success:
    def __init__(self, data):
        self.data = data
        self.confirmation = "Successful"

    def json(self):
        return {
            "confirmation": self.confirmation,
            "data": self.data
        }
