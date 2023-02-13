import random
#Rock-Paper-Scissor Game

print("""Instructions:
1: Rock
2: Paper
3: Scissor
9: Start
0: Stop""") #if the user does not enter the given keys
#a while loop will kick in which will keep on running unless the user enters the correct keys 


moves = ["Rock","Paper","Scissor"]

state = int(input("""Enter 9 to Start the Game
Ready to Start the game: """))

if state!=9:
    while state!=9: #wrong key entered
        state = int(input("""Wrong Key!!!
        Enter 9 to Start the game
        Ready to Start the game: """))

if state==9:
    while state!=0:
        my_move = int(input("""Choose your move - 1: Rock ; 2: Paper ; 3: Scissor
        :"""))
        if my_move not in [1,2,3]: #wrong key entered
            while my_move not in [1,2,3]:
                my_move = int(input("""Wrong Key!!!
                Choose your move - 1: Rock ; 2: Paper ; 3: Scissor
                :"""))
                if my_move in [1,2,3]: #correct key entered
                    break

        ai_move = random.randint(1,3)
        print("You chose ",moves[my_move-1])
        print("The AI chose",moves[ai_move-1])
        if my_move==ai_move:
            print("It's a Draw!!")
        else:
            if my_move==1 and ai_move==2:
                print("The AI Won!!")
            elif my_move==1 and ai_move==3:
                print("You Won!!")
            elif my_move==2 and ai_move==1:
                print("You Won!!")
            elif my_move==2 and ai_move==3:
                print("The AI Won!!")
            elif my_move==3 and ai_move==1:
                print("The AI Won!!")
            elif my_move==3 and ai_move==2:
                print("You Won!!")
        
        state = int(input("""Enter 9 to Keep Playing or 0 to Stop
        Want to Keep Playing: """))

        if state not in [0,9]: #wrong key entered
            while state!=9 or state!=0:
                state = int(input("""Wrong Key!!!
                Enter 9 to Keep Playing or 0 to Stop
                Want to Keep Playing: """))
                if state==9 or state==0: #correct key entered
                    break

print("---Thank You---")
