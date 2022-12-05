f = open('./input.txt', 'r')
#Task 1
# me = {"X":1,'Y':2,"Z":3}
# wins = ['AY',"BZ",'CX']
# draws = ['AX','BY','CZ']
# points = 0
# for l in f:
#     points += me[l[2]]
#     test = f"{l[0]}{l[2]}"
#     if test in wins:
#         points += 6
#     elif test in draws:
#         points += 3
# print(points)

#
#Task 2
#

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