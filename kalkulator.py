import math

def pitagorov_izrek():
    print("Kalkulator Pitagorovega izreka")
    print("Izberite eno od možnosti:")
    print("1. Izračun hipotenuze (c)")
    print("2. Izračun katete (a ali b)")
    print("3. Izhod")

    izbira = input("Vaša izbira (1/2/3): ")

    if izbira == "1":
        a = float(input("Vnesite dolžino katete a: "))
        b = float(input("Vnesite dolžino katete b: "))
        c = math.sqrt(a**2 + b**2)
        print(f"Dolžina hipotenuze (c) je {c}")
    elif izbira == "2":
        c = float(input("Vnesite dolžino hipotenuse (c): "))
        kateta = float(input("Vnesite dolžino znane katete (a ali b): "))
        if kateta > c:
            print("Napaka: Dolžina katete ne sme biti večja od hipotenuse.")
        else:
            preostala_kateta = math.sqrt(c**2 - kateta**2)
            print(f"Dolžina preostale katete je {preostala_kateta}")
    elif izbira == "3":
        return
    else:
        print("Neveljavna izbira. Prosimo, izberite 1, 2 ali 3.")

    pitagorov_izrek()

if __name__ == "__main__":
    pitagorov_izrek()
