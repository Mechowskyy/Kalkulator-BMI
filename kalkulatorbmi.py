def kalkulator_bmi():
    print("Oblicz swoje BMI i dowiedz się, czy twoja masa jest dobra. Tylko dla osób dorosłych, BMI dzieci, nastolatków i osób po 64 roku życia oblicza się inaczej.")
    while True:
        mass = int(input("Masa ciała(kg):"))
        height = int(input("Twój wzrost(cm):"))
        BMI = mass / ((height / 100) ** 2)
        print("Twoje BMI wynosi:", BMI)
        if BMI < 16:
            wynik = "Wygłodzenie"
        if BMI >= 16 and BMI < 17:
            wynik = "Wychudzenie"
        if BMI >= 17 and BMI < 18.5:
            wynik = "Niedowaga"
        if BMI >= 18.5 and BMI < 25:
            wynik = "Prawidłowa masa ciała"
        if BMI >= 25 and BMI < 30:
            wynik = "Nadwaga"
        if BMI >= 30 and BMI < 35:
            wynik = "Otyłość I stopnia"
        if BMI >= 35 and BMI < 40:
            wynik = "Otyłość II stopnia"
        if BMI > 40:
            wynik = "Otyłość III stopnia"
        print(wynik)
        print("=================")

kalkulator_bmi()
