input = open("./day4/input.txt")

count = 0


def numList(start, end):
    myList = []
    for i in range(start, end+1):
        myList.append(i)
    return myList


for i in input:
    first, second = i.split(",")
    firstStart, firstEnd = first.split("-")
    secondStart, secondEnd = second.split("-")

    firstList = numList(int(firstStart), int(firstEnd))
    secondList = numList(int(secondStart), int(secondEnd))

    if set(firstList).issubset(secondList) or set(secondList).issubset(firstList):
        count += 1

print(count)
