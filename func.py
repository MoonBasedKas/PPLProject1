class x:
    def __init__(self) -> None:
        self.q = 2
    
    def add(self, x: float, y: float):
        return x + y + 2
    

class z:
    def __init__(self) -> None:
        self.q = 3

class y (x, z):
    def __init__(self) -> None:
        self.x.__init__()
        self.y.__init__()
        self.q = 1
        print(self.super().q)
    

m = y()
# print(z.add(2, 2))