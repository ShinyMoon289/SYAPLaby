def zad1():
    # This task converts seconds to days, hours, minutes

    time_secs = int(input("Enter seconds: "))
    years = time_secs // (60 * 60 * 24 * 365)
    time_secs %= (60 * 60 * 24 * 365)
    days = time_secs // (60 * 60 * 24)
    time_secs %= (60 * 60 * 24)
    hours = time_secs // (60 * 60)
    time_secs %= (60 * 60)
    minutes = time_secs // 60
    time_secs %= 60
    print(f"{years} years, {days} days,  {hours} hours, {minutes} minutes, {time_secs} seconds")


def zad2():
    # This task shows numbers if met in a string
    word = str(input("Enter line: "))
    for i in range(0, len(word)):
        if word[i] >= '0' and word[i] <= '9':
            print(f"{word[i]}")


# This task show number of syllables and vowels
def zadanie_3():
    wordlist = ['Python', 154543, 32, 'QweRty', 34, 19, 'love']
    vowels = 'aeiuyo'
    for i in wordlist:
        if not isinstance(i, str):
            continue
        sylc = 0
        vowc = 0
        convt = i.lower()
        for g in convt:
            if g in vowels:
                vowc += 1
            else:
                sylc += 1
        print(i)
        print("Syllables: ", sylc, ", Vowels: ", vowc)
    print("\n")


# This task merges two dictionaries
def zadanie_4():
    dict1 = {
        "name": "Ilya",
        "surname": "Kudin"
    }
    dict2 = {"group": 272301, "faculty": "IEF"}
    dict3 = dict1 | dict2
    print(dict3)


# This task shows menu of a shop ant lets you buy some
def zadanie_5():
    menu = ("Description", "Price", "Stock", "Show all", "Buy", "Quit")
    product = {"Shoes": ["Leather shoes", "420", "100"]}
    while 1:
        for i in menu:
            print(i)
        ch = int(input("Choose an option"))
        if ch == 1:
            print(product["Shoes"][0])
        elif ch == 2:
            print(product["Shoes"][1])
        elif ch == 3:
            print(product["Shoes"][2])
        elif ch == 4:
            print(product)
        elif ch == 5:
            amount = int(input("Enter quantity: "))
            if amount > int(product["Shoes"][2]):
                print("We don't have enough shoes!")
            else:
                print("Purchase successful!")
        elif ch == 6:
            break
        else:
            print("Incorrect value")


# This task show the sum of the elements before a negative one
def zadanie_6():
    ch = int(input("Enter size of the tuple"))
    tup = []
    for i in range(ch):
        ind = (int(input()))
        tup.append(ind)
    tup = tuple(tup)
    sum = 0
    print(tup)
    for i in tup:
        if i < 0:
            break
        else:
            sum = sum + i
    print(sum)
