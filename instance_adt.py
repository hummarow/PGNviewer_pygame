# Abstract Data Type (ADT) of instsances


class Instance:
    def __init__(self, handler: int):
        if not handler or handler < 0:
            raise ValueError("Handler is not passed or negative value is passed when creating a new instance.")
        else:
            self.handler = handler
