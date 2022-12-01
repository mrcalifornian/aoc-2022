text = open("input.txt")

num = 0
myList = []
max = 0
sum = 0
index = 0

for i in text:
    if i == "\n":
        myList.append(num)
        num = 0
    else:
        num += int(i)


for n in range(3):
    for i in range(len(myList)):
        if myList[i] > max:
            print(f"max is {myList[i]}, {i}")
            max = myList[i]
            index = i
    del myList[index]
    sum += max
    max = 0

print(sum)
