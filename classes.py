class Human:
    def __init__(self, n, o):
        self.name = n  # properties
        self.occupation = o

    def do_work(self):  # methos
        if self.occupation == "tennis player":
            print(self.name, "Plays tennis")
        elif self.occupation == "actor":
            print(self.name, "Shoots film")

    def speaks(self):  # methods
        print(self.name, "Says how are you")


tom = Human("tom Cruise", "actor")
tom.do_work()
tom.speaks()

maria = Human("maria sharapova","tennis player")
maria.do_work()
maria.speaks()