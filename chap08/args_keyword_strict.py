# arg2, arg3はキーワード引数であること
def my_func(arg1, *, arg2=0, arg3=0):
    pass


my_func(1, arg2=2, arg3=3)
