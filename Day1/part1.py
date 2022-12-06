import time
start = time.perf_counter()
f = open('./input.txt', 'r')
mTotal = 0
currTotal = 0 
for l in f:
    if l == '\n':
        if currTotal > mTotal:
            mTotal = currTotal
        currTotal = 0
    else:
        currTotal += int(l)
print(f"{mTotal}")
print(f"Time taken: {time.perf_counter() - start}")
