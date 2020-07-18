from random import randint

t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = ["heads", "tails"]
b = ["bat" , "bowl"]
computer = t[randint(0, 9)]
computer1 = a[randint(0,1)]
computer3 = b[randint(0,1)]
player = False
run = 0
run1 = 0
choice = 0
bat = 0
ball = 0
choice1 = 0
choice = input("enter your choice 1) heads 2)tails")
print("server choice is ", computer1)
if choice == computer1:
     choice1 = input("player won the toss and choose to: 1)bat 2)ball")
     print("choice is ", choice1)
     if choice1 == b[0]:
        while player == False:
            player = int(input("player is batting"))
            print("computer  is bowling:", computer)
            if player == computer:
                print("you are out")
                print("player total score is", run)
                print("computer has to score this much of runs to win", run)
                break
            else:
                run = run + player
                print(run)
                player = False
                computer = t[randint(0, 9)]
     player = False
        # player is bowling after batting first
     while player == False:
            player = int(input("player is bowling:"))
            print("computer is batting :", computer)
            if player == computer:
                print("you are out")
                if run > run1:
                    print("player wins")
                else:
                    print("match tie")
                break
            elif run1 > run:
                print("computer wins")
            else:
                run1 = run1 + computer
                print(run1)
                player = False
                computer = t[randint(0, 9)]

     else:
        # player is bowling after winning toss
        while player == False:
            player = int(input("player is bowling:"))
            print("computer is batting :", computer)
            if player == computer:
                print("you are out")
                print("total run of computer is", run1)
                print("player has to score this much of run to win:", run1)

            else:
                run1 = run1 + computer
                print(run1)
                player = False
                computer = t[randint(0, 9)]
        # player is batting after bowling 2nd innings
        while player == False:

            player = int(input("player is batting:"))
            print("computer  is bowling :", computer)
            if player == computer:
                print("you are out")
            elif run < run1:
                print("computer wins")
            elif run > run1:
                print("player wins")

            break
            if player != computer:
                run = run + player
                print(run)
            player = False
            computer = t[randint(0, 9)]

else:
    print("opponent decide")
    computer3 = b[randint(0,1)]
    print(computer3)
    if computer3 == b[0]:
        # computer choosen batting by winning toss
        while player == False:

            player = int(input("player bowling starts"))
            print("computer is batting :", computer)
            if player == computer:
                print("you are out")
                print("computer total score is", run1)

            else:
                run1 = run1 + computer
                print(run1)
                player = False
                computer = t[randint(0, 9)]

        # computer is bowling after batting first
    player = False
    while player == False:
        player = int(input("player is batting:"))
        print("computer is bowling :", computer)
        if player == computer:
            print("you are out")
            if run < run1:
                print("computer wins")
            elif run > run1:
                print("player wins")
            else:
                print("match tie")
            break
        elif player != computer:
            run = run + player
            print(run)
            player = False
            computer = t[randint(0, 9)]
    else:
        # computer is bowling after winning toss
        while player == False:
            player = int(input("player is batting :"))
            print("computer is bowling :", computer)
            if player == computer:
                print("you are out")
                print("total run of player is", run1)


            else:
                run = run + player
                print(run)
                player = False
                computer = t[randint(0, 9)]
        # computer is batting after bowling 2nd innings
    while player == False:
        player = int(input("player is bowling:"))
        print("computer is batting :", computer)
        if player == computer:
            print("you are out")
            if run < run1:
                print("computer wins")
            elif run > run1:
                print("player wins")
            else:
                print("match tie")
            break
        else:
            run1 = run1 + computer
            print(run1)
            player = False
            computer = t[randint(0, 9)]

print("thanks for playing")

