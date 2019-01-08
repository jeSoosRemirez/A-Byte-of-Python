shoplist = ['apple', 'banana', 'carrot', 'mango']
name = 'Swaroop'

# Операция индексирования
print('0 item -', shoplist[0])
print('1 item -', shoplist[1])
print('2 item -', shoplist[2])
print('3 item -', shoplist[3])
print('-1 item -', shoplist[-1])
print('-2 item -', shoplist[-2])
print('Sign 0 -', name[0])

# Вырезка из списка
print('Items from 1 to 3:', shoplist[1:3])
print('Items from 2 to the end:', shoplist[2:])
print('Items from 1 to -1:', shoplist[1:-1])
print('Items from begun to the end:', shoplist[:])
print('Signs from 1 to 3:', name[1:3])
print('Signs from 2 to the end:', name[2:])
print('Signs from 1 to -1:', name[1:-1])
print('Signs from begun to the end:', name[:])
