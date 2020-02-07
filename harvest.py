############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.extend(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    muskmelon.add_pairing(["mint"])
    all_melon_types.append(muskmelon)

    casaba = MelonType("cas", 2003, "orange", False, False, "Casaba")
    casaba.add_pairing(["strawberries", "mint"])
    all_melon_types.append(casaba)

    crenshaw = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    crenshaw.add_pairing(["proscuitto"])
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType("yw", 2013, "yellow", False, True, 
                                  "Yellow Watermelon")
    yellow_watermelon.add_pairing(["ice cream"])
    all_melon_types.append(yellow_watermelon)

    return all_melon_types


def print_pairing_info(melon_types=make_melon_types()):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name} pairs with')

        for pair in melon.pairings:
            print(f'- {pair}')


def make_melon_type_lookup(melon_types=make_melon_types()):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}
    for melon in melon_types:
        melon_dict[melon.code] = melon

    return melon_dict


############
# Part 2   #
############


def process_melon_data(file_path):
    '''Process melon data, instantiate melon objects for all melons harvested. '''

    # Open and read data
    harvest_log = open(file_path)

    list_of_instance = []

    for line in harvest_log:
        line.rstrip()
        line_list = line.split()
        mel_type = line_list[5]
        shape = line_list[1]
        color = line_list[3]
        field = line_list[11]
        harvester = line_list[8]

        list_of_instance.append([mel_type, shape, color, field, harvester])

        list_of_objects = []

    for instance in list_of_instance:
        melon = Melon(instance[0], instance[1], instance[2], instance[3],
                      instance[4])

        list_of_objects.append(melon)

    return list_of_objects
        

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, mel_type, shape, color, field, harvester):
        self.mel_type = mel_type
        self.shape = shape
        self.color = color
        self.field = field
        self.harvester = harvester

    def is_sellable(self):
        return self.shape > 5 and self.color > 5 and self.field != 3





def make_melons():
    """Returns a list of Melon objects."""

    melon_list = []

    melon1 = Melon("yw", 8, 7, 2, "Sheila")
    melon_list.append(melon1)

    melon2 = Melon("yw", 3, 4, 2, "Sheila")
    melon_list.append(melon2)

    melon3 = Melon("yw", 9, 8, 3, "Sheila")
    melon_list.append(melon3)

    melon4 = Melon("cas", 10, 6, 35, "Sheila")
    melon_list.append(melon4)

    melon5 = Melon("cren", 8, 9, 35, "Michael")
    melon_list.append(melon5)

    melon6 = Melon("cren", 8, 2, 35, "Michael")
    melon_list.append(melon6)

    melon7 = Melon("cren", 2, 3, 4, "Michael")
    melon_list.append(melon7)

    melon8 = Melon("musk", 6, 7, 4, "Michael")
    melon_list.append(melon8)

    melon9 = Melon("yw", 7, 10, 3, "Sheila")
    melon_list.append(melon9)

    return melon_list


def get_sellability_report(melons=make_melons()):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable():
            print((f'Harvested by {melon.harvester} from Field {melon.field}')
                  + " (CAN BE SOLD)")
        else:
            print((f'Harvested by {melon.harvester} from Field {melon.field}')
                  + " (NOT SELLABLE)")


