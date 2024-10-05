from random import randint
def main():
    while True:
        x = input("How many players? (1-4) ")
        if x == "2":
            playerCount2()
        elif x == "3":
            playerCount3()
        elif x == "4":
            playerCount4()
        else:
            pass


def playerCount2():
    print("Welcome to this game of Pig")
    xA = rollFunction(0,"Player 1")
    print(f"Player 1 your score after the 1st round is: {xA}")
    xB = rollFunction(0,"Player 2")
    print(f"Player 2 your score after the 1st round is: {xB}")
    yA = rollFunction(xA,"Player 1")
    print(f"Player 1 your score after the 2nd round is: {yA}")
    yB = rollFunction(xB,"Player 2")
    print(f"Player 2 your score after the 2nd round is: {yB}")
    zA = rollFunction(yA,"Player 1")
    print(f"Player 1 your score after the 3rd round is {zA}")
    zB = rollFunction(yB,"Player 2")
    print(f"Player 2 your score after the 3rd round is {zB}")

def playerCount3():
    print("Welcome to this game of Pig")
    xA = rollFunction(0,"Player 1")
    print(f"Player 1 your score after the 1st round is: {xA}")
    xB = rollFunction(0,"Player 2")
    print(f"Player 2 your score after the 1st round is: {xB}")
    xC = rollFunction(0,"Player 3")
    print(f"Player 3 your score after the 1st round is: {xC}")
    yA = rollFunction(xA,"Player 1")
    print(f"Player 1 your score after the 2nd round is: {yA}")
    yB = rollFunction(xB,"Player 2")
    print(f"Player 2 your score after the 2nd round is: {yB}")
    yC = rollFunction(xC, "Player 3")
    print(f"Player 3 your score after the 2nd round is: {yC}")
    zA = rollFunction(yA,"Player 1")
    print(f"Player 1 your score after the 3rd round is {zA}")
    zB = rollFunction(yB,"Player 2")
    print(f"Player 2 your score after the 3rd round is {zB}")
    zC = rollFunction(yC, "Player 3")
    print(f"Player 3 your score after the 3rd round is {zC}")

def playerCount4():
    xA = rollFunction(0,"Player 1")
    print(f"Player 1 your score after the 1st round is: {xA}")
    xB = rollFunction(0,"Player 2")
    print(f"Player 2 your score after the 1st round is: {xB}")
    xC = rollFunction(0,"Player 3")
    print(f"Player 3 your score after the 1st round is: {xC}")
    xD = rollFunction(0, "Player 4")
    print(f"Player 4 after the ist round your score is: {xD} ")
    yA = rollFunction(xA,"Player 1")
    print(f"Player 1 your score after the 2nd round is: {yA}")
    yB = rollFunction(xB,"Player 2")
    print(f"Player 2 your score after the 2nd round is: {yB}")
    yC = rollFunction(xC, "Player 3")
    print(f"Player 3 your score after the 2nd round is: {yC}")
    yD = rollFunction(xD, "Player 4")
    print(f"Player 4 your score after the 2nd round is: {yD}")
    zA = rollFunction(yA,"Player 1")
    print(f"Player 1 your score after the 3rd round is {zA}")
    zB = rollFunction(yB,"Player 2")
    print(f"Player 2 your score after the 3rd round is {zB}")
    zC = rollFunction(yC, "Player 3")
    print(f"Player 3 your score after the 3rd round is {zC}")
    zD = rollFunction(yD, "Player 4")
    print(f"Player 4 your score after the 3rd round is: {zD}")


def rollFunction(cs, Player):
    currentScore = cs
    roundscore = 0
    while True:
        roll = randint(1,6)
        decision = input(f"{Player} Do you want to roll or not? (yes/no) ")
        if decision == "yes":
            print(f"you've rolled a: {roll}")
            roundscore = roundscore + roll
            print(f"roundscore is: {roundscore}")
            print(f"Saved score is: {currentScore}")
        elif decision == "no":
            currentScore = currentScore + roundscore
            return currentScore
        if currentScore + roundscore >= 50:
            print("you won the game")
            break
        if roll == 1:
            print("Youve rolled a 1 your turn is over")
            return currentScore

main()
