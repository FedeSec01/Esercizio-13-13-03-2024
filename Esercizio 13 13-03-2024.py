'''
Nome: Federico
Cognome: Russo
Data e ora: 13-03-2024 10:17
Obiettivo:
'''
import matplotlib.pyplot as plt
import numpy as np

class PoligonoRegolare:
    def __init__(self, num_lati, lunghezza_lato):
        self.num_lati = num_lati
        self.lunghezza_lato = lunghezza_lato

    def calcola_area(self):
        apotema = self.lunghezza_lato / (2 * np.tan(np.pi / self.num_lati))
        return (self.num_lati * self.lunghezza_lato * apotema) / 2

    def calcola_perimetro(self):
        return self.num_lati * self.lunghezza_lato

    def disegna(self):
        angolo_incremento = 2 * np.pi / self.num_lati
        angoli = [i * angolo_incremento for i in range(self.num_lati)]
        x = [self.lunghezza_lato * np.cos(angolo) for angolo in angoli]
        y = [self.lunghezza_lato * np.sin(angolo) for angolo in angoli]
        x.append(x[0])
        y.append(y[0])
        plt.plot(x, y, 'b-')
        plt.axis('equal')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(f"Poligono regolare con {self.num_lati} lati")
        plt.show()

def richiedi_dato(descrizione):
    while True:
        dato = input(f"Inserisci {descrizione} o digita 'non lo so': ")
        if dato.lower() == "non lo so":
            return None
        try:
            valore = float(dato)
            if valore <= 0:
                print("Per favore, inserisci un numero maggiore di zero.")
                continue
            return valore
        except ValueError:
            print("Per favore, inserisci un numero valido.")

def main():
    while True:
        print("\nScegli un poligono regolare:")
        print("1. Triangolo")
        print("2. Quadrato")
        print("3. Pentagono")
        print("4. Esagono")
        print("5. Esci")
        scelta = input("Inserisci il numero della tua scelta: ")

        if scelta == "5":
            print("Arrivederci!")
            break

        if scelta not in ["1", "2", "3", "4"]:
            print("Scelta non valida.")
            continue

        lato = richiedi_dato("la lunghezza del lato")
        if lato is None:
            print("Senza la lunghezza del lato non posso calcolare le proprietà della figura.")
            continue

        num_lati = int(scelta) + 2  # Modifica qui

        poligono = PoligonoRegolare(num_lati, lato)

        print(f"Area: {poligono.calcola_area():.2f}")
        print(f"Perimetro: {poligono.calcola_perimetro():.2f}")

        poligono.disegna()

if __name__ == "__main__":
    main()
s