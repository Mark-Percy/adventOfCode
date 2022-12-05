f = open('./input.txt', 'r')
# mTotal = 0
# currTotal = 0 
# for l in f:
#     if l == '\n':
#         if currTotal > mTotal and currTotal < 68878:
#             mTotal = currTotal
#         currTotal = 0
#     else:
#         currTotal += int(l)

# print(f"{mTotal}")


threeTop = [0,0,0]
currTotal = 0 
for l in f:
    if l == '\n':
        added = 0
        for i in range(len(threeTop)):
            totalToTest = currTotal
            if currTotal > threeTop[i] and added == 0:
                threeTop.insert(i, currTotal)
                threeTop.pop()
                added = 1
        currTotal = 0
    else:
        currTotal += int(l)

print(f"{threeTop} :{sum(threeTop)}")
