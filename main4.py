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
        self.spejimai = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def prideti_X_spejima(self, pasirinkimai):
        pasirinkimai2 = pasirinkimasX(pasirinkimai)
        self.spejimai[pasirinkimai - 1] = "X"

    def prideti_O_spejima(self, pasirinkimai):
        pasirinkimai2 = pasirinkimasO(pasirinkimai)
        self.spejimai[pasirinkimai - 1] = "O"

    def atvaizduoti(self):
        count = 0
        for x in self.spejimai:
            print(f'| {x} |', end="")
            count += 1
            if count == 3:
                count = 0
                print()
        return self.spejimai

    def balansas(self):
        suma = 0
        for x in self.spejimai:
            if isinstance(x, pasirinkimasX):
                suma += x.suma
            elif isinstance(x, pasirinkimasO):
                suma -= x.suma
        return suma



spejimai = Spejimai()


while True:
    pasirinkimas = int(input("Iveskite X ejima "))
    spejimai.prideti_X_spejima(pasirinkimas)
    spejimai.atvaizduoti()
    pasirinkimas = int(input("Iveskite O ejima "))
    spejimai.prideti_O_spejima(pasirinkimas)
    spejimai.atvaizduoti()


