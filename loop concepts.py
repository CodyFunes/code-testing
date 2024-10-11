#New checkpoint concept
#Failed checkpoint code is on row 121


def start1():
    start_story = 0
    while start_story != 1 and start_story != 2 and start_story != 3 and start_story != 4:
        try:
            start_story = int(input("Hello please enter a number between 1-4: "))
        except ValueError:
            print("Pleases enter  1-4")
            continue
    print("Nice choice.")
    checkpoint(start_story)



def checkpoint(start_story):
    if start_story == 1:
        favorite = input("Is this your favorite number. Y/N: ").lower().strip()
        while favorite != "y" and favorite != "n":
            print("Please enter y or n")
            favorite = input("Is this your favorite number. Y/N: ").lower().strip()
        if favorite == "y":
            print("Cool!")
            print()
            restart1 = input("If you want to fix your last answer type 'Fix'\nIf you want to start from the beginning type 'S'\nIf you want to end the code type 'E'\nEnter choice: ").lower().strip()
            if restart1 == "s":
                return start1()
            if restart1 == "fix":
                return checkpoint(start_story)
            if restart1 == "e":
                exit()
        if favorite == "n":
            print("Why not.")
            print()
            restart1 = input("If you want to fix your last answer type 'Fix'\nIf you want to start from the beginning type 'S'\nIf you want to end the code type 'E'\nEnter your choice: ").lower().strip()
            if restart1 == "s":
                return start1()
            elif restart1 == "fix":
                return checkpoint(start_story)
            elif restart1 == "e":
                exit()

    if start_story ==2:
        favorite = input("Is this your favorite number. Y/N: ").lower().strip()
        while favorite != "y" and favorite != "n":
            print("Please enter y or n:")
            favorite = input("Is this your favorite number. Y/N: ").lower().strip()
        if favorite == "y":
            print("Cool!")
            print()
            restart1 = input("If you want to fix your last answer type 'Fix'\nIf you want to start from the beginning type 's'\nIf you want to end the code type 'e'\nEnter your choice: ").lower().strip()
            if restart1 == "fix":
                return checkpoint(start_story)
            elif restart1 == "s":
                start1()
            elif restart1 == "e":
                exit()
        if favorite == "n":
            print("Why not.")
            print()
            restart1 = input("If you want to fix your last answer type 'Fix'\nIf you want to start from the beginning type 'S'\nIf you want to end the code type 'E'\nEnter your choice: ").lower().strip()
            if restart1 == "fix1":
                return checkpoint(start_story)
            elif restart1 == "s":
                return start1()
            elif restart1 == "e":
                exit()

    if start_story ==3:
        favorite = input("Is this your favorite number. Y/N: ").lower().strip()
        while favorite != "y" and favorite != "n":
            print("Please enter y or n")
            favorite = input("Is this your favorite number. Y/N: ").lower().strip()
        if favorite == "y":
            print("Cool!")
            print()
            restart1 = input("If you want to fix your last answer type 'Fix'\nIf you want to start from the beginning type 'S'\nIf you want to end the code type 'E'\nEnter your choice:").lower().strip()
            if restart1 == "fix":
                return checkpoint(start_story)
            elif restart1 == "s":
                return start1()
            elif restart1 == "e":
                exit()
        if favorite == "n":
            print("Why not.")
            print()
            restart1 = input("If you want to fix your last answer type 'fix'\nIf you want to start from the beginning type 's'\nIf you want to end the code type 'e'\nEnter your choice: ").lower().strip()
            if restart1 == "fix":
                return checkpoint(start_story)
            elif restart1 == "s":
                return start1()
            elif restart1 == "e":
                exit()

    if start_story == 4:
        favorite = input("Is this your favorite number. Y/N: ").lower().strip()
        while favorite != "y" and favorite != "n":
            print("Please enter y or n")
            favorite = input("Is this your favorite number. Y/N: ").lower().strip()
        if favorite == "y":
            print("Cool!")
            print()
            restart1 = input("If you want to fix your last answer type 'Fix'\nIf you want to start from the beginning type 'S'\nIf you want to end the code type 'E'\nEnter your choice: ").lower().strip()
            if restart1 == "fix":
                return checkpoint(start_story)
            elif restart1 == "s":
                return start1()
            elif restart1 == "e":
                exit()
        if favorite == "n":
            print("Why not.")
            print()
            restart1 = input("If you want to fix your last answer type 'Fix'\nIf you want to start from the beginning type 'S'\nIf you want to end the code type 'E'\nEnter your choice: ").lower().strip()
            if restart1 == "fix":
                checkpoint(start1)
            elif restart1 == "s":
                return start1()
            elif restart1 == "e":
                exit()
checkpoint(start_story=(1, 4))
start1()



