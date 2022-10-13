from Starship import Starship
class Medical(Starship):
    #two private instance variables
    #one new method
    def __init__(self, faction, c_pit, vuln, cryo, support, organ):
        self.__longevity = cryo
        self.__life_capsules = support
        self.__initiate_incubator = organ
        super(Medical, self).__init__(faction, type, vuln)
