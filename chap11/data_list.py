import dataclasses

@dataclasses.dataclass(frozen=True)
class Person:
    firstname: str
    lastname: str
    age: int = 0
    memos: list = dataclasses.field(default_factory=list)
    
ms = ['married', 'AB']
p = Person('太郎', '山田', 58, ms)
ms.append('dog')
print(p)

p = Person('太郎', '山田', 58, ['married', 'AB'])
p.memos.append('dog')
print(p)
