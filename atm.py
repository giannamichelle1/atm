from cli import Cli
from user import User
from database import Database

class Atm(object):
    def run(self):
        self.__database.open()
        name = self.__interface.promptUser("what is your name? ")
        name = name.lower()
        pin = self.__interface.promptUser("what is your pin? ")
        user = User(name, pin)
        userIndex = self.__database.authenticate(user)
        if userIndex == -1:
            print("Access is denied!")
            
        else:
            user = self.__database.getUserData(userIndex)
            print("Welcome " + user.name + "!")
            Input = ""
            while Input != "exit":
                Input = self.__interface.promptUser("Withdrawal, Deposit, or Balance? ")
                Input = Input.lower()
                if Input == "withdrawal":
                    self._withdrawal(user)

                elif Input == "deposit":
                     self._deposit(user)

                elif Input == "balance":
                    self._balance(user)

                elif Input != "exit":
                    print("Invalid command!")
        self.__database.close()
        self._exit()
        		
    def _withdrawal(self, user):
        m = self.__interface.promptUser("How much would you like to withdrawal? ")
        m = int(m)
        user.money = user.money - m
        self.__database.save(user)
        self._balance(user)
        
    def __init__(self):
        super().__init__()
        self.__interface = Cli()
        self.__database = Database("database.txt")

    def _deposit(self, user):
        m = self.__interface.promptUser("How much would you like to deposit? ")
        m = int(m)
        user.money = user.money + m
        self.__database.save(user)
        self._balance(user)

    def _balance(self, user):
        print("Your balance is " + str(user.money) + "!")

    def _exit(self):
        print("Goodbye!")
