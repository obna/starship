class Equip():
    def __init__(self):
        pass

    mods = {
        1: ['ADAPT', 'Adaptation: +Increases damage resistance to the last damage type received'],
        2: ['AUX', 'Auxiliary Power: +Increases Maximum Energy'],
        3: ['DEFENSE', 'Superior Defenses: +Increases Shield Recharge Rate'],
        4: ['ENEMY', 'Enemy Sense: +Pinpoints enemy locations on minimap'],
        5: ['ENERGY', 'Energy Inversion: +Increases Shield Capacity'],
        6: ['FORM', 'Streamlined Form: +Increases weapon switch speed, Increases slide speed, Reduces friction'],
        7: ['RAPID', 'Vigilante Armaments: +Increases multishot'],
        8: ['RETRIBUTION', 'Retribution: +Adds chance to do Functional damage to attackers that damage your shields'],
        9: ['SPEED', 'Hyperion Thrusters: +Increases Flight Speed']
    }

    def get_mods(self):
        # if type.lower() == 'mods':
        for k, v in self.mods.items():
            print(str(k) + ': ' + v[0])

    def get_mod_name(self, k):
        return str(self.mods[k][0])

    def get_mod_description(self, k):
        return str(self.mods[k][1])
