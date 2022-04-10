from unicodedata import name


class Person:
    def __init__(self, firstname, lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname
    
    def __hash__(self) -> int:
        return hash((self.firstname, self.lastname))

if __name__ == '__main__':
    p = Person('太郎','山田')
    dic = {p: '男'}
    print(dic[p])



