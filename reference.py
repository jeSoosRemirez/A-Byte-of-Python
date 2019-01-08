print("Simple assignment")
shoplist = ["apple", "mango", "carrot", "banana"]
mylist = shoplist

del shoplist[0]

print("shoplist:", shoplist)
print("mylist:", mylist)

print("Copying by full cut")
mylist = shoplist[:] # создаём копию путём полной вырезки
del mylist[0]

print("shoplist:", shoplist)
print("mylist:", mylist)
# Обратите внимание, что теперь списки разные

