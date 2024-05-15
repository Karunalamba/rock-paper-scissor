import random
l=["rock","paper","scissor"]
while True:
    ccount=0
    ucount=0
    uc=int(input('''
    Game start........
    1 Yes 
    2 No | Exit 
            '''))
    if uc==1:
        for a in range(1,6):
            userinput=int(input('''
1 rock
2 scissor
3 paper
            '''))
            if userinput==1:
                uchoice="rock"
            elif userinput==2:
                uchoice="scissor"
            elif userinput==3:
                uchoice="paper"
            cchoice=random.choice(l)
            print(uchoice)
            print(cchoice)

            if cchoice==uchoice:
                print("computer value",cchoice)
                print("user value",uchoice)
                print("Game draw")
                ccount=ccount+1
                ucount=ucount+1
            elif (uchoice=="rock" and cchoice=="scissor") or (uchoice=="paper" and cchoice=="rock") or (uchoice=="scissor" and cchoice=="paper"):
                print("computer value",cchoice)
                print("user value",uchoice)
                print("You win")
                ucount=ucount+1
            else:
                print("computer value", cchoice)
                print("user value", uchoice)
                print("Computer win")
                ccount=ccount+1




    else:
        break



