score1=int(input("Player 1 Enter Your Number:"))
score2=int(input("Player 2 Enter Your Number:"))

Player1Win: int = 0
Player2Win: int = 0

Player1scoreboard = 0
Player2scoreboard = 0

print("Player 1 Number was:", score1)
print("Player 2 Number was:", score2)
print("The Winner is:")

if score1 > score2:
    Player1scoreboard = Player1Win + 1
    print("Player 1 Wins")
elif score1 < score2:
    Player2scoreboard = Player2Win + 1
    print("Player 2 Wins")
if score1 == score2:
    print("Tie")
print("The score is:\n", "Player1:", Player1scoreboard, '\n', "Player2:", Player2scoreboard)

def loop():
    restart = input("Would you like to play again:")
    if restart == "yes":
        loop()
    if restart == "no":
        print("Thank you for playing")
loop()




