def printMax(a, b):
    if a > b:
        print(a, 'more than ', b)
    elif a < b:
        print(b, 'more than', a)
    else:
        print(a, '=', b)


a = input(str('Pls, type a: '))
b = input(str('Pls, type b: '))

printMax(a, b)
