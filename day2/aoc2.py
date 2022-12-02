# "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors.Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

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

# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.


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
