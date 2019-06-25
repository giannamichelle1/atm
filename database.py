import os
from user import User

class Database(object):
    def __init__(self, filePath):
        self.__filePath = filePath
        self.__users = []
        
    def open(self):
        if not os.path.exists(self.__filePath):
            with open(self.__filePath, 'w'): pass
        else:
            with open(self.__filePath, "r") as file:
                readLines = file.readlines()
                for line in readLines:
                    Split = line.split(" ")
                    tmp = User(Split[0], Split[1], int(Split[2]))
                    self.__users.append(tmp)

    def close(self):
        with open (self.__filePath, "w+") as file:
            for user in self.__users:
                file.write(user.name + " " + user.pin + " " + str(user.money) + "\n")

    def add(self, user):
        self.__users.append(user)

    def authenticate(self, potential):
        index = -1
        for i in range(0, len(self.__users)):
            user = self.__users[i]
            if potential.name == user.name and potential.pin == user.pin:
                index = i
                break
        return index

    def getUserData(self, userIndex):
        return self.__users[userIndex]

    def save(self, user):
        
        
