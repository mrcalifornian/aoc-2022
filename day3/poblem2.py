input = open(".\day3\input.txt")
total = 0


def findSame(first, second, third):
    for i in first:
        for n in second:
            for z in third:
                if i == n == z:
                    return i


def findNum(str):
    if str.isupper():
        return ord(str)-38
    elif str.islower():
        return ord(str)-96


line = input.readlines()
for i in range(len(line)):
    if (i+3) % 3 == 0:
        total += findNum(findSame(line[i], line[i+1], line[i+2]))
        print(i, i+1, i+2)
        print(findSame(line[i], line[i+1], line[i+2]))

print(total)
