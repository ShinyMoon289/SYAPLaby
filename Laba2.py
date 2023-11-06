import numpy as np


def zadanie1():  # this task shows the amount vowels and syllables in a string
    vowels = "aeiuyo"
    try:
        word = str(input("Enter the word"))
    except TypeError:
        print("Incorrect input!")
    else:
        vowcount = 0
        sylcount = 0
        print(f"Your string: {word}")
        word = word.lower()
        for i in word:
            if i.isalpha():
                if i in vowels:
                    vowcount += 1
                else:
                    sylcount += 1
        print(f"Syllables: {sylcount}, vowels: {vowcount}")


def zadanie2():
    def check(*args):
        if isinstance(*args, str):
            for i in args:
                if not args[i].isalpha():
                    args.replace(args[i], "")
            print(*args)
        elif isinstance(*args, dict):
            max = args[0]
            for i in args:
                if i > max:
                    max = i
            print(max)
        elif isinstance(*args, list):
            count = 0
            for i in args:
                if i // 2 == 0:
                    count += 1
                args = set(*args)
                print(f"Final list: {args}. Amount of even numbers: {count}")
        else:
            print("This function does not take this parameter")

    while 1:
        try:
            # The dictionary you're supposed to type is actually preset, cause i'm too lazy
            print("1 - Enter a string\n2 - Enter a list\n3 - Enter a dictionary (preset)")
            ch = int(input("Enter the type you want to type in."))
        except TypeError:
            print("Incorrect value!")
        else:
            if ch == 1:
                try:
                    phrase = str(input("Enter your sentence:"))
                except TypeError:
                    print("Incorrect input!")
                    continue
                else:
                    check(phrase)
            elif ch == 2:
                try:
                    size = int(input("Enter the size of the list: "))
                    if size <= 0:
                        raise ValueError("Negative or null size is not allowed!")
                except TypeError:
                    continue
                else:
                    mylist = []
                    for m in range(size):
                        try:
                            mylist[m] = int(input())
                        except ValueError:
                            print("Incorrect value found!")
                            continue
                    check(mylist)
            elif ch == 3:
                mydict = {"Border of space": 100000,
                          "Deepest point on Earth": 12300,
                          "Average altitude of planes": 4000}
                check(mydict)


def zadanie3():
    try:
        cols = int(input("Enter the number of columns: "))
        rows = int(input("Enter the number of rows: "))
        if cols or rows <= 0:
            raise ValueError
    except ValueError:
        print("Incorrect sizes!")
    else:
        matrix = np.empty([cols, rows], dtype=int)
        for j in range(cols):
            for i in range(rows):
                try:
                    row = []
                    row[i] = int(input())
                except TypeError:
                    print("Incorrect value found!")
                else:
                    np.concatenate((matrix, row), 0)
        count = 0
        for i in range(rows):
            sw = True
            for j in range(cols):
                if matrix[i][j] == 0:
                    sw = False
                else:
                    continue
            if sw:
                count += 1
        print(f"Number of rows that don't have 0: {count}")
