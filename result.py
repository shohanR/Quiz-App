class Result:
    def __init__(self, playerDetails):
        self.playerDetails = playerDetails
        self.userName = list(playerDetails.keys())

    def scoreInfo(self):
        if len(self.userName)==2:
            print(f"{self.userName[0]} got {self.playerDetails[self.userName[0]]} points\nAnd {self.userName[1]} got {self.playerDetails[self.userName[1]]} points")

            if self.playerDetails[self.userName[0]]>self.playerDetails[self.userName[1]]:
                print(f"The winner is {self.userName[0]}")
            elif self.playerDetails[self.userName[0]] == self.playerDetails[self.userName[1]]:
                print("It's a tie!")
            else:
                print(f"The winner is {self.userName[1]}")
        else:
            print(f"{self.userName[0]} got {self.playerDetails[self.userName[0]]} points")
    