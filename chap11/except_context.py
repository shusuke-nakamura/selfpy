class MyContext:
    def __enter__(self):
        print('**Enter**')
        return self
    
    def __exit__(self, type, value, tb):
        if type is None:
            print('**Exti**')
        else:
            print(f'**{value}**')
            return True
    
    def hoge(self):
        print('Hoge')

with MyContext() as c:
    print('With Start')
    c.hoge()

