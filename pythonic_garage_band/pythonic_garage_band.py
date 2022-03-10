from abc import abstractmethod


class Musician:
    """
    this class is to handle common functionality which particular kinds of musicians will inherit
    """

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def __str__(self):
        pass

    def __repr__(self):
        return f"{self.name}"

    @abstractmethod
    def get_instrument(self):
        """
        returns a string for each musician
        """

        pass

    @abstractmethod
    def play_solo(self):
        """
        returns a string for each musician
        """

        pass


"""
Musician Subclass Tests
Each kind of Musician instance should have appropriate __str__ and __repr__ methods.
Each kind of Musician instance should have a get_instrument method that returns string.
Each kind of Musician instance should have a play_solo method that returns string.

"""


class Guitarist(Muscian):
    """
    this class named Guitarist inherts from Musician class
    """

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    """
    this class named Bassist inherts from Musician class
    """

    def __str__(self):
        return f"My name is {self.name} and I play bass"
        """ 
        returns string which is the name
        """

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"


class Band:
    instances = []

    def __init__(self, name, members=[]):
        self.name = name
        self.members = members
        self.__class__.instances.append(self)

    def __str__(self):
        """
        returns a string with  band name
        """

        return f"This is the {self.name} band"

    def __repr__(self):
        """
        returns a string for the name of the band name
        """

        return f"{self.name}"

    """ method that asks each member musician to play a solo, in the order they were added to band."""

    def play_solos(
        self,
    ):

        solos = []
        for el in self.members:
            solos = solos + [f"{el.play_solo()}"]
        return solos

    @classmethod
    def to_list(cls):
        """
        returns a list of previously created Band instances
        """

        return cls.instances
