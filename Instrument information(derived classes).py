class Instrument:
    def __init__(self, name, manufacturer, year_built, cost):
        self.name = name
        self.manufacturer = manufacturer
        self.year_built = year_built
        self.cost = cost

    def print_info(self):
        print('Instrument Information:')
        print('   Name:', self.name)
        print('   Manufacturer:', self.manufacturer)
        print('   Year built:', self.year_built)
        print('   Cost:', self.cost)


class StringInstrument(Instrument):
    # TODO: Define constructor with attributes:
    #       name, manufacturer, year_built, cost, num_strings, num_frets
    def __init__(self, name, manufacturer, year_built, cost, num_strings, num_frets):
        Instrument.__init__(self, name, manufacturer, year_built, cost)
        self.num_strings = num_strings
        self.num_frets = num_frets


if __name__ == "__main__":
    instrument_name = input('Type in instrument name:')
    manufacturer_name = input("Type in instrument manufacturer:")
    year_built = int(input("Type in the year it was built:"))
    cost = int(input("Type in cost:"))
    string_instrument_name = input("Type in the name of the string instrument:")
    string_manufacturer = input("Type in string instrument manufacturer:")
    string_year_built = int(input("Type in the year it was built:"))
    string_cost = int(input("Type in cost:"))
    num_strings = int(input("Type in the number of strings it has:"))
    num_frets = int(input("Type in the number of frets it has:"))

    my_instrument = Instrument(instrument_name, manufacturer_name, year_built, cost)
    my_string_instrument = StringInstrument(string_instrument_name, string_manufacturer, string_year_built, string_cost,
                                            num_strings, num_frets)

    my_instrument.print_info()
    my_string_instrument.print_info()

    print('   Number of strings:', my_string_instrument.num_strings)
    print('   Number of frets:', my_string_instrument.num_frets)