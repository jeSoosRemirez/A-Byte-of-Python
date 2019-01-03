def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count


print(total(10, 1, 2, 3, vegetables=50, fruits=100))
# * tuple
# ** dictionary
# [key] - так як keywords словник, то на 6 рядку ми вказуємо ключ, щоб значення сохранялося не в пусту комірку
