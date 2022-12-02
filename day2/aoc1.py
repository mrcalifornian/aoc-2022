input = open(".\input.txt")


def turnMe(me):
    if me == "X":
        return "A"
    elif me == "Y":
        return "B"
    elif me == "Z":
        return "C"


def score(L):
    if L == "A":
        return 1
    elif L == "B":
        return 2
    elif L == "C":
        return 3


def check(rival, me):
    if me == rival:
        return 3
    elif me == "A" and rival == "C":
        return 6
    elif me == "C" and rival == "B":
        return 6
    elif me == "B" and rival == "A":
        return 6
    else:
        return 0


total = 0

for i in input:
    rival = i[0]
    me = turnMe(i[2])

    total += check(rival, me) + score(me)

print(total)
