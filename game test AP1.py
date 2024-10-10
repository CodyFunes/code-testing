story = ""



def loop():
    hero_name =(input("enter name"))
    story = input("the shining knight", hero_name, "was walking in a forest with shining armor and as they are walking passed a bush a green witch steals there pouch of gold and says")
    story = input("Hit the Enter Key to Continue:")
    witch_hand = input("GREEN WITCH - Which hand of the witch will it be' As she hold her hand out wanting for you to choose which of her hands has your gold . Will you choose the right hand or left hand?   :")

    ending1 = input("do you want to play again? yes/no")

    if witch_hand == str("right"):
        print("hell0")

    else:
        print(ending1)


    if ending1 == str("yes"):
        loop()
    else:
        print("Thanks for playing!")


loop()