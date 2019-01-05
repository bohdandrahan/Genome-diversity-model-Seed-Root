import random
import numpy as np


from species import Bacteria

class Population():
    '''Abstract class'''

    def get_pop(self):
        return self.pop

    def get_initial_pop_size(self):
        return self.initial_pop_size

    def get_birth_prob(self):
        return self.birth_prob

    def get_death_prob(self):
        return self.death_prob

    def update_death_prob(self):
        self.death_prob = 1 - (self.world.abs_max - len(self.pop))/float(self.world.abs_max)

    def creat_first_gen(self):
        pop = list()
        for each in range(self.get_initial_pop_size()):
            pop.append(self.species(each))
        return pop

    def kill_wave(self):
        new_pop = list(self.pop)
        for individual in self.pop:
            if random.random() < self.get_death_prob():
                new_pop.remove(individual)

        self.pop = new_pop
        self.update_death_prob()

class AsexualPopulation(Population):
    '''Concrete Class'''
    def __init__ (self, world, species = Bacteria, initial_pop_size = 100, birth_prob = 0.05):
        self.world = world
        self.species = species
        self.initial_pop_size = initial_pop_size
        self.pop = self.creat_first_gen()
        self.birth_prob = birth_prob
        self.update_death_prob()

        self.update_genes_matrix()

    def update_genes_matrix(self):
        genes = list()
        for i in range(self.get_initial_pop_size()):
            qty = 0
            for individual in self.get_pop():
                if i == individual.get_genotype():
                    qty += 1
            genes.append(qty)
        self.genes_matrix = genes

    def get_genes_matrix(self):
        return self.genes_matrix

    def get_original_genes(self):
        original_genes = list()
        for individual in self.get_pop():
            original_genes.append(individual.get_genotype())
        return list(set(original_genes))

    def birth_wave(self):
        new_pop = list(self.get_pop())
        for individual in self.get_pop():
            if random.random() < self.get_birth_prob():
                new_born = self.species(individual.get_genotype())
                new_pop.append(new_born)

        self.pop = new_pop
        self.update_death_prob()

