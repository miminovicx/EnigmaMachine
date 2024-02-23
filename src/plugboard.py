class Plugboard:
    def __init__(self, wiring=''):
        self.wiring_map = self.create_wiring_map(wiring)

    def create_wiring_map(self, wiring):       
        wiring_map = {chr(i + ord('A')): chr(i + ord('A')) for i in range(26)}
        for pair in wiring.split():
            if len(pair) == 2:
                wiring_map[pair[0]] = pair[1]
                wiring_map[pair[1]] = pair[0]
        return wiring_map

    def encrypt(self, char):        
        return self.wiring_map.get(char, char)

    def set_wiring(self, wiring):
        self.wiring_map = self.create_wiring_map(wiring)
