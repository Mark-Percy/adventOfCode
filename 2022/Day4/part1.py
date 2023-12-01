from operator import itemgetter

def changeIntList(l) :
    returnList = []
    for i in l:
        new = i.split('-')
        for j in range(len(new)):
            new[j] = int(new[j])
        returnList.append(new)
    return returnList


f = open('input.txt', 'r')
arealist = []
count = 5
for l in f:
    if count != 10:
        count += 1
        line = l[:-1]
        arealist += changeIntList(line.split(','))

sortedAreaList = sorted(arealist, key=itemgetter(0))
print(sortedAreaList)

nums = 0
p1 = 0
while p1 < len(sortedAreaList) -1:
    p2 = p1+1
    while p2 < len(sortedAreaList):
        print(sortedAreaList[p1], sortedAreaList[p2])
        if (sortedAreaList[p1][1] > sortedAreaList[p2][0] and sortedAreaList[p1][1] > sortedAreaList[p2][1]):
            nums+= 1
        else: 
            break
        p2 += 1
    p1+=1
print(nums)
