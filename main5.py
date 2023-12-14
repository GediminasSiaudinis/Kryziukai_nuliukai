while not spejimai.ar_lygiosios() and not spejimai.ar_laimejo_X() and not spejimai.ar_laimejo_O():
    try:
        pasirinkimas = int(input("Iveskite X ejima "))
        spejimai.prideti_X_spejima(pasirinkimas)
        spejimai.atvaizduoti()
        if spejimai.ar_laimejo_X() == 1:
            print("X laimejo!")
            break

        if spejimai.ar_lygiosios():
            print("Lygiosios")
            break

        pasirinkimas = int(input("Iveskite O ejima "))
        spejimai.prideti_O_spejima(pasirinkimas)
        spejimai.atvaizduoti()
        if spejimai.ar_laimejo_O() == 1:
            print("O laimejo!")
            break

        if spejimai.ar_lygiosios():
            print("Lygiosios")
            break

    except ValueError:
        print("Invalid input! Please enter a valid number.")
