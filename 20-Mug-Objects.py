class Mug:

    def __init__(self, capacity=8):
        self.capacity = capacity
        self.temp = 80
        self.contents = 0
        self.clean = True


    def fill(self):
        self.contents = self.capacity
        self.clean = False

    def drain(self):
        self.contents = 0

    def clean(self):
        self.clean = True
        self.contents = 0
        self.temp = 80


    def __str__(self):
        return f"Mug size {self.capacity} contents {self.contents} oz, clean: {self.clean} temp: {self.temp}"


# >>> exec(open('20-Mug-Objects.py', 'r').read())
