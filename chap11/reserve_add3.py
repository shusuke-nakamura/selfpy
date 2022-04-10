class Coordinate:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, Coordinate):
            return Coordinate(self.x + other.x, self.y + other.y)
        elif isinstance(other, int):
            return Coordinate(self.x + other, self.y)
        else:
            raise TypeError('type must be Coordinate or int')
    
    def __str__(self) -> str:
        return f'({self.x},{self.y})'

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

if __name__ == '__main__':
    c1 = Coordinate(10, 20)
    c2 = Coordinate(15, 25)

    c1 += c2
    print(c1)

