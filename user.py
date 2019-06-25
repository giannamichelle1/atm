class User(object):
    def __init__(self):
        self.name = ""
        self.pin = ""
        self.money = 0

    def __init__(self, name, pin, money=0):
        self.name = name
        self.pin = pin
        self.money = money
        
