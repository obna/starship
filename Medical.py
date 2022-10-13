from Starship import Starship


class Medical(Starship):
    health_kit = ''
    def __init__(self, faction, c_pit, vuln, cryo, support, organ):
        self.__longevity = cryo
        self.__life_capsules = support
        self.__initiate_incubator = organ
        super(Medical, self).__init__(faction, c_pit, vuln)

    def get_longevity(self):
        return self.__longevity

    def set_longevity(self, cryo):
        self.__longevity = cryo

    def get_life_cap(self):
        return self.__life_capsules

    def set_life_cap(self, support):
        self.__life_capsules = support

    def get_organ(self):
        return self.__initiate_incubator

    def set_organ(self, organ):
        self.__initiate_incubator = organ

    def revive(self, grim):
        print('Commence Revive...')
        if grim.lower() == 'personal':
            print('....Respawned')
            self.health_kit = 'me'
        if grim.lower == 'member':
            print('Hold for 10 seconds....')
            self.health_kit = 'them'
        return self.health_kit


    def print(self):
        super(Medical, self).print()
        print('Cryogenic capabilities:', self.__longevity)
        print('Life Capsules Generated:', self.__life_capsules)
        print('Organ and Status:', self.__initiate_incubator)
        if self.health_kit == 'me':
            print('Revive has been used for: personal')
        elif self.health_kit == 'them':
            print('Revive has been used for: member')
        else:
            print('No revive issued')
