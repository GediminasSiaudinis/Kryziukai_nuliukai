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

    def istrinti(self):
        self.spejimai = [7, 8, 9, 4, 5, 6, 1, 2, 3]

    def ar_lygiosios(self):
        # for x in self.spejimai:
        if all(elem == "X" or elem == "O" for elem in self.spejimai) is True:
            return 1
            # for x in self.spejimai:
        #     suma = 100
        #     if x == "O" or x == "X":
        #         suma += 1
        #         if suma == 109:
        #             return 1
        # if visi_x_o is True:
        #     return 1
        # else:
        #     pass
    # def ar_tinkamas(self, pasirinkimai):
    #     # if self.spejimai.index(pasirinkimai) == "O" or self.spejimai.index(pasirinkimai) == "X" or self.spejimai.index(pasirinkimai) == 0:
    #     #     return True
    #     # else:
    #     #     return False
    #     try:
    #         self.spejimai.index(pasirinkimai)
    #         return True
    #     except:
    #         return False

    def prideti_X_spejima(self, pasirinkimai):
        # while True:
            # try:
        # pasirinkimai2 = pasirinkimasX(pasirinkimai)
        pasirinkimai = self.spejimai.index(pasirinkimai)
        self.spejimai[pasirinkimai] = "X"
            # except ValueError:
            #     print("_____________________________________________________________________________")
            #     print("Tokio pasirinkimo nera arba toks skaicius jau buvo, pasirinkite kita varianta")
            #     print("______________________________________________________________________________")
            #     return
            # else:
            #     break

    def prideti_O_spejima(self, pasirinkimai):
        # try:
        pasirinkimai2 = pasirinkimasO(pasirinkimai)
        pasirinkimai = self.spejimai.index(pasirinkimai)
        self.spejimai[pasirinkimai] = "O"
        # except ValueError:
        #     print("Tokio pasirinkimo nera arba toks skaicius jau buvo, pasirinkite kita varianta")
        # else:
        #     ...

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

# def zaisti_zaidima():
#     spejimai_zaisti = Spejimai()

# zaisti_zaidima()

spejimai.atvaizduoti()

while True:
    # spejimai.ar_lygiosios()
    if spejimai.ar_lygiosios() == 1:
        print("Lygiosios")
        zaisti = input("Ar norite zaisti darkart? (taip/ne): ")
        if zaisti.lower() != 'taip':
            break
        else:
            spejimai.istrinti()
            continue

    # pasirinkimas = int(input("Iveskite X ejima "))
    # try:
    while True:
        try:
            pasirinkimas = int(input("Iveskite X ejima "))
            spejimai.spejimai.index(pasirinkimas)
            spejimai.prideti_X_spejima(pasirinkimas)
            break
        except ValueError:
            print("Tokio pasirinkimo nera arba toks skaicius jau buvo, pasirinkite kita varianta")
    # except ValueError:
        # while True:
        # if spejimai.ar_tinkamas(pasirinkimas) == True:
        # print("Tokio pasirinkimo nera arba toks skaicius jau buvo, pasirinkite kita varianta")
        # pasirinkimas = int(input("Iveskite X ejima "))
        # if spejimai.ar_tinkamas(pasirinkimas) == False:
        #     spejimai.prideti_X_spejima(pasirinkimas)
            # while spejimai.ar_tinkamas(pasirinkimas) == True:
            #     print("Tokio pasirinkimo nera arba toks skaicius jau buvo, pasirinkite kita varianta")
                # spejimai.prideti_X_spejima(pasirinkimas)
    # else:
    #     spejimai.prideti_X_spejima(pasirinkimas)

    spejimai.atvaizduoti()
    # spejimai.ar_laimejo_X()
    if spejimai.ar_laimejo_X() == 1:
        zaisti = input("Ar norite zaisti darkart? (taip/ne): ")
        if zaisti.lower() != 'taip':
            break
        else:
            spejimai.istrinti()
            continue
        # break

    if spejimai.ar_lygiosios() == 1:
        print("Lygiosios")
        zaisti = input("Ar norite zaisti darkart? (taip/ne): ")
        if zaisti.lower() != 'taip':
            break
        else:
            spejimai.istrinti()
            continue

    # pasirinkimas = int(input("Iveskite O ejima "))
    while True:
        try:
            pasirinkimas = int(input("Iveskite O ejima "))
            spejimai.spejimai.index(pasirinkimas)
            spejimai.prideti_O_spejima(pasirinkimas)
            break
        except ValueError:
            print("Tokio pasirinkimo nera arba toks skaicius jau buvo, pasirinkite kita varianta")
    spejimai.atvaizduoti()
    # spejimai.ar_laimejo_O()
    spejimai.ar_lygiosios()
    if spejimai.ar_laimejo_O() == 1:
        zaisti = input("Ar norite zaisti darkart? (taip/ne): ")
        if zaisti.lower() != 'taip':
            break
        else:
            spejimai.istrinti()
            continue
