import math
import random

__author__ = 'Sam Broderick'

"""
Designed to test get_ordered_adoption_center_list and
get_adopters_for_advertisement functions for ps7 from MIT 6.00.1x
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
        self.location = (float(location[0]), float(location[1]))

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
        try:
            num_desired = float(adoption_center_species[self.desired_species])
        except KeyError:
            num_desired = 0
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
        num_other = 0  # Initialize for the KeyError case
        try:  # Feared species is not necessarily there
            num_other = float(adoption_center_species[self.feared_species])
        except KeyError:
            pass
        score = adopter_score - 0.3 * num_other
        if score < 0:
            score = 0.0
        return score


class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """

    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species

    def get_score(self, adoption_center):
        adoption_center_species = adoption_center.get_species_count()
        adopter_score = 0.0
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
            return 0.0
        else:
            return adopter_score


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be
    given in a dictionary
    To calculate the score for a specific adoption center, we want to find
    what is the most allergy-inducing species that the adoption center has
    for the particular MedicatedAllergicAdopter.
    To do this, first examine what species the AdoptionCenter has that the
    MedicatedAllergicAdopter is allergic to, then compare them to the
    medicine_effectiveness dictionary.
    Take the lowest medicine_effectiveness found for these species, and
    multiply that value by the Adopter's calculate score method.
    """

    def __init__(self, name, desired_species, allergic_species,
                 medicine_effectiveness):
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
                    problem_species.append(self.
                                           medicine_effectiveness[species])
            except KeyError:
                pass
        try:
            adopter_score = float(adoption_center_species[self.
                                  desired_species])
        except KeyError:
            pass
        if len(problem_species) > 0:
            return adopter_score * min(problem_species)
        else:
            return adopter_score


class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """

    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        assert type(location) == tuple
        self.location = location

    def get_linear_distance(self, to_location):
        delta_x_sq = (to_location[0] - self.location[0]) ** 2  # square of the x dist.
        delta_y_sq = (to_location[1] - self.location[1]) ** 2  # square of the y dist.
        return math.sqrt(delta_x_sq + delta_y_sq)

    def get_score(self, adoption_center):
        adoption_center_species = adoption_center.get_species_count()
        adoption_center_distance = self.get_linear_distance(adoption_center.get_location())
        try:
            num_desired = float(adoption_center_species[self.desired_species])
        except KeyError:
            num_desired = 0.0
        if adoption_center_distance < 1:
            return 1 * num_desired
        elif 1 <= adoption_center_distance < 3:
            return random.uniform(0.7, 0.9) * num_desired
        elif 3 <= adoption_center_distance < 5:
            return random.uniform(0.5, 0.7) * num_desired
        elif adoption_center_distance >= 5:
            return random.uniform(0.1, 0.5) * num_desired


def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the
    scores for each AdoptionCenter to the Adopter will be ordered from
    highest score to lowest score.
    :param adopter: looking to adopt a pet
    :param list_of_adoption_centers: list of centers with pets to adopt
    """
    local_copy = list_of_adoption_centers[:]  # copy to prevent changing original
    local_copy.sort(key=lambda x: (-adopter.get_score(x), x.get_name()))

    # returns just the sorted list of names without scores
    return local_copy


def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from
    list_of_adopters (in numerical order of score)
    :param adoption_center: adoption center placing an ad
    :param list_of_adopters: list of potential pet adopters
    :param n: maximum number of ads
    """

    local_copy = list_of_adopters[:]  # copy to prevent changing original
    local_copy.sort(key=lambda x: (-x.get_score(adoption_center), x.get_name()))

    if len(list_of_adopters) > n:
        return local_copy[:n]
    else:
        return local_copy


adopter = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'],
                                   {"Dog": .5, "Horse": 0.2})
adopter2 = Adopter("Two", "Cat")
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter4 = FearfulAdopter("Four", "Cat", "Dog")
adopter5 = SluggishAdopter("Five", "Cat", (1, 2))
adopter6 = AllergicAdopter("Six", "Cat", "Dog")

ac = AdoptionCenter("Place1", {"Mouse": 12, "Dog": 2}, (1, 1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3, 5))
ac3 = AdoptionCenter("Place3", {"Horse": 25, "Dog": 9}, (-2, 10))

adopters = [adopter, adopter2, adopter3, adopter4, adopter5, adopter6]

# how to test get_adopters_for_advertisement
test1 = get_adopters_for_advertisement(ac, [adopter, adopter2, adopter3,
                                            adopter4, adopter5, adopter6], 10)
# you can print the name and score of each item in the list returned
print('======= Test 1 =======')
for a in test1:
    print(a.get_name())
print('=======')

for a in adopters:
    print('Adopter {0}:  score: {1}'.format(a.get_name, a.get_score(ac)))

print('======= Test 2 =======')
test2 = get_adopters_for_advertisement(ac2, [adopter, adopter2, adopter3,
                                             adopter4, adopter5, adopter6], 10)
for a in test2:
    print(a.get_name())
print('=======')

for a in adopters:
    print('Adopter {0}:  score: {1}'.format(a.name, a.get_score(ac2)))

print('======= Test 3 =======')
test2 = get_adopters_for_advertisement(ac3, [adopter, adopter2, adopter3,
                                             adopter4, adopter5, adopter6], 10)
for a in test2:
    print(a.get_name())
print('=======')

for a in adopters:
    print('Adopter {0}:  score: {1}'.format(a.name, a.get_score(ac3)))

print
adopter4 = FearfulAdopter("Four", "Cat", "Dog")
adopter5 = SluggishAdopter("Five", "Cat", (1, 2))
adopter6 = AllergicAdopter("Six", "Lizard", "Cat")

ac = AdoptionCenter("Place1", {"Cat": 12, "Dog": 2}, (1, 1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3, 5))
ac3 = AdoptionCenter("Place3", {"Cat": 40, "Dog": 4}, (-2, 10))
ac4 = AdoptionCenter("Place4", {"Cat": 33, "Horse": 5}, (-3, 0))
ac5 = AdoptionCenter("Place5", {"Cat": 45, "Lizard": 2}, (8, -2))
ac6 = AdoptionCenter("Place6", {"Cat": 23, "Dog": 7, "Horse": 5}, (-10, 10))

# how to test get_ordered_adoption_center_list
test_acs = list()
test_acs.append(get_ordered_adoption_center_list(adopter4, [ac, ac2, ac3, ac4, ac5, ac6]))
test_acs.append(get_ordered_adoption_center_list(adopter5, [ac, ac2, ac3, ac4, ac5, ac6]))
test_acs.append(get_ordered_adoption_center_list(adopter6, [ac, ac2, ac3, ac4, ac5, ac6]))
# you can print the name and score of each item in the list returned
print('======= Test get_ordered_adoption_center_list =======')
print

for a in test_acs:
    print('=======')
    for c in a:
        print(c.get_name())

print('=======')
for c in test_acs[1]:
    print('{0}:  distance: {1}  normal: {2}  score: {3}'.
          format(c.get_name(), adopter5.get_linear_distance(c.get_location()),
                 c.get_number_of_species(adopter5.desired_species),
                 adopter5.get_score(c)))
