input = open("./day5/input.txt")

endList = ""

A = ["T", "D", "W", "Z", "V", "P"]
B = ["L", "S", "W", "V", 'F', 'J', 'D']
C = ["Z", "M", "L", "S", 'V', "T", 'B', 'H']
D = ['R', 'S', 'J']
E = ['C', 'Z', 'B', 'G', 'F', 'M', 'L', 'W']
F = ["Q", 'W', 'V', 'H', 'Z', 'R', 'G', 'B']
G = ['V', 'J', 'P', 'C', 'B', 'D', 'N']
H = ["P", "T", "B", "Q"]
I = ["H", "G", "Z", "R", "C"]


def returnList(num):
    if num == 1:
        return A
    if num == 2:
        return B
    if num == 3:
        return C
    if num == 4:
        return D
    if num == 5:
        return E
    if num == 6:
        return F
    if num == 7:
        return G
    if num == 8:
        return H
    if num == 9:
        return I


def startIn(list, count):
    start = len(list)-1
    return start-(count-1)


for i in input:
    a, b, c, d, e, f = i.split(" ")

    moving = int(b)
    fromList = returnList(int(d))

    toList = returnList(int(f))

    start = startIn(fromList, moving)

    data = fromList[start:]
    data.reverse()
    toList.extend(data)
    del fromList[start:]

for i in range(9):
    endList += returnList(i+1)[-1]

print(endList)
