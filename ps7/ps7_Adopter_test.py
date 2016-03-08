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


class Adopter:
    """
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """

    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species

    def get_name(self):
        return self.name

    def get_desired_species(self):
        return self.desired_species

    def get_score(self, adoption_center):
        adoption_center_species = adoption_center.get_species_count()
        num_desired = float(adoption_center_species[self.desired_species])
        return 1 * num_desired


class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        assert type(considered_species) == list
        assert len(considered_species) > 0
        self.considered_species = considered_species

    def get_score(self, adoption_center):
        adoption_center_species = adoption_center.get_species_count()
        adopter_score = 0
        try:
            adopter_score = float(adoption_center_species[self.desired_species])
        except KeyError:
            pass
        num_other = 0
        for species in self.considered_species:
            try:
                num_other += float(adoption_center_species[species])
            except KeyError:
                pass
        return adopter_score + 0.3 * num_other


class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        assert type(feared_species) == str
        self.feared_species = feared_species

    def get_score(self, adoption_center):
        adoption_center_species = adoption_center.get_species_count()
        adopter_score = 0
        try:
            adopter_score = float(adoption_center_species[self.desired_species])
        except KeyError:
            pass
        num_other = 0                   # Initialize for the KeyError case
        try:                            # Feared species is not necessarily there
            num_other = float(adoption_center_species[self.feared_species])
        except KeyError:
            pass
        return adopter_score - 0.3 * num_other


class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """

    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        assert type(allergic_species) == list
        self.allergic_species = allergic_species

    def get_score(self, adoption_center):
        adoption_center_species = adoption_center.get_species_count()
        adopter_score = 0
        allergic_species_present = False
        for species in self.allergic_species:
            try:
                if adoption_center_species[species] > 0:
                    allergic_species_present = True
            except KeyError:
                pass
        try:
            adopter_score = float(adoption_center_species[self.desired_species])
        except KeyError:
            pass
        if allergic_species_present:
            return 0
        else:
            return adopter_score


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter.
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary.
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        assert type(medicine_effectiveness) == dict
        self.medicine_effectiveness = medicine_effectiveness

    def get_score(self, adoption_center):
        adoption_center_species = adoption_center.get_species_count()
        adopter_score = 0.0
        problem_species = []

        for species in self.allergic_species:
            try:
                if adoption_center_species[species] > 0:
                    problem_species.append(self.medicine_effectiveness[species])
            except KeyError:
                pass
        try:
            adopter_score = float(adoption_center_species[self.desired_species])
        except KeyError:
            pass
        if len(problem_species) > 0:
            return adopter_score * min(problem_species)
        else:
            return adopter_score


my_adoption_center = AdoptionCenter('Sam\'s Homeless Pets', {'Dog': 3, 'Cat': 2, 'Elephant': 10, 'Horse': 2}, (1, 1))
print(my_adoption_center.get_number_of_species('Dog'))
print(my_adoption_center.get_number_of_species('Cat'))
print(my_adoption_center.get_number_of_species('Elephant'))
print(my_adoption_center.adopt_pet('Cat'))


my_adopter = Adopter('Lily', 'Dog')
print(my_adopter.get_desired_species())
print(my_adopter.get_score(my_adoption_center))

my_flexible_adopter = FlexibleAdopter('Dylan', 'Dog', ['Cat', 'Elephant'])
print(my_flexible_adopter.get_desired_species())
print(my_flexible_adopter.get_score(my_adoption_center))

my_fearful_adopter = FearfulAdopter('Dylan2', 'Cat', 'Dog')
print(my_fearful_adopter.get_desired_species())
print(my_fearful_adopter.get_score(my_adoption_center))

my_allergic_adopter = AllergicAdopter('Susanne', 'Dog', ['Cat'])
print('===== Allergic =====')
print(my_allergic_adopter.get_desired_species())
print(my_allergic_adopter.get_score(my_adoption_center))

my_medicated_adopter = MedicatedAllergicAdopter('Susanne', 'Dog', ['Cat', 'Horse'], {'Cat': 0.25, 'Horse': 0.5})
print('===== Medicated =====')
print(my_medicated_adopter.get_desired_species())
print(my_medicated_adopter.get_score(my_adoption_center))
