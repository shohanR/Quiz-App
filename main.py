questionAnswer = dict()
flag = 1

while True:
    question = input("Enter your question: ").strip()
    question = question.capitalize()
    if question in questionAnswer:
        print("This question has already been given.\nWould you like to continue adding question? If yes, enter 1. Otherwise enter 0.")
        flag = int(input())
    if flag==0:
        break
    answer = input("Enter your answer: ").strip()
    questionAnswer[question] = answer
    print("To add question please enter 1, otherwise 0.")
    while True:
        temp = 0
        try:
            flag = int(input())
        except:
            print("Please enter 1 or 0 (integer) only!")
            temp = 1
        if temp==0:
            if flag<2:
                break
            else:
                print("Please enter 1 or 0 only!")

    if flag==0:
        break

print("Proceed to the game as a \n1) Solo Player\n2)Multiplayer-(2)")
try:
    player = int(input())
except:
    print("You have provided wrong type of input. Terminating the game.")
else:
    playerDetails = dict()
    flag = 0
    while flag!=player:
        temp = input(f"Enter the user name of player{flag+1}: ").strip()
        if temp in playerDetails:
            print("Player is already present. Try again!")
        else:
            playerDetails[temp] = None
            flag += 1
    print(playerDetails)
