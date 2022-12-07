input = open("./day6/input.txt")

text = input.readline()


# print(len(text))

for i in range(len(text)):
    myList = []
    for x in range(14):
        myList.append(text[i+x])

    if len(set(myList)) == 14:
        print(text[:i+4])
        print(i+14)
        break
