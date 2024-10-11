checkpoint1 = 3
checkpoint2 =4
checkpoint3 = 5
checkpoint4 = 6


start1 = 7


while start1 == 7:
    start_of_story = int(input("hello enter you A number between 1-4"))
    while start_of_story != 1 and start_of_story != 2 and start_of_story != 3 and start_of_story != 4:
        print("pleases enter  1-4")
        start_of_story = int(input("hello enter you A number between 1-4"))

    if start_of_story ==1:
        print("nice choice")
        favorite = input("Is this your favorite number. Y/N: ").lower().strip()
        while checkpoint1 <= 4:
            while favorite != "y" and favorite != "n":
                print("please enter y or n")
                favorite = input("Is this your favorite number. Y/N: ").lower().strip()
            if favorite == "y":
                print("cool")
                restart1 = input("if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e'").lower().strip()
                if restart1 == "fix1":
                    checkpoint1 = checkpoint1 + 4
                elif restart1 == "s":
                    start1 = start1 - 3
                elif restart1 == "e":
                    exit()
            if favorite == "n":
                print("why not")
                restart1 = input("if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e'").lower().strip()
                if restart1 == "fix1":
                    checkpoint1 = checkpoint1 + 4
                elif restart1 == "s":
                    start1 = 2
                elif restart1 == "e":
                    exit()

    if start_of_story ==2:
        print("nice choice")
        favorite = input("Is this your favorite number. Y/N: ").lower().strip()
        while checkpoint2 <= 6:
            while favorite != "y" and favorite != "n":
                print("please enter y or n")
                favorite = input("Is this your favorite number. Y/N: ").lower().strip()
            if favorite == "y":
                print("cool")
                restart1 = input("if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e'").lower().strip()
                if restart1 == "fix1":
                    checkpoint2 = checkpoint2 + 4
                elif restart1 == "s":
                    start1 = 2
                elif restart1 == "e":
                    exit()
            if favorite == "n":
                print("why not")
                restart1 = input("if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e'").lower().strip()
                if restart1 == "fix1":
                    checkpoint1 = checkpoint1 + 4
                elif restart1 == "s":
                    start1 = 2
                elif restart1 == "e":
                    exit()

    if start_of_story ==3:
        print("nice choice")
        favorite = input("Is this your favorite number. Y/N: ").lower().strip()
        while checkpoint3 <= 8:
            while favorite != "y" and favorite != "n":
                print("please enter y or n")
                favorite = input("Is this your favorite number. Y/N: ").lower().strip()
            if favorite == "y":
                print("cool")
                restart1 = input("if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e'").lower().strip()
                if restart1 == "fix1":
                    checkpoint3 = checkpoint3 + 4
                elif restart1 == "s":
                    start1 = 2
                elif restart1 == "e":
                    exit()
            if favorite == "n":
                print("why not")
                restart1 = input("if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e'").lower().strip()
                if restart1 == "fix1":
                    checkpoint1 = checkpoint1 + 4
                elif restart1 == "s":
                    start1 = 2
                elif restart1 == "e":
                    exit()

    if start_of_story == 4:
        print("nice choice")
        favorite = input("Is this your favorite number. Y/N: ").lower().strip()
        while checkpoint4 <= 10:
            while favorite != "y" and favorite != "n":
                print("please enter y or n")
                favorite = input("Is this your favorite number. Y/N: ").lower().strip()
            if favorite == "y":
                print("cool")
                restart1 = input("if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e'").lower().strip()
                if restart1 == "fix1":
                    checkpoint4 = checkpoint4 + 4
                elif restart1 == "s":
                    start1 = 2
                elif restart1 == "e":
                    exit()
            if favorite == "n":
                print("why not")
                restart1 = input("if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e'").lower().strip()
                if restart1 == "fix1":
                    checkpoint1 = checkpoint1 + 4
                elif restart1 == "s":
                    start1 = 2
                elif restart1 == "e":
                    exit()

