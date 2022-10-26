class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        if(country not in ['Uganda', 'Albania']):
            raise ValueError('Invalid country: %s' % country)
        self._country = country

    def __str__(self):
        return f"name: {self.name} country: {self.country}"


def main():
    person = get_person()
    person.name = "Ken"
    print(person)


def get_person():
    name = input('Name')
    country = input('Country')

    return Person(name, country)


main()
