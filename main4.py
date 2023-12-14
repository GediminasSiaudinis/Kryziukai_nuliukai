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

    def ar_lygiosios(self):
        # for x in self.spejimai:
        visi_x_o = all(elem == "X" or elem == "Y" for elem in self.spejimai)
        # if visi_x_o is True:
        #     print("Lygiosios")
        # else:
        #     pass



    def prideti_X_spejima(self, pasirinkimai):
        while True:
            try:
                pasirinkimai2 = pasirinkimasX(pasirinkimai)
                pasirinkimai = self.spejimai.index(pasirinkimai)
                self.spejimai[pasirinkimai] = "X"
            except ValueError:
                print("_____________________________________________________________________________")
                print("Tokio pasirinkimo nera arba toks skaicius jau buvo, pasirinkite kita varianta")
                print("______________________________________________________________________________")
                break
            else:
                break

    def prideti_O_spejima(self, pasirinkimai):
        try:
            pasirinkimai2 = pasirinkimasO(pasirinkimai)
            pasirinkimai = self.spejimai.index(pasirinkimai)
            self.spejimai[pasirinkimai] = "O"
        except ValueError:
            print("Tokio pasirinkimo nera arba toks skaicius jau buvo, pasirinkite kita varianta")
        else:
            ...

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
            if self.spejimai[0] == "X" and self.spejimai[1] == "X" and self.spejimai[2] == "X":
                print("X laimejo")
                return 1
                break
            elif self.spejimai[3] == "X" and self.spejimai[4] == "X" and self.spejimai[5] == "X":
                print("X laimejo")
                return 1
                break
            elif self.spejimai[6] == "X" and self.spejimai[7] == "X" and self.spejimai[8] == "X":
                print("X laimejo")
                return 1
                break
            elif self.spejimai[0] == "X" and self.spejimai[3] == "X" and self.spejimai[6] == "X":
                print("X laimejo")
                return 1
                break
            elif self.spejimai[1] == "X" and self.spejimai[4] == "X" and self.spejimai[7] == "X":
                print("X laimejo")
                return 1
                break
            elif self.spejimai[2] == "X" and self.spejimai[5] == "X" and self.spejimai[8] == "X":
                print("X laimejo")
                return 1
                break
            elif self.spejimai[0] == "X" and self.spejimai[4] == "X" and self.spejimai[8] == "X":
                print("X laimejo")
                return 1
                break
            elif self.spejimai[2] == "X" and self.spejimai[4] == "X" and self.spejimai[6] == "X":
                print("X laimejo")
                return 1
                break
    def ar_laimejo_O(self):
        for x in self.spejimai:
            if self.spejimai[0] == "O" and self.spejimai[1] == "O" and self.spejimai[2] == "O":
                print("O laimejo")
                return 1
                break
            elif self.spejimai[3] == "O" and self.spejimai[4] == "O" and self.spejimai[5] == "O":
                print("O laimejo")
                return 1
                break
            elif self.spejimai[6] == "O" and self.spejimai[7] == "O" and self.spejimai[8] == "O":
                print("O laimejo")
                return 1
                break
            elif self.spejimai[0] == "O" and self.spejimai[3] == "O" and self.spejimai[6] == "O":
                print("O laimejo")
                return 1
                break
            elif self.spejimai[1] == "O" and self.spejimai[4] == "O" and self.spejimai[7] == "O":
                print("O laimejo")
                return 1
                break
            elif self.spejimai[2] == "O" and self.spejimai[5] == "O" and self.spejimai[8] == "O":
                print("O laimejo")
                return 1
                break
            elif self.spejimai[0] == "O" and self.spejimai[4] == "O" and self.spejimai[8] == "O":
                print("O laimejo")
                return 1
                break
            elif self.spejimai[2] == "O" and self.spejimai[4] == "O" and self.spejimai[6] == "O":
                print("O laimejo")
                return 1
                break

spejimai = Spejimai()

spejimai.atvaizduoti()

while True:
    try:
        spejimai.ar_lygiosios()
        if spejimai.ar_lygiosios() is True:
            break
        pasirinkimas = int(input("Iveskite X ejima "))
        spejimai.prideti_X_spejima(pasirinkimas)
        spejimai.atvaizduoti()
        spejimai.ar_laimejo_X()

        if spejimai.ar_laimejo_X() == 1:
            break
        spejimai.ar_lygiosios()
        if spejimai.ar_lygiosios() is True:
            break
        pasirinkimas = int(input("Iveskite O ejima "))
        spejimai.prideti_O_spejima(pasirinkimas)
        spejimai.atvaizduoti()
        spejimai.ar_laimejo_O()
        spejimai.ar_lygiosios()
        if spejimai.ar_laimejo_O() == 1:
            break
    except:
        print("Lygiosios")
    # else:
    #     print("lygiosios")