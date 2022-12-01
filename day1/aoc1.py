text = open("input.txt")

num = 0
myList = []
max = 0

for i in text:
    if i == "\n":
        myList.append(num)
        num = 0
    else:
        num += int(i)


for i in myList:
    if i > max:
        max = i

print(max)
