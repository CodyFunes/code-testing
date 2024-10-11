# Does not work
def main():
    textfile = open('words.txt', 'r').read()
    dictionary_of_words = filename(textfile)
    yay_anagrams = anagramlist(lword)
    double_whammy = binary_search(fresh_list, ltextfile)
    answer = output()


def filename(textfile):
    ltextfile = textfile.lower()
    scrambled_eggs = input("Please enter a jumbled word: ")
    lword = scrambled_eggs.lower()


def anagramlist(lword):
    if lword == "":
        return([lword])
    else:
        yay_word = lword[1:]
        first_letter = lword[0]
        fresh_list = []
        for mixed_word in filename(yay_word):
            for pos in range(len(mixed_word) + 1):
                fresh_list.append(mixed_word[:pos] + first_letter[0] + mixed_word[pos:])
            return fresh_list


def binary_search(fresh_list, ltextfile):
    for eachword in fresh_list:
        low = 0
        high = len(list) - 1
    while low <= high:
        mid = (low + high)//2
        item = list[mid]
    if fresh_list == item:
        return True
    elif fresh_list < item:
        high = mid - 1
    elif fresh_list > item:
        low = mid + 1
    return False


def output():
    if fresh_list == True:
        newlist = set()
        for item in fresh_list:
            newlist.add(item)
        print("Your words are:/n", newlist)
    if fresh_list == False:
        print("Your word cannot be unjumbled.")
main()