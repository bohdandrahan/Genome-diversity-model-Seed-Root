class Species():
    '''Abstract class'''
    def get_genotype(self):
        return self.get_genotype

class Bacteria(Species):
    '''Concrete class'''
    def __init__(self, genotype):
        self.genotype = genotype




