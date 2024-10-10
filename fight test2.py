import random
witch_health = 15
player_health = 10
witch_attack = random.randint(-2,7)
player_attack = int(input("Enter your attack power -2,7:"))

def loop():

    while player_health != 0 or witch_health != 0:
        if player_health == 0 or witch_health == 0:
            exit()

        if player_attack >= 7:
            print("please enter a number -2-7")

            print("The witches attack was", witch_attack)



            if witch_attack <= -2:
                witch_health = player_attack + witch_attack

            if player_attack <= -2:
                player_attack = witch_attack + player_attack

                if witch_attack and player_attack <=0:
                    witch_health == witch_health
                    player_health == player_health
                print("player and witch took no damage.")

            elif player_attack > witch_attack:
                witch_health = witch_health - player_attack
                print("witch took", player_attack, "the witches health is now", witch_health)
            else:
                player_health = player_health - witch_attack
                print("You took damage", witch_attack, "your health is now", player_health)




loop()