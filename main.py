from Starship import Starship
from Battleship import Battleship
from Transport import Transport
from Medical import Medical

print('-----------------------------------------------------')
print('>>> Starship 1 Details <<<')
liset = Starship('Tenno', 'Landing Craft', '100')
liset.print()

print('-----------------------------------------------------')
print('>>> Battleship 1 Details <<<')
mantis = Battleship('Sentient', 'Railjack', '100', 'akara', 3)
mantis.print()
print('\n>>> Battleship 1 Element Upgrade <<<')
mantis.equip_element('earth')
print('\n>>> Battleship 1 Final <<<')
mantis.print()

print('-----------------------------------------------------')
print('>>> Battleship 2 Details <<<')
nightwave = Battleship('Grineer', 'Railjack', '93', 'fufu', 4)
nightwave.print()
print('\n>>> Battleship 2 Mod Upgrade <<<')
nightwave.equip_mods(3)
print('\n>>> Battleship 2 Final <<<')
nightwave.print()

print('-----------------------------------------------------')
print('>>> Transport 1 Details <<<')
ordis = Transport('Infested', 'Transport', '100', 'T-35 minutes', 'Prisoner', 'Auto-pilot(and crewed)')
ordis.print()
print('\n>>> Transport 2 Details <<<')
jotly = Transport('Infested', 'Transport', '100', 'T-0 minutes(docked)', 'VIP', 'Auto-pilot(and w/o crew)')
jotly.print()
print('\n>>> Transport 2 Stealth <<<')
jotly.transparent(2)
print('\n>>> Transport 2 Final <<<')
jotly.print()
print('-----------------------------------------------------')


print('>>> Medical 1 Details <<<')
xiphos = Medical('Corpus', 'Medical', '100', '200 years Phobos time remains', '3 vessels activated in field', 'Left Arm, 43.8% complete')
xiphos.print()
print('\n>>> Medical 2 Details <<<')
scimitar = Medical('Corpus', 'Medical', '100', '57 years Earth time remains', '1 vessels activated in ship','N/A')
scimitar.print()
print('\n>>> Medical 2 Generate <<<')
scimitar.revive('personal')
print('\n>>> Medical 2 Final <<<')
scimitar.print()
print('-----------------------------------------------------')
