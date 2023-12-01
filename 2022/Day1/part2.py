import time

start = time.perf_counter()
f = open('./input.txt', 'r')
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
print(f"Time taken: {time.perf_counter() - start}")