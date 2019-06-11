from cli import Cli

class Atm(object):
    def run(self):
        print("runningAtm")
        name = self._interface.promptUser("what is your name? ")
        print(name)
        pin = self._interface.promptUser("what is your pin? ")
        print (pin)
    def _withdrawal(self):
        pass

    def __init__(self):
        super().__init__()
        self._interface = Cli()
        print("constructing")

    def _deposit(self):
        pass

    def _balance(self):
        pass

    def _exit(self):
        pass
