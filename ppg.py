import random, os, string
os.system("cls" or "clear")
item = 1
i = int(input("How Many Want You:"))
character = string.printable
while i >= item:
    a = ''.join(random.sample(character,8))
    print(" Password {0} is :{1}".format(item,a))
    item += 1
