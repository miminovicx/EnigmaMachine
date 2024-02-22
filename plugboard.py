class Plugboard:
    # Initialise le plugboard avec une configuration de câblage.
    def __init__(self, wiring=''):
        self.wiring_map = self.create_wiring_map(wiring)

    # Crée une carte de câblage à partir de la configuration donnée.
    def create_wiring_map(self, wiring):       
        wiring_map = {chr(i + ord('A')): chr(i + ord('A')) for i in range(26)}  # Initialisation avec identité
        for pair in wiring.split():
            if len(pair) == 2:
                wiring_map[pair[0]] = pair[1]
                wiring_map[pair[1]] = pair[0]
        return wiring_map

    # Chiffre une lettre en passant par le plugboard.
    def encrypt(self, char):        
        return self.wiring_map.get(char, char)  # Retourne la lettre échangée ou la lettre originale

    # En cas de redéfinition du câblage du plugboard.
    def set_wiring(self, wiring):
        self.wiring_map = self.create_wiring_map(wiring)
