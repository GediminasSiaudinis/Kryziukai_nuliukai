class pasirinkimai:
    def __init__(self, pasirinkimai):
        self.pasirinkimai = pasirinkimai

    def __repr__(self):
        return f'{self.pasirinkimai}'

class pasirinkimasX(pasirinkimai):
    def __init__(self, pasirinkimai):
        self.pasirinkimai = pasirinkimai

    def __repr__(self):
        return f'{self.pasirinkimai}'


class pasirinkimasO(pasirinkimai):
    def __init__(self, pasirinkimai):
        self.pasirinkimai = pasirinkimai

    def __repr__(self):
        return f'{self.pasirinkimai}'

class Spejimai:
    def __init__(self):
        self.spejimai = [7, 8, 9, 4, 5, 6, 1, 2, 3]

    def prideti_X_spejima(self, pasirinkimai):
        pasirinkimai2 = pasirinkimasX(pasirinkimai)
        pasirinkimai = self.spejimai.index(pasirinkimai)
        self.spejimai[pasirinkimai] = "X"

    def prideti_O_spejima(self, pasirinkimai):
        pasirinkimai2 = pasirinkimasO(pasirinkimai)
        pasirinkimai = self.spejimai.index(pasirinkimai)
        self.spejimai[pasirinkimai] = "O"

    def atvaizduoti(self):
        count = 0
        for x in self.spejimai:
            print(f'| {x} |', end="")
            count += 1
            if count == 3:
                count = 0
                print()
        return self.spejimai


    def ar_laimejo_X(self):
        for x in self.spejimai:
            if self.spejimai[0] and self.spejimai[1] and self.spejimai[2] == "X":
                print("X laimejo")
            elif self.spejimai[3] and self.spejimai[4] and self.spejimai[5] == "X":
                print("X laimejo")
            elif self.spejimai[6] and self.spejimai[7] and self.spejimai[8] == "X":
                print("X laimejo")
            elif self.spejimai[0] and self.spejimai[3] and self.spejimai[6] == "X":
                print("X laimejo")
            elif self.spejimai[1] and self.spejimai[4] and self.spejimai[7] == "X":
                print("X laimejo")
            elif self.spejimai[2] and self.spejimai[5] and self.spejimai[8] == "X":
                print("X laimejo")
            elif self.spejimai[0] and self.spejimai[4] and self.spejimai[8] == "X":
                print("X laimejo")
            elif self.spejimai[2] and self.spejimai[4] and self.spejimai[6] == "X":
                print("X laimejo")
            break

# if self.spejimai[0] and self.spejimai[1] and self.spejimai[2] is isinstance(x, pasirinkimasX):

# and self.spejimai[1] and self.spejimai[2]


spejimai = Spejimai()


while True:
    pasirinkimas = int(input("Iveskite X ejima "))
    spejimai.prideti_X_spejima(pasirinkimas)
    spejimai.atvaizduoti()
    spejimai.ar_laimejo_X()
    pasirinkimas = int(input("Iveskite O ejima "))
    spejimai.prideti_O_spejima(pasirinkimas)
    spejimai.atvaizduoti()
    # spejimai.ar_laimejo_X()


