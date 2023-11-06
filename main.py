import Laba1
import Laba2

while 1:
    ch = int(input("Which lab you wanna see? 0 to quit."))
    if ch == 1:
        while 1:
            ch2 = int(input("Which task you wanna choose? 1 - 6. 0 to return"))
            if ch2 == 1:
                Laba1.zad1()
            elif ch2 == 2:
                Laba1.zad2()
            elif ch2 == 3:
                Laba1.zadanie_3()
            elif ch2 == 4:
                Laba1.zadanie_4()
            elif ch2 == 5:
                Laba1.zadanie_5()
            elif ch2 == 6:
                Laba1.zadanie_6()
            elif ch2 == 0:
                break
            else:
                print("Incorrect choice!")
    elif ch == 2:
        while 1:
            ch2 = int(input("Which task you wanna choose? 1 - 4. 0 to return"))
            if ch2 == 1:
                Laba2.zadanie1()
            if ch2 == 2:
                Laba2.zadanie2()
            if ch2 == 3:
                Laba2.zadanie3()
    elif ch == 0:
        break
