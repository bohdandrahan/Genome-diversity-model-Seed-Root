class Genotype():
    def create_initial_genotype(self, dna_name):
        dna_part = 1
        self.genotype = [(dna_name, dna_part)]

    def get_genotype(self):
        return self.genotype

    def mix_parents_dna(self, couple):
        mother_genotype = couple[0].get_genotype()
        father_genotype = couple[1].get_genotype()

        mix_genotype = list()
        not_original_dna_names = list()
        for dna_mother in mother_genotype.get_genotype():
            for dna_father in father_genotype.get_genotype():
                if dna_mother[0] == dna_father[0]:
                    new_dna_part = (dna_mother[1] + dna_father[1])/float(2)
                    mix_genotype.append((dna_mother[0], new_dna_part))
                    not_original_dna_names.append(dna_mother[0])
            if dna_mother[0] not in not_original_dna_names:
                new_dna_part = dna_mother[1]/float(2)
                mix_genotype.append((dna_mother[0], new_dna_part))
        for dna_father in father_genotype.get_genotype():
            if dna_father[0] not in not_original_dna_names:
                new_dna_part = dna_father[1]/float(2)
                mix_genotype.append((dna_father[0], new_dna_part))

        self.genotype = mix_genotype


