import time
start = time.perf_counter()
f = open('./input.txt', 'r')
me = {'R':1,'P':2,"S":3}
wins = {'A':'P','B':'S','C':'R'}
draws = {'A':'R','B':'P','C':'S'}
loss = {'A':'S','B':'R','C':'P'}
points = 0
for l in f:
    if l[2] == 'Z':
        points += (me[wins[l[0]]] + 6)
    elif l[2] == 'Y':
        points += (me[draws[l[0]]] + 3)
    else:
        points += me[loss[l[0]]]
print(points)
print(f"Time taken: {time.perf_counter() - start}")