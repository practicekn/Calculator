import os
import math


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def body():
    print("1 - прямокутний")
    print("2 - рівносторонній")
    print("3 - рівнобедренний")
    choose = input("Виберіть який трикутник будете обчислюватись: ")
    cls()


def first():
    print("1 - є кут за яким потрібно знайти(не 90)")
    print("2 - існують лише катети")
    print("3 - шснує радіус кола за яким потрібно знайти дані")
    choose1 = input("Тож ваш вибір: ")
    cls()

    if choose1 == '1':
        c = int(input("Введіть довжину гіпотенузи: "))
        p = c * math.cos(45) + c + c
        S = (c * math.cos(45) * c) / 2
        print("Периметр: ", math.ceil(p))
        print("Площа: ", math.ceil(S))

    elif choose1 == '2':
        a = int(input("Впишіть перший катет: "))
        b = int(input("Впишіть другий катет: "))
        print("Площа: ", (1 / 2) * a * b)
        c = math.sqrt(pow(a, 2) + pow(b, 2))
        print("Щоб знайти периметр потрібно обчислити гіпотенузу c = √(a^2 + b^2) ")
        print("c = ", math.ceil(c))
        print("Периметр: ", a + b + c)

    elif choose1 == '3':
        print("1 - у вас є радіус вписаного кола")
        print("2 - у вас існує радіус описаного кола")
        choose2 = input("Тож ваш вибір: ")
        cls()

        if choose2 == '1':
            R = int(input("Введіть довжину радіуса R: "))
            S = R * 4
            print("Площа: ", S)
            print("Периметр знайти не можливо")

        elif choose2 == '2':
            R = int(input("Введіть довжину радіуса r: "))
            c = int(input("Введіть довжину гіпотенузи: "))
            S = r * (r + c)
            print("Площа: ", S)
            print("Периметр знайти не можливо")


