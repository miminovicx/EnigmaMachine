from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector

class Enigma:
    def __init__(self, rotor_configurations, reflector_wiring, plugboard_wiring):
        self.rotors = [Rotor(wiring, notch, position) for wiring, notch, position in rotor_configurations]
        self.reflector = Reflector(reflector_wiring)
        self.plugboard = Plugboard(plugboard_wiring)

    # Chiffre ou déchiffre un message.
    def encrypt(self, message):
        encrypted_message = ""
        
        for char in message.upper():
            if char.isalpha():
                # Passage initial par le plugboard
                char = self.plugboard.encrypt(char)

                # Passage à travers les rotors (aller)
                for rotor in self.rotors:
                    char = rotor.encrypt_forward(char)
                
                # Réflexion dans le réflecteur
                char = self.reflector.reflect(char)
                
                # Passage à travers les rotors (retour)
                for rotor in reversed(self.rotors):
                    char = rotor.encrypt_backward(char)
                
                # Passage final par le plugboard
                char = self.plugboard.encrypt(char)
                
                # Rotation du rotor le plus à droite
                self.rotors[0].rotate()
                # Gérer la rotation des autres rotors en fonction de leur position de déclenchement
                for i in range(len(self.rotors) - 1):
                    if self.rotors[i].position == ord(self.rotors[i].notch) - ord('A'):
                        self.rotors[i+1].rotate()

            encrypted_message += char
        
        return encrypted_message
