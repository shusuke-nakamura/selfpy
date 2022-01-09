class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


if __name__ == '__main__':
    p1 = Person('太郎', '山田')
    p1.age = 52
    print(p1.age)