def second():
    print("1 - знайти площу за стороною і висотою")
    print("2 - знайти площу за стороною")
    print("3 - знайти площу за радіусом кола")
    choose2 = input("Тож ваш вибір: ")
    cls()

    if choose2 == '1':
        a = int(input("Впишіть сторону: "))
        h = math.sqrt((a * a) - (a // 2 * a // 2))
        print("H = √(a^2 - (a/2)^2)")
        print("H = ", h)
        S = 1 / 2 * a * h
        print("Площа: ", math.ceil(S))
        print("Периметр: ", a * 3)

    elif choose2 == '2':
        a = int(input("Впишіть сторону: "))
        print("Площа: ", (a * a * math.sqrt(3)) / 4)
        print("Периметр: ", a * 3)
    elif choose2 == '3':
        print("1 - радіус вписаного кола r")
        print("2 - радіус описаного кола R")
        choose2 = input("Тож ваш вибір: ")
        cls()
        if choose2 == '1':
            R = int(input("Введіть довжину радіуса r: "))
            S = 3 * math.sqrt(3) * r * r
            print("Площа: ", S)

        elif choose2 == '2':
            R = int(input("Введіть довжину радіуса R: "))
            S = (3 * math.sqrt(3) * R * R) / 4
            print("Площа: ", S)


def third():
    print("1 - знайти площу за стороною та висотою")
    print("2 - знайти площу за формулою герона")
    choose1 = input("Тож ваш вибір: ")
    cls()

    if choose1 == '1':
        a = int(input("Впишіть сторону: "))
        b = int(input("Впишіть основу: "))
        print("Для того, щоб знайти площу потрібна висота: ")
        h = math.sqrt(pow(a, 2) - pow((b / 2), 2))
        print("H = √(a^2 - (b/2)^2)", "h = ", math.ceil(h))
        print("Площа: ", (1 / 2) * b * h)
        print("Периметр: ", a * 2 + b)

    elif choose1 == '2':
        a = int(input("Впишіть сторону: "))
        b = int(input("Впишіть основу: "))
        S = 1 / 2 * b * math.sqrt((a + 1 / 2 * b) * (a - 1 / 2 * b))
        print("Площа: ", math.ceil(S))
        print("Периметр: ", a * 2 + b)


print("1 - прямокутний")
print("2 - рівносторонній")
print("3 - рівнобедренний")
choose = input("Виберіть який трикутник будете обчислюватись: ")
cls()

if choose == '1':  # прямокутний
    print("1 - є кут за яким потрібно знайти(не 90)")
    print("2 - існують лише катети")
    print("3 - шснує радіус кола за яким потрібно знайти дані")
    choose1 = input("Тож ваш вибір: ")
    cls()

    if choose1 == '1':
        c = int(input("Введіть довжину гіпотенузи: "))
        p = c * math.cos(45) + c + c
        S = (c * math.cos(45) * c) / 2
        print("Периметр: ", math.ceil(p))
        print("Площа: ", math.ceil(S))

    elif choose1 == '2':
        a = int(input("Впишіть перший катет: "))
        b = int(input("Впишіть другий катет: "))
        print("Площа: ", (1 / 2) * a * b)
        c = math.sqrt(pow(a, 2) + pow(b, 2))
        print("Щоб знайти периметр потрібно обчислити гіпотенузу c = √(a^2 + b^2) ")
        print("c = ", math.ceil(c))
        print("Периметр: ", a + b + c)

    elif choose1 == '3':
        print("1 - у вас є радіус вписаного кола")
        print("2 - у вас існує радіус описаного кола")
        choose2 = input("Тож ваш вибір: ")
        cls()

        if choose2 == '1':
            R = int(input("Введіть довжину радіуса R: "))
            S = R * 4
            print("Площа: ", S)
            print("Периметр знайти не можливо")

        elif choose2 == '2':
            R = int(input("Введіть довжину радіуса r: "))
            c = int(input("Введіть довжину гіпотенузи: "))
            S = r * (r + c)
            print("Площа: ", S)
            print("Периметр знайти не можливо")
    else:
        print("Спробуйте ще разок")
        body()
        if choose == '1':
            first()
        elif choose == '2':
            second()
        elif choose == '3':
            third()

elif choose == '2':  # рівньосторонній
    print("1 - знайти площу за стороною і висотою")
    print("2 - знайти площу за стороною")
    print("3 - знайти площу за радіусом кола")
    choose2 = input("Тож ваш вибір: ")
    cls()

    if choose2 == '1':
        a = int(input("Впишіть сторону: "))
        h = math.sqrt((a * a) - (a // 2 * a // 2))
        print("H = √(a^2 - (a/2)^2)")
        print("H = ", h)
        S = 1 / 2 * a * h
        print("Площа: ", math.ceil(S))
        print("Периметр: ", a * 3)

    elif choose2 == '2':
        a = int(input("Впишіть сторону: "))
        print("Площа: ", (a * a * math.sqrt(3)) / 4)
        print("Периметр: ", a * 3)
    elif choose2 == '3':
        print("1 - радіус вписаного кола r")
        print("2 - радіус описаного кола R")
        choose2 = input("Тож ваш вибір: ")
        cls()
        if choose2 == '1':
            R = int(input("Введіть довжину радіуса r: "))
            S = 3 * math.sqrt(3) * r * r
            print("Площа: ", S)

        elif choose2 == '2':
            R = int(input("Введіть довжину радіуса R: "))
            S = (3 * math.sqrt(3) * R * R) / 4
            print("Площа: ", S)

        else:
            print("Спробуйте ще разок")
            body()
            if choose == '1':
                first()
            elif choose == '2':
                second()
            elif choose == '3':
                third()
    else:
        print("Спробуйте ще разок")
        body()
        if choose == '1':
            first()
        elif choose == '2':
            second()
        else:
            third()


elif choose == '3':  # рівнобедренний
    print("1 - знайти площу за стороною та висотою")
    print("2 - знайти площу за формулою герона")
    choose1 = input("Тож ваш вибір: ")
    cls()

    if choose1 == '1':
        a = int(input("Впишіть сторону: "))
        b = int(input("Впишіть основу: "))
        print("Для того, щоб знайти площу потрібна висота: ")
        h = math.sqrt(pow(a, 2) - pow((b / 2), 2))
        print("H = √(a^2 - (b/2)^2)", "h = ", math.ceil(h))
        print("Площа: ", (1 / 2) * b * h)
        print("Периметр: ", a * 2 + b)

    elif choose1 == '2':
        a = int(input("Впишіть сторону: "))
        b = int(input("Впишіть основу: "))
        S = 1 / 2 * b * math.sqrt((a + 1 / 2 * b) * (a - 1 / 2 * b))
        print("Площа: ", math.ceil(S))
        print("Периметр: ", a * 2 + b)

    else:
        print("Спробуйте ще разок")
        body()
        if choose == '1':
            first()
        elif choose == '2':
            second()
        else:
            third()



else:
    print("Спробуйте ще разок")
    body()
    if choose == '1':
        first()
    elif choose == '2':
        second()
    elif choose == '3':
        third()
    else:
        print("Спробуйте ще разок")
        body()
        if choose == '1':
            first()
        elif choose == '2':
            second()
        elif choose == '3':
            third()