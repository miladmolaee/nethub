class Multi:
    commands: str

    def set(self, script):
        self.commands = script

        print(self.commands)

    def run(self):
        print('run multi')