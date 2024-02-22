from enigma import Enigma

if __name__ == "__main__":
    # Configuration des rotors : (Câblage, Notch, Position initiale)
    rotor_configurations = [
        ('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q', 'A'),  # Rotor I
        ('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E', 'A'),  # Rotor II
        ('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V', 'A')   # Rotor III
    ]

    # Câblage du réflecteur
    reflector_wiring = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
    
    # Câblage du plugboard
    plugboard_wiring = 'AX BZ CW DY EJ FG HL IM KU NQ OP RT SV'

    # Initialisation de la machine Enigma
    enigma_machine = Enigma(rotor_configurations, reflector_wiring, plugboard_wiring)
    
    # Chiffrer un message
    encrypted_message = enigma_machine.encrypt('yanish')
    print(f'Encrypted Message: {encrypted_message}')
    
    # Pour déchiffrer, réinitialisez la machine à la même configuration initiale et chiffrez le message chiffré
    enigma_machine = Enigma(rotor_configurations, reflector_wiring, plugboard_wiring)
    decrypted_message = enigma_machine.encrypt(encrypted_message)
    print(f'Decrypted Message: {decrypted_message}')
