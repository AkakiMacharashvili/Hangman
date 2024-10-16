from random import randint  # Do not delete this line


def displayIntro():
    print("________________________________________________")
    print("| | ")
    print("| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __")
    print("| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
    print("| | | | (_| | | | | (_| | | | | | | (_| | | | |")
    print("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
    print("                    __/ |                       ")
    print("                   |___/                       ")
    print("_______________________________________________")
    print("_____________________Rules_____________________")
    print("Try to guess the hidden word one letter at a")
    print("time. The number of dashes are equivalent to")
    print("the number of letters in the word. If a player")
    print("suggests a letter that occurs in the word,")
    print("blank places containing this character will be")
    print("filled with that letter. If the word does not")
    print("contain the suggested letter, one new element")
    print("of a hangman’s gallow is painted. As the game")
    print("progresses, a segment of a victim is added for")
    print("every suggested letter not in the word. Goal is")
    print("to guess the word before the man hangs!")
    print("_______________________________________________")

def displayEnd(result):
    if result :
        print("________________________________________________________________________")
        print("          _                                  _                          ")
        print("         (_)                                (_)                         ")
        print("__      ___ _ __  _ __   ___ _ __  __      ___ _ __  _ __   ___ _ __    ")
        print("\ \ /\ / / | '_ \| '_ \ / _ \ '__| \ \ /\ / / | '_ \| '_ \ / _ \ '__|   ")
        print(" \ V  V /| | | | | | | |  __/ |     \ V  V /| | | | | | | |  __/ |      ")
        print("  \_/\_/ |_|_| |_|_| |_|\___|_|      \_/\_/ |_|_| |_|_| |_|\___|_|      ")
        print("           | |   (_)    | |                  | (_)                      ")
        print("        ___| |__  _  ___| | _____ _ __     __| |_ _ __  _ __   ___ _ __ ")
        print("       / __| '_ \| |/ __| |/ / _ \ '_ \   / _` | | '_ \| '_ \ / _ \ '__|")
        print("      | (__| | | | | (__|   <  __/ | | | | (_| | | | | | | | |  __/ |   ")
        print("       \___|_| |_|_|\___|_|\_\___|_| |_|  \__,_|_|_| |_|_| |_|\___|_|   ")
        print("________________________________________________________________________")
    else:
        print("__________________________________________________________________________")
        print(" __     __           _           _   _                                    ")
        print(" \ \   / /          | |         | | | |                                   ")
        print("  \ \_/ /__  _   _  | | ___  ___| |_| |                                   ")
        print("   \   / _ \| | | | | |/ _ \/ __| __| |                                   ")
        print("    | | (_) | |_| | | | (_) \__ \ |_|_|                                   ")
        print("    |_|\___/ \__,_| |_|\___/|___/\__(_)                                   ")
        print("        _______ _                                        _ _          _ _ ")
        print("       |__   __| |                                      | (_)        | | |")
        print("          | |  | |__   ___   _ __ ___   __ _ _ __     __| |_  ___  __| | |")
        print("          | |  | '_ \ / _ \ | '_ ` _ \ / _` | '_ \   / _` | |/ _ \/ _` | |")
        print("          | |  | | | |  __/ | | | | | | (_| | | | | | (_| | |  __/ (_| |_|")
        print("          |_|  |_| |_|\___| |_| |_| |_|\__,_|_| |_|  \__,_|_|\___|\__,_(_)")
        print("__________________________________________________________________________")

def displayHangman(state):
    if state == 5:
        print("    ._______.  ")
        print("    |/         ")
        print("    |          ")
        print("    |          ")
        print("    |          ")
        print("    |          ")
        print("    |          ")
        print("____|___       ")
    elif state == 4:
        print("    ._______.  ")
        print("    |/      |  ")
        print("    |          ")
        print("    |          ")
        print("    |          ")
        print("    |          ")
        print("    |          ")
        print("____|___       ")
    elif state == 3:
        print("    ._______.  ")
        print("    |/      |  ")
        print("    |      (_) ")
        print("    |          ")
        print("    |          ")
        print("    |          ")
        print("    |          ")
        print("____|___       ")
    elif state == 2:
        print("    ._______. ")
        print("    |/      | ")
        print("    |      (_)")
        print("    |       | ")
        print("    |       | ")
        print("    |         ")
        print("    |         ")
        print("____|___      ")
    elif state == 1:
        print("    ._______.  ")
        print("    |/      |  ")
        print("    |      (_) ")
        print("    |      \|/ ")
        print("    |       |  ")
        print("    |          ")
        print("    |          ")
        print("____|___       ")
    elif state == 0:
        print("    ._______.  ")
        print("    |/      |  ")
        print("    |      (_) ")
        print("    |      \|/ ")
        print("    |       |  ")
        print("    |      / \ ")
        print("    |          ")
        print("____|___       ")

def getWord():
    lst = []
    file = open("hangman_words.txt", "r")
    for i in file.readlines():
        lst.append(i)
    file.close()
    rand = randint(0, len(lst)-1)
    str = lst[rand]

    return str[0:len(str)-1]

def valid(c):
    if 97 <= ord(c) <= 122:
        return True
    else:
        return False

def play():
    word = getWord()
    lives = 5
    length = len(word)
    s = ""
    st = set()
    for i in range(length):
        s += "*"
        st.add(word[i])

    while lives > 0 and length > 0:
        displayHangman(lives)
        print("Guess the word:" + s)
        letter = input("Enter the letter:")
        while not valid(letter):
            letter = input("Enter the letter:")

        if letter in st:
            for j in range(len(s)):
                if word[j] == letter and s[j] != letter:
                    r = s[j + 1:]
                    s = s[0:j] + letter
                    if (j + 1) < len(word):
                        s += r
                    length -= 1
        else:
            lives -= 1
    if(lives == 0):
        displayHangman(lives)
    print("Hidden word was: " + word)
    if lives == 0:
        return False
    elif length == 0:
        return True

def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        # TODO
        inp = input("Do you want to play again? (yes/no)")
        if inp == "no":
            return


if __name__ == "__main__":
    hangman()
