class test:
    __x = []

    def __init__(self) -> None:
        self.__x.append(1)
        print(self.__x)

z = []
for x in range(5):
    z.append(test())
