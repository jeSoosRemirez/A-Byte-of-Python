zoo = ('snake', 'tiger', 'lion')
print('The number of animal - ', len(zoo))
new_zoo = 'monkey', 'camel', 'goat', zoo
print('The number of cage -', len(zoo))
print('All animals in zoo:', new_zoo)
print('Animals from old zoo:', new_zoo[3])
print('The last of animals that been re-road to new zoo is', new_zoo[3][2])
print('The number of all animals -', len(new_zoo) - 1 + len(new_zoo[3]))
