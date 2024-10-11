end_game = False
start_of_game = False
check1 = False

while end_game is False:
    if end_game == True:
        exit()
    while start_of_game is False:
        enter_name = input("Knight please enter your name:")
        hero_name = enter_name.upper()
        print("Hello Knight", hero_name,". Pleases hit the enter key to continue:")
        input()
        print("Our Knight story begins with them walking though a beautiful mythical forest after a successful mission.")
        input()
        print("As knight", hero_name," is happily walking in the forest dreaming about what they will get with the new bag of gold they pass by some bushes.\nStill unaware of there surrounding they don't see a ugly green witch hiding within the bushes.\nSuddenly the witch jumps out of the bushes and snatches knight",hero_name, "bag of gold and says.")
        input()
        print("Witch: Which hand of the witch will it be hahaha as she holds her left and right hand out in a fist.\nYou look at her confused and ask your self which hand will I choose Left or Right?")
        input()
        if start_of_game ==True:
            enter_name = input("Knight please enter your name:")
            hero_name = enter_name.upper()
            print("Hello Knight", hero_name, ". Pleases hit the enter key to continue:")
            input()
            print(
                "Our Knight story begins with them walking though a beautiful mythical forest after a successful mission.")
            input()
            print("As knight", hero_name,
                  " is happily walking in the forest dreaming about what they will get with the new bag of gold they pass by some bushes.\nStill unaware of there surrounding they don't see a ugly green witch hiding within the bushes.\nSuddenly the witch jumps out of the bushes and snatches knight",
                  hero_name, "bag of gold and says.")
            input()
            print(
                "Witch: Which hand of the witch will it be hahaha as she holds her left and right hand out in a fist.\nYou look at her confused and ask your self which hand will I choose Left or Right?")
            input()

        while check1 is False:
            witch_hand = input("Type left or right to choose: ")
            while witch_hand != "left" and witch_hand != "right" and witch_hand != "Left" and witch_hand != "Right":
                print("Please enter left or right.")
                witch_hand = input("Type left or right to choose: ")
            if witch_hand == "left" or witch_hand == "Left":
                print()
                print("The Witch laughs and says")
                input()
                print("Witch: Wrong hand.")
                input()
                print("Then the witch throws a potion at you turning you into a frog. You watch her as she skips away laughing.\nThe End.")
                input()
                ending1 = input("would you like to play again?\nIf you want to start from your last choose type 'C1'\nIf you want to start from the beginning type 'B'\nIf you want to end the game type 'E'\nEnter choose:")
                if ending1 == "B" or "b":
                    start_of_game = True
                if ending1 == "C1" or "c1":
                    check1 = True
                if ending1 == "E":
                    print("Thanks for playing")
                    end_game = True
                if witch_hand == "right" or witch_hand == "right":
                    print("You chose the correct hand but the witch put her hands behind her back an switches which hand your money was i and says.")
                    input()
                    print("Witch: Wong Hand. as she laughs")
                    input()
                    print("Knight", hero_name, "Done with the witches game charges at her saying.")
                    input()
                    print("Knight", hero_name,": YOU CHEATED GIVE ME MY GOLD BACK!!")
                    input()
                    print("The witch panicking grabs dirt from the ground and says.")
                    input()
                    print("Witch: Mysterious dirt. Then throws the dirt in your eyes.")