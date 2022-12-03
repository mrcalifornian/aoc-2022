input = open(".\day3\input.txt")
total = 0


def splits(str):
    end = int(len(str))
    half = int(len(str)/2)
    first = str[:half]
    second = str[half:end]

    for i in first:
        for l in second:
            if i == l:
                return i


def findNum(str):
    if str.isupper():
        return ord(str)-38
    elif str.islower():
        return ord(str)-96


for i in input:
    total += findNum(splits(i))
    print(findNum(splits(i)), splits(i))

print(total)
