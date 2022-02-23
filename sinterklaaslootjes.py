from fileinput import filename
import random, json

names1 = []
names2 = []
lootjes = {}
lootje = {}
filepath = (r"C:\Projecten\Software Dev\Mapje 9\file-remember\data\lootjes.json")
with open(filepath, "w") as file:
    pass

players = int(input("Hoeveel mensen doen mee met lootjes trekken? "))

for i in range(players):
    name = input("Naam "+str(i+1)+": ")
    if name in names1:
        print("Deze naam zit er al in.")
    else:
        names1.append(name)
        names2.append(name)

while names1:
    name1 = names1[random.randint(0, len(names1) - 1)]
    name2 = names2[random.randint(0, len(names2) - 1)]

    if name1 == name2:
        if len(names1) == 1:
            print(name1 + " is helaas alleen.")
            break
    else:
        print(name1 + " heeft " + name2 + " als lootje getrokken.\n")
        lootje[name1] = name2
        names1.remove(name1)
        names2.remove(name2)
with open(filepath, "a") as outfile:
    json.dump(lootje, outfile)