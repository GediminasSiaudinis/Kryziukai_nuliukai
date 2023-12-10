sarasas = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while True:
    pasirinkimasX = int(input("Iveskite X ejima "))
    sarasas[pasirinkimasX - 1] = "X"
    print(sarasas)
    # if pasirinkimasX
    pasirinkimasO = int(input("Iveskite O ejima "))
    sarasas[pasirinkimasO - 1] = "O"
    print(sarasas)