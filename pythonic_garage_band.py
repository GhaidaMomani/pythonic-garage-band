# base class or parent class

def read_file(file):
    """F() to take data from band.txt file"""
    with open(file, 'r') as f:
        template = (f.read())
        return template

band_data = read_file("band.txt")

class Musician:
    """
    Parent class to all musicians. Parent to Gutarist, Bassist and Drummer classes has:
    __init__ - method which creates role and instrument attributes for the class
    based on given function parameters, and append the new obj instance tothe members array
    __str__ - string with the "role" of the obj instance
    __repr__ - string with the "role" of th eobj instance
    play_solo - string representing that the instance of this class playing solo
    get_instrument - returns a string with instrument that was created upon the obj initiation
    """

    members = []

    def __init__(self, role, instrument):
        self.role = role
        self.instrument = instrument
        self.__class__.members.append(self)

    def __str__(self):
        return f'I am a {self.role}'


    def __repr__(self):
        return self.role

    def play_solo(self):
        return f'{self.role} is playing solo on the {self.instrument}'


    def get_instrument(self):
        return self.instrument


class Guitarist(Musician):
    """Class which creates new guitarist and inherits all it's properties from
    the Musician class"""

    pass

class Bassist(Musician):
    """Class which creates new bassist and inherits all it's properties from
    the Musician class"""

    pass

class Drummer(Musician):
    """Class which creates new drummer and inherits all it's properties from
    the Musician class"""

    pass



class Band:

    """
    Class which creates a Band instance with these class methods:
    __init__, __str__, __repr__, play_solos, to_list, create_from_data -
    """

    all = []


    def __init__(self, name, members=[]):
        """
        Method which creates name of the band and its members
        based on given function parameters, and append the new obj instance to the "all" array
        """
        self.name = name
        self.members = members
        self.__class__.all.append(self)


    def play_solos(self):
        """
        Returns string that represents all members of the band playing their solos based on the
        order they were added to the band
        """

        solos = ''
        for el in self.members:
            solos += f'{el.play_solo()}\n'
        return solos[:-1]


    def __str__(self):
        """string with the "name" of the obj instance"""

        return ("We are the " + self.name)

    def __repr__(self):
        """string with the "name" of the obj instance"""

        return ("This is the " + self.name)

    @classmethod
    def to_list(cls):
        """Returns all Band instances that were created"""

        return cls.all

    @staticmethod
    def create_from_data(data):
        """
        Returns formatted data from the given data that can be used to create an instance
        of the Band
        """

        members = []
        parsed_data = data.split('\n')
        band_name = parsed_data[0]

        for el in parsed_data[1:len(parsed_data)-1]:

            musician_data = el.split(",")

            if musician_data[0] == "Bassist":
                members.append(Bassist(musician_data[0], musician_data[1]))

            elif musician_data[0] == "Guitarist":
                members.append(Guitarist(musician_data[0], musician_data[1]))

            elif musician_data[0] == "Drummer":
                members.append(Drummer(musician_data[0], musician_data[1]))

            else:
                return f"{musician_data[0]} doesn't exists in DB"
        return [band_name, members]

band_data_formatted = Band.create_from_data(band_data)
new_band = Band(band_data_formatted[0], band_data_formatted[1])
new_band2 = Band(band_data_formatted[0], band_data_formatted[1])

print('\n'+ repr(new_band.members) + '\n')
print(str(new_band) + '\n')
print(new_band.play_solos() + '\n')
print(Band.to_list(), '\n')