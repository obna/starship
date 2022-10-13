from Starship import Starship  # had to do this for class use not module use?
from Equip import Equip


class Battleship(Starship):
    mod_added = False
    mod_name = ''
    mod_desc = ''

    def __init__(self, faction, type, vuln, name, crew):
        self.__craft = name
        self.__squad_size = crew
        super(Battleship, self).__init__(faction, type, vuln)

    def get_craft(self):
        return self.__craft

    def set_craft(self, name):
        self.__craft = name

    def get_squad_size(self):
        return self.__squad_size

    def set_squad_size(self, crew):
        self.__squad_size

    def get_shield_strength(self):
        return super(Battleship, self).get_shield_strength()

    def set_shield_strength(self, vuln):
        self.__shield_strength = vuln

    def equip_mods(self):
        print('Availible mods...\n#: NAME')
        Equip().get_mods()
        upgrade = int(input('\nEnter desired MOD number: '))
        self.mod_added = True
        print('Mod Equiped...')
        self.mod_name = Equip().get_mod_name(upgrade)
        print('\t',self.mod_name)
        self.mod_desc = Equip().get_mod_description(upgrade)

    def equip_element(self, element):
        stronger = len(element) * 3
        ss = super().get_shield_strength()
        super().set_shield_strength(stronger + int(ss))
        print('Warning ONE ELEMENT EQUIP per battleship\n\tCannot be undone')
        print('Equipping new element...', element.upper())
        print('Increasing shield strength...')
        print('Shield Strength added: '+str(stronger)+'%')

    def print(self):
        super(Battleship, self).print()
        print('Ship Name:', self.__craft.upper())
        print('Squad Size:', self.__squad_size, '/ 4')
        if self.mod_added:
            print('Upgrade:', self.mod_desc)
