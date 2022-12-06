from string import ascii_letters
import time
start = time.perf_counter()
f = open('./input.txt', 'r')
#set up points
numOfPoint = 1
letter_val = {}
for c in ascii_letters:
    letter_val[c] = numOfPoint
    numOfPoint +=1
totalPoints = 0
groupP = []
count = 0
for l in f:
    line = l[:-1]
    if len(groupP) < 3:
        groupP.append(line)
    if len(groupP) == 3:
        count += 1
        for g in groupP[0]:
            if g in groupP[1] and g in groupP[2]:
                totalPoints += letter_val[g]
                break
        groupP = []
print(totalPoints)
print(f"Time taken: {time.perf_counter() - start}")