shoplist = ['apple', 'rice', 'ketchup', 'meat']
pre_words = 'My shop list looks like this:'

print('I should do', len(shoplist), 'purchases')


def myList():
    print(pre_words, end=' ')
    for item in shoplist:
        print(item, end=' ')
    print()


myList()

print('So i want to buy salt')
shoplist.append('salt')
pre_words = 'And now my shop list looks ike this:'
myList()

print('I need to sort my list...')
shoplist.sort()
pre_words = 'Sorted shop list looks like this:'
myList()

print('The first, that i want to buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I buy', olditem)
pre_words = 'And now my shop list is:'
myList()
