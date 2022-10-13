from Starship import Starship  # had to do this for class use not module use?


class Transport(Starship):
    skin = ''

    def __init__(self, faction, c_pit, vuln, dock, kind, pilot):
        self.__landing_pad = dock
        self.__content = kind  # prison, vip, cargo
        self.__guide = pilot
        super(Transport, self).__init__(faction, c_pit, vuln)

    def get_landing_pad(self):
        return self.__landing_pad

    def set_landing_pad(self, dock):
        self.__landing_pad = dock

    def get_content(self):
        return self.__content

    def set_content(self, kind):
        self.__content = kind

    def get_guide(self):
        return self.__guide

    def set_guide(self, pilot):
        self.__guide = pilot

    def transparent(self, facade):
        print('Initializing change in appearance sequence...\n\tSystem Restarting')
        print('.....\n..........\n\tSystem Rebooted')
        if facade == 1:
            self.skin = 'Camo'
        elif facade == 2:
            self.skin = 'Translucent'
        elif facade == 3:
            self.skin = 'Observable'
        return self.skin

    def print(self):
        super(Transport, self).print()
        print('Transport Docked ETA:', self.__landing_pad)
        print('Transport Contract:', self.__content)
        print('Pilot Status:', self.__guide)
        if self.skin != '':
            print('Spectrum Status:', self.skin)
