import time
start = time.perf_counter()
f = open('./input.txt', 'r')
me = {"X":1,'Y':2,"Z":3}
wins = ['AY',"BZ",'CX']
draws = ['AX','BY','CZ']
points = 0
for l in f:
    points += me[l[2]]
    test = f"{l[0]}{l[2]}"
    if test in wins:
        points += 6
    elif test in draws:
        points += 3
print(points)
print(f"Time taken: {time.perf_counter() - start}")