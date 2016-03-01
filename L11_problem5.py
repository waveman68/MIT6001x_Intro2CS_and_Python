# my solution

# class intSet(object):
#     """An intSet is a set of integers
#     The value is represented by a list of ints, self.vals.
#     Each int in the set occurs in self.vals exactly once."""
#
#     def __init__(self):
#         """Create an empty set of integers"""
#         self.vals = []
#
#     def insert(self, e):
#         """Assumes e is an integer and inserts e into self"""
#         if not e in self.vals:
#             self.vals.append(e)
#
#     def member(self, e):
#         """Assumes e is an integer
#            Returns True if e is in self, and False otherwise"""
#         return e in self.vals
#
#     def remove(self, e):
#         """Assumes e is an integer and removes e from self
#            Raises ValueError if e is not in self"""
#         try:
#             self.vals.remove(e)
#         except:
#             raise ValueError(str(e) + ' not found')
#
#     def __str__(self):
#         """Returns a string representation of self"""
#         self.vals.sort()
#         return '{' + ','.join([str(e) for e in self.vals]) + '}'
#
#     def intersect(self, other):
#         return_set = intSet()
#         my_set = eval(self.__str__())
#         for s in my_set:
#             if other.member(s):
#                 return_set.insert(s)
#         return return_set
#
#     def __len__(self):
#         l = 0
#         my_set = eval(self.__str__())
#         for s in my_set:
#             l += 1
#         return l
#
# setA = intSet()
# setB = intSet()
# for s in {-11,-10,-9,-5,3,11,12,15,16}:
#     setA.insert(s)
# for s in {-16,-6,-3,-1,0,1,5,7,9,15}:
#     setB.insert(s)
# setA.intersect(setB)


# more elegant, since I missed the access to the values w/ self.vals
class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        return_set = intSet()
        my_set = eval(self.__str__())
        for s in my_set:
            if other.member(s):
                return_set.insert(s)
        return return_set

    def __len__(self):
        l = 0
        my_set = eval(self.__str__())
        for s in my_set:
            l += 1
        return l

