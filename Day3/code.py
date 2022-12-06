
import math
from string import ascii_letters


f = open('./input.txt', 'r')

#set up points
numOfPoint = 1
letter_val = {}
for c in ascii_letters:
    letter_val[c] = numOfPoint
    numOfPoint +=1
#
# Part 1
#
# totalPoints = 0
# for l in f:
#     lengthOfLine = math.floor(len(l) /2)
#     ll = []
#     letterC = 0
#     for c in l:
#         if letterC == lengthOfLine:
#             if c in ll:
#                 totalPoints += letter_val[c]
#                 break
#         else:
#             letterC += 1
#             ll.append(c)
# print(totalPoints)

#
#Part 2
#

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