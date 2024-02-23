from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector

class Enigma:
    def __init__(self, rotor_configurations, reflector_wiring, plugboard_wiring):
        self.rotors = [Rotor(wiring, notch, position) for wiring, notch, position in rotor_configurations]
        self.reflector = Reflector(reflector_wiring)
        self.plugboard = Plugboard(plugboard_wiring)

    def encrypt(self, message):
        encrypted_message = ""
        
        for char in message.upper():
            if char.isalpha():
                char = self.plugboard.encrypt(char)

                for rotor in self.rotors:
                    char = rotor.encrypt_forward(char)
                
                char = self.reflector.reflect(char)
                
                for rotor in reversed(self.rotors):
                    char = rotor.encrypt_backward(char)
                
                char = self.plugboard.encrypt(char)
                
                self.rotors[0].rotate()
                for i in range(len(self.rotors) - 1):
                    if self.rotors[i].position == ord(self.rotors[i].notch) - ord('A'):
                        self.rotors[i+1].rotate()

            encrypted_message += char
        
        return encrypted_message
