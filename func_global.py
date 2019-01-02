a = 50


def func():
    global a

    print('x is', a)
    a = 2
    print('x is', a)


func()
print('x is', a)
