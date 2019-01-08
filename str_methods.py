name = "Swaroop"

if name.startswith("Swa"):
    print("Да, строка начинаеться на Swa")

if "a" in name:
    print("Да, строка содержит букву 'a'")

if name.find("war"):
    print("Да, в строке есть 'war'")

delimiter = "_*_"

mylist = ["Japan", "USA", "Russia", "Ukraine"]
print(delimiter.join(mylist))
