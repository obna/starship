from Starship import Starship
from Battleship import Battleship
from Equip import Equip as eq
print('-----------------------------------------------------')
print('>>> Starship 1 Details <<<')
liset = Starship('Tenno', 'Landing Craft', '100%')
liset.print()

print('-----------------------------------------------------')
print('>>> Battleship 1  Details <<<')
mantis = Battleship('Sentient', 'Railjack', '100', 'akara', 3)
mantis.print()
print('\n>>> Battleship 1 Element Upgrade <<<')
mantis.equip_element('earth')
print('\n>>> Battleship 1 Final <<<')
mantis.print()

print('-----------------------------------------------------')
print('>>> Battleship 2  Details <<<')
nightwave = Battleship('Grineer', 'Railjack','93','fufu',4)
nightwave.print()
print('\n>>> Battleship 2  Mod Upgrade <<<')
nightwave.equip_mods()
print('\n>>> Battleship 2  Final <<<')
nightwave.print()
print('-----------------------------------------------------')