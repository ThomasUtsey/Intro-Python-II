
class Car:
    runs = True

    def __init__(self, name):
        print("New Car")
        self.name = name

    def __str__(self):
        return f"My car the {self.name} currenty {self.runs} "

    def start(self):
        if self.runs:
            print(f"{self.name} car is started")
        else:
            print(f"{self.name} car is broken :(!")


mustang = Car('mustang')
# print(type(mustang))
# mustang.runs = False
print(str(mustang))
mustang.start()
