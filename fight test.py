import random
witch_health = 15

player_attack = int(input(print("enter a number 1-7")))
witch_attack = random.randint(1,7)
print(witch_attack)

if player_attack > witch_attack:
    witch_health = witch_health - player_attack
    print("witch took", player_attack, "the witches health is now", witch_health)





