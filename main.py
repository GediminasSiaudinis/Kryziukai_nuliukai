# pasirinkimas = int(
#     input("Jei norite iveste pajamas - 1 Jei islaidas - 2 Jei paziureti balansa - 3 Jei iseiti - 4 Jei ataskaita - 5 "))

# septintas = print("|7|", end="")
# astuntas = print("|8|", end="")
# devintas = print("|9|")
# ketvirtas = print("|4|", end="")
# penktas = print("|5|", end="")
# sestas = print("|6|")
# pirmas = print("|1|", end="")
# antras = print("|2|", end="")
# trecias = print("|3|")
# pasirinkimasX = int(input("Iveskite X langeli: "))
pirmas = 1
antras = 2
trecias = 3
ketvirtas = 4
penktas = 5
sestas = 6
septintas = 7
astuntas = 8
devintas = 9
opcijos = [pirmas, antras, trecias, ketvirtas, penktas, sestas, septintas, astuntas, devintas]
opcijos2 = opcijos
class pasirinkimasX:
    def __init__(self):
        self.zurnalas = []

    # def spausdinti(self):
class pasirinkimasO:
    def __init__(self):
        self.zurnalas = []

print(opcijos)
pasirinkimas1 = int(input("Pasirinkite X ejima "))
opcijos[pasirinkimas1 - 1] = "X"
print(opcijos)
print(opcijos2)



