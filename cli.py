class Cli(object):
    def __init__(self):
        super().__init__()

    def promptUser(self, prompt):
        s = input(prompt)
        return s
