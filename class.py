# Inheritance in Python.
class a:
    def __init__(self) -> None:
        self.x = 3
        return 3
    
    def p(self):
        print("A")


class b:
    def __init__(self) -> None:
        self.x = 1
        self.y = 2
        return 2

    def p(self):
        print("B")

    def bfunc(self):
        self.z = 0
        return 4

class ab (a,b):
    def __init__(self) -> None:
        print(super().__init__())
        print(self.x)
        print(self.bfunc(), self.z)
        self.p()

        

z = ab()