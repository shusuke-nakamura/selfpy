def log_func(func):
    def inner(*args, **keywords):
        print('------------------------')
        print(f'Name: {func.__name__}')
        print(f'Args: {args}')
        print(f'Keywords: {keywords}')
        print('------------------------')
        return func(*args, **keywords)
    return inner


def hoge(x, y, m='bar', n='piyo'):
    print(f'hoge: {x}-{y}/{m}-{n}')


log_hoge = log_func(hoge)
log_hoge(15, 37, m='ほげ', n='ぴよ')
