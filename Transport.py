import Starship
class Transport(Starship):
    def __init__(self,to_carry):
        self.__landing_pad = to_carry


    def get_landing_pad(self):
        return self.__landing_pad
    def set_landing_pad(self,to_carry):
        self.__landing_pad = to_carry