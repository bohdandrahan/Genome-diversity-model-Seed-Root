import random

class Species():
    '''Abstract class'''
    def get_genotype(self):
        return self.genotype

class Bacteria(Species):
    '''Concrete class'''
    def __init__(self, genotype):
        self.genotype = genotype

class Giraffe(Species):
    def __init__(self, genotype):
        self.genotype = genotype
        self.male = bool(random.getrandbits(1)) 

    def is_male(self):
        return self.male
