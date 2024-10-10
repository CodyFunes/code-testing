import time
import keyboard





party_size = int(input("enter party size"))

player_health = 5
witch_health = 15

if party_size >= 2:
    party_health = player_health + 5
    print("Your partys health is", party_health)
elif party_size < 2:
    print("your players health is", player_health)
time.sleep(1)
print("press any key to continue")
input()

print("the wiches health is", witch_health)
