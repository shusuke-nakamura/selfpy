def log_func(func):
    def inner(*args, **keywords):
        print('------------------------')
        print(f'Name: {func.__name__}')
        print(f'Args: {args}')
        print(f'Keywords: {keywords}')
        print('------------------------')
        return func(*args, **keywords)
    return inner


@log_func
def hoge(x, y, m='bar', n='piyo'):
    print(f'hoge: {x}-{y}/{m}-{n}')


hoge(15, 37, m='ほげ', n='ぴよ')
