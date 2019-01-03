def maximum(first_num, second_num):
    if first_num > second_num:
        return first_num
    elif first_num == second_num:
        return print('First number = second number (', first_num, '=', second_num, ')')
    else:
        return second_num


first = input('Pls, type some number: ')
second = input('Pls, type some number again: ')
maximum(first, second)