if start1 != 7:
    start_of_story = int(input("hello enter you A number between 1-4"))
    while start_of_story != 1 and start_of_story != 2 and start_of_story != 3 and start_of_story != 4:
        print("pleases enter  1-4")
        start_of_story = int(input("hello enter you A number between 1-4"))

    if start_of_story == 1:
        print("nice choice")
        favorite = input("Is this your favorite number. Y/N: ").lower().strip()
        while checkpoint1 <= 4:
            while favorite != "y" and favorite != "n":
                print("please enter y or n")
                favorite = input("Is this your favorite number. Y/N: ").lower().strip()
            if favorite == "y":
                print("cool")
                restart1 = input(
                    "if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e'").lower().strip()
                if restart1 == "fix1":
                    checkpoint1 = checkpoint1 + 4
                elif restart1 == "s":
                    start1 = 2
                elif restart1 == "e":
                    exit()
            if favorite == "n":
                print("why not")
                restart1 = input("if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e'").lower().strip()
                if restart1 == "fix1":
                    checkpoint1 = checkpoint1 + 4
                elif restart1 == "s":
                    start1 = 2
                elif restart1 == "e":
                    exit()

    if start_of_story == 2:
        print("nice choice")
        favorite = input("Is this your favorite number. Y/N: ").lower().strip()
        while checkpoint2 <= 6:
            while favorite != "y" and favorite != "n":
                print("please enter y or n")
                favorite = input("Is this your favorite number. Y/N: ").lower().strip()
            if favorite == "y":
                print("cool")
                restart1 = input(
                    "if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e'").lower().strip()
                if restart1 == "fix1":
                    checkpoint2 = checkpoint2 + 4
                elif restart1 == "s":
                    start1 = 2
                elif restart1 == "e":
                    exit()
            if favorite == "n":
                print("why not")
                restart1 = input("if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e'").lower().strip()
                if restart1 == "fix1":
                    checkpoint1 = checkpoint1 + 4
                elif restart1 == "s":
                    start1 = 2
                elif restart1 == "e":
                    exit()

    if start_of_story == 3:
        print("nice choice")
        favorite = input("Is this your favorite number. Y/N: ").lower().strip()
        while checkpoint3 <= 8:
            while favorite != "y" and favorite != "n":
                print("please enter y or n")
                favorite = input("Is this your favorite number. Y/N: ").lower().strip()
            if favorite == "y":
                print("cool")
                restart1 = input(
                    "if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e'").lower().strip()
                if restart1 == "fix1":
                    checkpoint3 = checkpoint3 + 4
                elif restart1 == "s":
                    start1 = 2
                elif restart1 == "e":
                    exit()
            if favorite == "n":
                print("why not")
                restart1 = input("if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e'").lower().strip()
                if restart1 == "fix1":
                    checkpoint1 = checkpoint1 + 4
                elif restart1 == "s":
                    start1 = 2
                elif restart1 == "e":
                    exit()

    if start_of_story == 4:
        print("nice choice")
        favorite = input("Is this your favorite number. Y/N: ").lower().strip()
        while checkpoint4 <= 10:
            while favorite != "y" and favorite != "n":
                print("please enter y or n")
                favorite = input("Is this your favorite number. Y/N: ").lower().strip()
            if favorite == "y":
                print("cool")
                restart1 = input(
                    "if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e'").lower().strip()
                if restart1 == "fix1":
                    checkpoint4 = checkpoint4 + 4
                elif restart1 == "s":
                    start1 = 2
                elif restart1 == "e":
                    exit()
            if favorite == "n":
                print("why not")
                restart1 = input("if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e'").lower().strip()
                if restart1 == "fix1":
                    checkpoint1 = checkpoint1 + 4
                elif restart1 == "s":
                    start1 = 2
                elif restart1 == "e":
                    exit()




