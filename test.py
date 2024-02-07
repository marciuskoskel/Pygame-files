import math


class cal():  # Defineerib klassi
    def __init__(self, num1, num2):  # Defineerib konstruktor methodi a ja b jaoks.
        self.num1 = a
        self.num2 = b

    def liitmine(self):  # Defineerib liitmise funktsiooni.
        return self.num1 + self.num2

    def lahutamine(self):  # Defineerib lahutamise funktsiooni.
        return self.num1 - self.num2

    def korrutamine(self):  # Defineerib korrutamise funktsiooni
        return self.num1 * self.num2

    def jagamine(self):  # Defineerib jagamise funktsiooni.
        return self.num1 / self.num2

    def jaak(self):  # Defineerib jaagi funktsiooni.
        return self.num1 % self.num2

    def astendamine(self):  # Defineerib ruutjuure funktsiooni.
        return self.num1 ** self.num2
    def ruutjuur(self):  # Defineerib ruutjuure
        return math.sqrt(self.num1)


a = int(input("Sisesta esimene number: "))  # Kusib kasutajalt esimest numbrit mida sisestada.
b = int(input("Sisesta teine number: "))  # Kusib kasutajalt teist numbrit mida sisestada.

kalk = cal(a, b)
while True:
    def menu():  # Defineerib menu kus saab valida millist funktsiooni kasutada.
        x = (
            '1. Liitmine \n2. lahutamine\n3. korrutamine\n4. jagamine\n5. Jäägi leidmine\n6. Astendamine\n7. '
            'Ruutjuure leidmine ')
        print(x)  # Prindib x kus on näha millist funktsiooni valida.


    menu()
    valik = int(input('Sisesta üks valikutest: '))  # Kusib kasutajalt millist funktsiooni kasutada.
    if valik == 1:
        print("Vastus: ", kalk.liitmine())  # Kui kasutaja  valik on 1 siis on liitmine.
        break
    elif valik == 2:
        print("Vastus: ", kalk.lahutamine())  # Kui kasutaja valik on 2 siis on lahutamine
        break
    elif valik == 3:
        print("Vastus: ", kalk.korrutamine())  # Kui kasutaja valik on 3 siis on korrutamine
        break
    elif valik == 4:
        print("Vastus: ", kalk.jagamine())  # Kui kasutaja valik on 4 siis on jagamine
        break
    elif valik == 5:
        print("Vastus: ", kalk.jaak())  # Kui kasutaja valik on 5 siis on jaagi leidmine
        break
    elif valik == 6:
        print("Vastus: ", kalk.astendamine())  # Kui kasutaja valik on 6 siis on astendamine
        break
    elif valik == 7:  # Kui valik on 7 tuleb ruutjuure funktsioon
        print("Ruutjuur: ", kalk.ruutjuur())
        break
    elif valik == 0:  # Defineerib kui valik on 0 siis tuleb uus operaator vaha sisestada.
        print('Sisesta uuesti üks liitmise operaator')
        break
