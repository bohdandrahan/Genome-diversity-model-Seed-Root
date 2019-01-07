import random
import numpy as np
from genotype import Genotype

class Population():
    '''Abstract class'''
    def __init__ (self, world, species, initial_pop_size, birth_prob):
        self.world = world
        self.species = species
        self.initial_pop_size = initial_pop_size
        self.pop = self.create_first_gen()
        self.birth_prob = birth_prob
        self.update_death_prob()
        self.update_genes()

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

    def create_first_gen(self):
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
    def update_genes(self):
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

class SexualPopulation(Population):
    def __init__ (self, world, species, initial_pop_size, birth_prob, long_term = True, monogamy = True):
        self.world = world
        self.species = species
        self.initial_pop_size = initial_pop_size
        self.pop = self.create_first_gen()
        self.birth_prob = birth_prob
        self.long_term = long_term
        self.monogamy = monogamy

        self.update_death_prob()
        self.update_genes()

        self.couples = list()
        self.update_couples()

    def create_first_gen(self):
        pop = list()
        for each in range(self.get_initial_pop_size()):
            genotype = Genotype()
            genotype.create_initial_genotype(each)
            pop.append(self.species(genotype))
        return pop

    def update_genes(self):
        pass #TODO

    def update_couples(self):
        if self.long_term:
            self.update_long_term_couples()
        else: self.update_short_term_couples()

    def update_couples(self):
        if self.long_term:
            self.remove_widows()
            open_to_mating = self.get_open_to_mating()
        else:
            open_to_mating = self.get_pop()
            self.couples = list()

        self.couples += self.find_new_couples(open_to_mating)

    def get_open_to_mating(self):
        open_to_mating = list(self.get_pop)
        for couple in self.get_couples():
            for partner in couple:
                open_to_mating.remove(partner)
        return open_to_mating

    def find_new_couples(self, open_to_mating):
        new_couples = list()
        singe_males = get_males(open_to_mating)
        for female in get_females(open_to_mating):
            male = random.choise(singe_males)
            couples.append((female, male))
            if self.monogamy:
                singe_males.remove(male)
        return new_couples

    def remove_widows(self):
        updated_couples = self.get_couples()
        for couple in self.get_couples():
            for partner in couple:
                if partner not in self.get_pop():
                    updated_couples.remove(couple)
        self.couples = updated_couples

    def birth_wave(self):
        new_pop = list(self.get_pop())
        for couple in self.get_couples():
            if random.random() < self.get_birth_prob():
                new_bort = self.give_birth(couple)
                new_pop.append(new_born)
        self.pop = new_pop
        self.update_death_prob()

    def give_birth(couple):
        new_born_genotype = Genotype()
        new_born_genotype.mix_parents_dna(couple)
        new_born = self.species(new_born_genotype)

    def get_males(self, pop):
        males = list()
        for individual in pop():
            if individual.is_male():
                males.append(individual)
        return males

    def get_females(self, pop):
        females = list(set(pop) - set(self.get_males(pop)))

    def get_couples(self):
        return self.couples
