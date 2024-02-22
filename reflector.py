class Reflector:
    # "YRUHQSLDPXNGOKMIEBFZCWVJAT" pour le réflecteur B.
    def __init__(self, wiring):
        self.wiring = wiring

    def reflect(self, char):
        # Trouve l'index de la lettre dans l'alphabet, puis trouve la lettre correspondante dans le câblage du réflecteur.
        index = ord(char) - ord('A')
        return self.wiring[index]
