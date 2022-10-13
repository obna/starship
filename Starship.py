class Starship:
    def __init__(self, faction, type, vuln):
        self.__commander = faction
        self.__compatible = type
        self.__shield_strength = vuln

    def get_commander(self):
        return self.__commander

    def set_commander(self, faction):
        self.__commander = faction

    def get_compatible(self):
        return self.__compatible

    def set_compatible(self, type):
        self.__compatible = type

    def get_shield_strength(self):
        return self.__shield_strength

    def set_shield_strength(self, vuln):
        self.__shield_strength = vuln

    def print(self):
        print('Officer Faction:', self.__commander)
        print('Ship Type:', self.__compatible)
        print('Shield strength: '+ str(self.__shield_strength)+'%')
