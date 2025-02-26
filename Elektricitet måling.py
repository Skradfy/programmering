while True:
    P = float(input("Indtast effektforbrug"))
    U = 230
    I = P / U
    print(f"Strømmen er = {I}")
    choose_cable = int(input("Indtast 70 grader eller 90 grader"))

    if choose_cable == 70 and I < 13:
        print("1,5 mm")

    elif choose_cable == 70 and 13 <= I < 25:
        print("2,5mm")

    elif choose_cable == 70 and 25 <= I < 34:
        print("4mm")

    elif choose_cable == 90 and I < 18:
        print("1,5mm")

    elif choose_cable == 90 and 18 <= I < 25:
        print("2,5mm")

    elif choose_cable == 90 and 25 <= I < 40:
        print("4mm")

    else:
        print("Indtast ny effekt, værdien stemmer passer ikke i virkeligheden")

    continue_input = input("Ønsker du at prøve igen? ja/nej?")
    if continue_input == "nej":
        break
