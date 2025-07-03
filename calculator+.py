while True:
    a = float(input("podaj pierwszą liczbę:"))
    b = float(input("podaj drugą liczbę:"))


    dzialanie = input("Wybierz działanie (+, -, *, /): ")

        # if = sprawdza warunek i wykonuje kod, jeśli warunek jest prawdziwy
        # elif = sprawdza kolejny warunek, jeśli poprzedni był fałszywy
        # else = wykonuje kod, jeśli żaden z poprzednich warunków nie był prawdziwy
        # == sprawdza równość dwóch wartości
        # != sprawdza nierówność dwóch wartości

    if dzialanie == "+":
        print(f"Wynik dodawania: {a + b}")
    elif dzialanie == "-":
        print(f"Wynik odejmowania: {a - b}")
    elif dzialanie == "*":
        print(f"Wynik mnożenia: {a * b}")
    elif dzialanie == "/":
        if b != 0:
            print(f"Wynik dzielenia: {a / b}")
        else:
            print("Nie można dzielić przez zero!")

    kontynuuj = input("Czy chcesz kontynuować? (tak/nie): ")
    if kontynuuj.lower() != "tak":
        print("Do zobaczenia!")
        
            # break = kończy pętlę
        break
          