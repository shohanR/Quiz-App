questionAnswer = dict()
flag = 1

while True:
    question = input("Enter your question: ")
    question = question.capitalize()
    if question in questionAnswer:
        print("This question has already been given.\nWould you like to continue adding question? If yes, enter 1. Otherwise enter 0.")
        flag = int(input())
    if flag==0:
        break
    answer = input("Enter your answer: ")
    questionAnswer[question] = answer
    print("To add question please enter 1, otherwise 0.")
    flag = int(input())
    if flag==0:
        break

print("Proceed to the game as a \n1) Solo Player\n2)Multiplayer-(2)")
try:
    player = int(input())
except:
    print("You have provided wrong type of input. Terminating the game.")
else:
    print(player)
