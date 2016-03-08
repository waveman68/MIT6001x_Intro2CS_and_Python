__author__ = 'Sam Broderick'
"""
Designed to test my AdoptionCenter class for ps7 from MIT 6.00.1x
"""

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """

    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        self.location = ( float(location[0]), float(location[1]) )

    def get_number_of_species(self, animal):
        try:
            return self.species_types[animal]
        except KeyError:
            return 0

    def get_location(self):
        return self.location

    def get_species_count(self):
        return self.species_types.copy()

    def get_name(self):
        return self.name

    def adopt_pet(self, species):
        try:
            if self.species_types[species] > 0:
                self.species_types[species] -= 1
            if self.species_types[species] == 0:
                self.species_types.pop(species)
        except KeyError:
            pass

my_adoption_center = AdoptionCenter('Sam\'s Homeless Pets', {'Dog': 3, 'Cat': 1}, (1, 1))
my_adoption_center.get_number_of_species('Dog')
my_adoption_center.get_number_of_species('Cat')
my_adoption_center.get_number_of_species('Elephant')
my_adoption_center.adopt_pet('Cat')
