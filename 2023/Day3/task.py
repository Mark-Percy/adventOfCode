
def addToList(strList, line):
    strList.append(line)
    return strList

def getAllSpecialChars(line, lineNum, specialCharsList, specialCharDic):
    specialCharIndexs = []
    for key, letter in enumerate(line):
        if not letter.isdigit() and letter != '.':
            if letter not in specialCharsList: specialCharsList.append(letter)
            specialCharIndexs.append(key)
    specialCharDic[lineNum] = specialCharIndexs
            
    return specialCharsList, specialCharDic

def MakeListFromFile(fileName, specialCharsList, specialCharDic):
    newList = []
    lineNum = 0
    with open(fileName) as f:
        for l in f:
            l = l.replace('\n', '')
            specialCharsList, specialCharDic = getAllSpecialChars(l, lineNum, specialCharsList, specialCharDic)
            addToList(newList, l)
            lineNum += 1
    return [newList, specialCharsList, specialCharDic]

def checkLine(currLine, lineCheck):
    nl = []
    for n in lineCheck:
        for k, ind in currLine.items():
            for indexitem, indexs in enumerate(ind):
                if n in indexs:
                    nl.append(k)
                    currLine[k].pop(indexitem)
    return nl, currLine
    
def makeLineDic(line):
    lineDic = {}
    digitarr = []
    numString = ''

    for key, char in enumerate(line):
        if char.isdigit():
            numString += char
            digitarr.append(key)
        elif digitarr != []:
            digitarr.insert(0, digitarr[0] - 1)
            digitarr.append(digitarr[len(digitarr) - 1] + 1)
            if lineDic.get(numString): lineDic[numString].append(digitarr)
            else: lineDic[numString] = [digitarr]

            digitarr = []
            numString = ''
    if(numString != '' and digitarr != []):
        digitarr.insert(0, digitarr[0] - 1)
        digitarr.append(digitarr[len(digitarr) - 1] + 1)
        if lineDic.get(numString): lineDic[numString].append(digitarr)
        else: lineDic[numString] = [digitarr]
    return lineDic


def main():
    response = MakeListFromFile('input.txt', [], {})
    fileList = response[0]
    specialChars = response[1]
    specialCharsDic = response[2]
    fullListOfNums = []
    sum = 0
    for k, i in enumerate(fileList):
        lineDic = makeLineDic(i)
        if(k != 0):
            resp = checkLine(lineDic, specialCharsDic[k-1])
            lineDic = resp[1]
            fullListOfNums.extend(resp[0])
        resp = checkLine(lineDic, specialCharsDic[k])
        fullListOfNums.extend(resp[0])
        lineDic = resp[1]
        if k != len(fileList) - 1:
            resp = checkLine(lineDic, specialCharsDic[k+1])
            fullListOfNums.extend(resp[0])
            lineDic = resp[1]
    for i in fullListOfNums:
        sum += int(i)
    print(sum)

main()