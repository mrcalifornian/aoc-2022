input = open(".\input.txt")

def turnMe(rival, me):
    if me == "X":
        if rival == "A":
            return "C"
        elif rival == "B":
            return "A"
        elif rival == "C":
            return "B"
    elif me == "Y":
        if rival == "A":
            return "A"
        elif rival == "B":
            return "B"
        elif rival == "C":
            return "C"
    elif me == "Z":
        if rival == "A":
            return "B"
        elif rival == "B":
            return "C"
        elif rival == "C":
            return "A"


def score(L):
    if L == "A":
        return 1
    elif L == "B":
        return 2
    elif L == "C":
        return 3


def check(me):
    if me == "X":
        return 0
    elif me == "Y":
        return 3
    elif me == "Z":
        return 6


total = 0

for i in input:
    rival = i[0]
    me = turnMe(rival, i[2])

    total += check(i[2]) + score(me)

print(total)
