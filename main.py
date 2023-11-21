import random

# dictionary to store Q/A
questionAnswer = dict()
flag = 1
# taking Q/A until user wants to proceed to the game
while flag==1:
    temp=0
    question = input("Enter your question: ").strip()
    question = question.capitalize()
    # handling repeated question
    if question in questionAnswer.keys():
        print("This question has already been given.\nWould you like to continue adding question? If yes, enter 1. Otherwise enter 0.")
        while True:    
            try:
                flag=int(input())
            except:
                print("Wrong input type! Enter 1, or, 0 only! ")
            else:
                if flag<0 or flag>1:
                    print("Wrong input type! Enter 1, or, 0 only! ")
                    continue
                else:
                    if flag==1:
                        temp=1
                    break

    # checking users choice
    if temp==1:
        continue
    else:
        if flag==0:
            break
        else:
            answer = input("Enter your answer: ").strip()
            # adding Q as keys and A as values
            questionAnswer[question] = answer
            print("To add question please enter 1, otherwise 0.")
            # handling input type errors
            while True:
                temp = 0
                try:
                    flag = int(input())
                except:
                    print("Please enter 1 or 0 (integer) only!")
                    temp = 1
                if temp==0:
                    if flag<0 or flag>1:
                        print("Please enter 1 or 0 (integer) only!")
                        continue
                    else:
                        break


# selecting game type
print("Proceed to the game as a \n1) Solo Player\n2)Multiplayer-(2)\nEnter 0 to terminate the game!")
# handling type error
while True:
    try:
        player = int(input())
    except:
        print("You have provided wrong type of input. Enter 1, 2, or 0.")
    else:
        # handling wrong integer type error
        if player==0:
            print("Terminating the game...")
            break
        elif player<0 or player>2:
            print("Wrong input! Please enter only 1, 2, or 0!")          
        else:
            flag = 1
            playerDetails = dict()
            temp = 0
            while temp!=player:
                playerName = input(f"Enter the user name of player{temp+1}: ").strip()
                playerName = playerName.lower()
                if playerName in playerDetails:
                    print("Player is already present. Try again!")
                else:
                    playerDetails[playerName] = 0
                    temp += 1
            print("Proceeding to the game...")
            break

if flag==0:
    print("\n!---------Game End!---------")
else:
    while flag==1:
        if len(playerDetails.keys())==2:
            print("Who will play the game first?")
            temp = input("Username: ").strip()
            if temp not in playerDetails.keys():
                print("Username not found! To try again enter 1, otherwise enter 0 to terminate the game: ")
                while True:
                    try:
                        flag = int(input())
                    except:
                        print("Wrong input! Please enter 1, or 0: ")
                    else:
                        if flag<0 or flag>1:
                            print("Please enter 1, or 0 only! ")
                        else:
                            break
        if flag==0:
            break
        ques = random.choice(list(questionAnswer.keys()))
        print(ques)
        ans = input("Answer: ").strip()
        
        if questionAnswer[ques]==ans:
            print(f"Correct answer! 5 points to {temp}")
            playerDetails[temp] = playerDetails[temp] + 5
        else:
            print("Wrong answer!")
        
        print("To continue the game, enter 1. Enter 0 to terminate the game! ")
        while True:
            try:
                flag = int(input())
            except:
                print("Wrong input! Please enter 1, or 0: ")
            else:
                if flag<0 or flag>1:
                    print("Please enter 1, or 0 only! ")
                else:
                    break
userName = list(playerDetails.keys())
print("Here is the result: ")
if len(playerDetails.keys())==2:
    print(f"{userName[0]} got {playerDetails[userName[0]]} points\n and {userName[1]} got {playerDetails[userName[1]]} points")
else:
    print(f"{userName[0]} got {playerDetails[userName[0]]} points")

if playerDetails[userName[0]]>playerDetails[userName[1]]:
    print(f"The winner is {userName[0]}")
else:
    print(f"The winner is {userName[1]}")
