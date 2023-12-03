total = 0

digitStrings = {"oneight":"18",
                "twone":"21",
                "threeight":"38",
                "eighthree":"83",
                "eightwo":"82",
                "one":"1",
                "two":"2",
                "three":"3",
                "four":"4",
                "five": "5",
                "six": "6",
                "seven": "7",
                "eight": "8",
                "nine": "9"}
def switchNumbers(garbStr):
    for key in digitStrings.keys():
        garbStr = garbStr.replace(key, digitStrings[key])
    return garbStr

with open("./input.txt") as f:
    for l  in f:
        l = switchNumbers(l) # Remove for solution to task1
        numlist = list(filter(lambda i: i.isdigit(), l))
        length = len(numlist)
        firstNum = numlist[0]
        secondnum = 0
        
        if(length == 1):
            secondnum = numlist[0]
        else:
            secondnum = numlist[length-1]
        total += int(firstNum + secondnum)
print(total)