class DiagramKosci:
    def __init__(self, wynik_rzutu):
        self.diagram_kosci = self.generuj_diagram_kosci(wynik_rzutu)

    WYGLAD_KOSCI = {
        1: (
            "-----------",
            "|         |",
            "|    0    |",
            "|         |",
            "-----------",
        ),
        2: (
            "-----------",
            "| 0       |",
            "|         |",
            "|       0 |",
            "-----------",
        ),
        3: (
            "-----------",
            "| 0       |",
            "|    0    |",
            "|       0 |",
            "-----------",
        ),
        4: (
            "-----------",
            "| 0     0 |",
            "|         |",
            "| 0     0 |",
            "-----------",
        ),
        5: (
            "-----------",
            "| 0     0 |",
            "|    0    |",
            "| 0     0 |",
            "-----------",
        ),
        6: (
            "-----------",
            "| 0  0  0 |",
            "| 0  0  0 |",
            "| 0  0  0 |",
            "-----------",
        )
    }
    WYSOKOSC = len(WYGLAD_KOSCI[1])
    SZEROKOSC = len(WYGLAD_KOSCI[1][0])
    SEPARATOR = "  |  "

    def generuj_diagram_kosci(self, wynik_rzutu):
        twarz_kosci = []
    # pobieram z listy winik_rzutu odpowiadające WYGLAD_KOSCI i zapisauje do twarz_kosci
        for wartosc in wynik_rzutu:
            twarz_kosci.append(self.WYGLAD_KOSCI[wartosc])

        rzedy_twarzy_kosci = []
        for rzedy in range(self.WYSOKOSC):
            komponent = []
            for x in twarz_kosci:
                komponent.append(x[rzedy])
            ciag = self.SEPARATOR.join(komponent)
            rzedy_twarzy_kosci.append(ciag)

        szerokosc = len(rzedy_twarzy_kosci[0])
        naglowek = "WYNIK".center(szerokosc,"-")

        diagram_kosci = "\n".join([naglowek] + rzedy_twarzy_kosci)
        return diagram_kosci

    def wyswietl_wynik(self):
        print(f"\n{self.diagram_kosci}")