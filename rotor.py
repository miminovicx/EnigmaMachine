class Rotor:
    def __init__(self, wiring, notch, initial_position='A'):
        self.wiring = wiring
        self.notch = notch
        self.position = ord(initial_position) - ord('A')  # Convertir la position initiale en un décalage (0-25).

    def rotate(self):
        self.position = (self.position + 1) % 26
        return self.wiring[self.position] in self.notch

    # Convertit la lettre en position (0-25), applique le décalage, puis convertit en retour en lettre.
    def encrypt_forward(self, char):
        index = (ord(char) - ord('A') + self.position) % 26
        return self.wiring[index]

    # Chiffre une lettre en passant dans le sens inverse du rotor.
    def encrypt_backward(self, char):
        index = self.wiring.index(char)
        return chr((index - self.position + 26) % 26 + ord('A'))

    def set_position(self, position):
        self.position = ord(position) - ord('A')
