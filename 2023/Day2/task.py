def calculatePower(game):
    power = 1
    for val in game.values():
        power *= val
    return power

total = 0
totalPower = 0

test = {'red': 12,'blue': 14, 'green': 13}
with open("input.txt") as f:
    for l in f:
        l = l.replace("\n", "")
        gamenum = int("".join(list(filter(lambda i: i.isdigit(), l.split(":")[0]))))
        game = {'red':0, 'blue': 0, 'green':0}

        gamesets = l.split(":")[1].split("; ")
        sets = [sets.split(", ") for sets in gamesets]
        for sett in sets:
            for pick in sett:
                split = pick.lstrip().split(" ")
                color = split[1]
                number = int(split[0])
                if(game[color] < number): game[color] = number
        totalPower += calculatePower(game)
        possible = True
        for key in game.keys():
            if(game[key] > test[key]):
                possible = False
        if(possible): total += gamenum

print("Total: ", total) # Task 1
print("Total Power: ", totalPower) # Task 2