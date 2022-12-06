import time
import math
from string import ascii_letters
start = time.perf_counter()
f = open('./input.txt', 'r')
#set up points
numOfPoint = 1
letter_val = {}
for c in ascii_letters:
    letter_val[c] = numOfPoint
    numOfPoint +=1

totalPoints = 0
for l in f:
    lengthOfLine = math.floor(len(l) /2)
    ll = []
    letterC = 0
    for c in l:
        if letterC == lengthOfLine:
            if c in ll:
                totalPoints += letter_val[c]
                break
        else:
            letterC += 1
            ll.append(c)
print(totalPoints)
print(f"Time taken: {time.perf_counter() - start}")