#This was the original consept code that did not work.
#It is missing a few part they were reused in the new code.

# start1 = 1
# checkpoint1 = 3
# checkpoint2 =4
# checkpoint3 = 5
# checkpoint4 = 6



# if start1 == 1:
#     start_of_story = int(input("hello enter you A number between 1-4: "))
#     while start_of_story != 1 and start_of_story != 2 and start_of_story != 3 and start_of_story != 4:
#         print("pleases enter  1-4: ")
#         start_of_story = int(input("hello enter you A number between 1-4: "))
#
#     if start_of_story == 1:
#         print("nice choice")
#         favorite = input("Is this your favorite number. Y/N: ").lower().strip()
#         while checkpoint1 <= 4:
#             while favorite != "y" and favorite != "n":
#                 print("please enter y or n")
#                 favorite = input("Is this your favorite number. Y/N: ").lower().strip()
#             if favorite == "y":
#                 print("cool")
#                 restart1 = input(
#                     "if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e'\nEnter number: ").lower().strip()
#                 if restart1 == "fix1":
#                     checkpoint1 = checkpoint1 + 4
#                 elif restart1 == "s":
#                     start1 = start1 - 3
#                 elif restart1 == "e":
#                     exit()
#             if favorite == "n":
#                 print("why not")
#                 restart1 = input("if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e'\nEnter number: ").lower().strip()
#                 if restart1 == "fix1":
#                     checkpoint1 = checkpoint1 + 4
#                 elif restart1 == "s":
#                     start1 = 2
#                 elif restart1 == "e":
#                     exit()
#
#     if start_of_story == 2:
#         print("nice choice")
#         favorite = input("Is this your favorite number. Y/N: ").lower().strip()
#         while checkpoint2 <= 6:
#             while favorite != "y" and favorite != "n":
#                 print("please enter y or n")
#                 favorite = input("Is this your favorite number. Y/N: ").lower().strip()
#             if favorite == "y":
#                 print("cool")
#                 restart1 = input(
#                     "if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e'\nEnter number: ").lower().strip()
#                 if restart1 == "fix1":
#                     checkpoint2 = checkpoint2 + 4
#                 elif restart1 == "s":
#                     start1 = 2
#                 elif restart1 == "e":
#                     exit()
#             if favorite == "n":
#                 print("why not")
#                 restart1 = input("if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e'\nEnter number: ").lower().strip()
#                 if restart1 == "fix1":
#                     checkpoint2 = checkpoint2 + 4
#                 elif restart1 == "s":
#                     start1 = 2
#                 elif restart1 == "e":
#                     exit()
#
#     if start_of_story == 3:
#         print("nice choice")
#         favorite = input("Is this your favorite number. Y/N: ").lower().strip()
#         while checkpoint3 <= 8:
#             while favorite != "y" and favorite != "n":
#                 print("please enter y or n")
#                 favorite = input("Is this your favorite number. Y/N: ").lower().strip()
#             if favorite == "y":
#                 print("cool")
#                 restart1 = input(
#                     "if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e'\nEnter number: ").lower().strip()
#                 if restart1 == "fix1":
#                     checkpoint3 = checkpoint3 + 4
#                 elif restart1 == "s":
#                     start1 = 2
#                 elif restart1 == "e":
#                     exit()
#             if favorite == "n":
#                 print("why not")
#                 restart1 = input("if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e\nEnter number: '").lower().strip()
#                 if restart1 == "fix1":
#                     checkpoint3 = checkpoint3 + 4
#                 elif restart1 == "s":
#                     start1 = 2
#                 elif restart1 == "e":
#                     exit()
#
#     if start_of_story == 4:
#         print("nice choice")
#         favorite = input("Is this your favorite number. Y/N: ").lower().strip()
#         while checkpoint4 <= 10:
#             while favorite != "y" and favorite != "n":
#                 print("please enter y or n")
#                 favorite = input("Is this your favorite number. Y/N: ").lower().strip()
#             if favorite == "y":
#                 print("cool")
#                 restart1 = input(
#                     "if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e'\nEnter number: ").lower().strip()
#                 if restart1 == "fix1":
#                     checkpoint4 = checkpoint4 + 4
#                 elif restart1 == "s":
#                     start1 = 2
#                 elif restart1 == "e":
#                     exit()
#             if favorite == "n":
#                 print("why not")
#                 restart1 = input("if you want to fix your last answer type 'fix1'\nIf you want to start from the beginning type 's'\nif you want to end the code type 'e'\nEnter number:").lower().strip()
#                 if restart1 == "fix1":
#                     checkpoint4 = checkpoint4 + 4
#                 elif restart1 == "s":
#                     start1 = 2
#                 elif restart1 == "e":
#                     exit()




