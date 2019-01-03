def func(a, b=5, c=10):
    print('a = ', a, ', b = ', b, ', c = ', c)


func(2, 3)
func(c=8, a=3)
func(a=4, b=4)
print('You can not call func without param a')
