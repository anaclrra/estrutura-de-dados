class NumComplexo:
    def __init__(self, real, img) -> None:
        self.__real = real
        self.__img = img
    def __str__(self) -> str:
        if(self.__img >= 0):
            return f"{self.__real} + {self.__img}j"
        else:
            return f"{self.__real} {self.__img}j"