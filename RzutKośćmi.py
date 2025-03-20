from random import randint
from DiagramKości import DiagramKosci


def sprawdz_ilosc(wprowadz_ilosc):
    if wprowadz_ilosc in {1,2,3,4,5,6}:
        return wprowadz_ilosc
    else:
        print("Nie mamy aż tylu kości")
        exit()

def rzuty(zaakceptowana_ilosc):
    wynik_rzutu = []
    for _ in range(zaakceptowana_ilosc):
        rzut = randint(1,6)
        wynik_rzutu.append(rzut)
    return wynik_rzutu

# krok 1 - pobieram liczbę
wprowadz_ilosc = int(input("Wprowadź jaką ilością kości chcesz rzucić (od 1 do 6): "))
# krok 2 - sprawdzam funkcją sprawdz_ilosc czy wybrana liczba mieści się w przedziale i zapisuje do zmiennej zaakceptowana_ilosc
zaakceptowana_ilosc = sprawdz_ilosc(wprowadz_ilosc)
# krok 3 - losuje funkcją rzuty tylke ilość liczb wybranych i zapisuję do wynik_rzutu
wynik_rzutu = rzuty(zaakceptowana_ilosc)

#print(wynik_rzutu) test

# krok 4 - wykorzystuje klase DiagramKosci
diagram_kosci = DiagramKosci(wynik_rzutu = wynik_rzutu)
# krok 5 - pobieram wynik z funkcji wyswietl_wynik w module DiagramKosci
diagram_kosci.wyswietl_wynik()