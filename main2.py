sarasas = [1, 2, 3, 4, 5, 6, 7, 8, 9]

ieskomasis = int(input("Įveskite X ejima "))
ieskomasis2 = int(input("Įveskite O ejima "))

for x in range(0, 10):
        if x == ieskomasis:
            sarasas[ieskomasis - 1] = "X"
            print(sarasas)
            continue
# else:
#     print("Skaičius nerastas")

print("Programos pabaiga")