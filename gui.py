import tkinter as tk
from tkinter import ttk
from enigma import Enigma

# Assurez-vous que les classes Enigma, Rotor, Reflector, et Plugboard sont définies comme précédemment.

class EnigmaGUI:
    def __init__(self, master):
        self.master = master
        master.title("Machine Enigma")

        # Configuration initiale des rotors et du plugboard (exemple simplifié)
        self.rotor_configurations = [
            ('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q', 'A'),
            ('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E', 'A'),
            ('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V', 'A')
        ]
        self.reflector_wiring = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
        self.plugboard_wiring = 'AX BZ CW DY EJ FG HL IM KU NQ OP RT SV'

        self.enigma_machine = Enigma(self.rotor_configurations, self.reflector_wiring, self.plugboard_wiring)

        # Message Entry
        self.message_label = ttk.Label(master, text="Message:")
        self.message_label.pack()
        self.message_entry = ttk.Entry(master, width=50)
        self.message_entry.pack()

        # Boutons pour chiffrer et déchiffrer
        self.encrypt_button = ttk.Button(master, text="Chiffrer", command=self.encrypt_message)
        self.encrypt_button.pack(pady=5)
        self.decrypt_button = ttk.Button(master, text="Déchiffrer", command=self.decrypt_message)
        self.decrypt_button.pack(pady=5)

        # Zone d'affichage du résultat
        self.result_label = ttk.Label(master, text="Résultat:")
        self.result_label.pack()
        self.result_text = tk.Text(master, height=10, width=50)
        self.result_text.pack()

    def encrypt_message(self):
        original_message = self.message_entry.get()
        encrypted_message = self.enigma_machine.encrypt(original_message)
        self.result_text.delete(1.0, tk.END)  # Nettoie la zone de texte
        self.result_text.insert(tk.END, encrypted_message)  # Affiche le message chiffré
        self.enigma_machine = Enigma(self.rotor_configurations, self.reflector_wiring, self.plugboard_wiring)


    def decrypt_message(self):
        original_message = self.message_entry.get()
        decrypted_message = self.enigma_machine.encrypt(original_message)  # Même fonction pour chiffrer et déchiffrer
        self.result_text.delete(1.0, tk.END)  # Nettoie la zone de texte
        self.result_text.insert(tk.END, decrypted_message)  # Affiche le message déchiffré
        self.enigma_machine = Enigma(self.rotor_configurations, self.reflector_wiring, self.plugboard_wiring)
        

def main():
    root = tk.Tk()
    app = EnigmaGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
