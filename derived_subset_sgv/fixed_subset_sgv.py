import sys


FIXED_MIN_FREQ = 0.95
SGV_MIN_FREQ = 0.05


def get_derived_allele(pos, pop, anc_pop):
  for allele in get_alleles(pos, pop):
    if allele_is_derived(allele, pos, pop, anc_pop):
      return allele
  return ''


def get_alleles(pos, pop):
  return set([genotype[pos] for genotype in pop])


def allele_is_derived(allele, pos, pop, anc_pop):
  return allele_is_fixed(pos, allele, pop) and \
    not allele_is_fixed(pos, allele, anc_pop)


def allele_is_fixed(pos, allele, pop):
  allele_freq = get_allele_freq(pos, allele, pop)
  return allele_freq > FIXED_MIN_FREQ


def allele_is_sgv(pos, allele, pop):
  allele_freq = get_allele_freq(pos, allele, pop)
  return allele_freq > SGV_MIN_FREQ


def get_allele_freq(pos, allele, pop):
  allele_count = get_allele_count(pos, allele, pop)
  return float(allele_count) / len(pop)


def get_allele_count(pos, allele, pop):
  return sum([1 for genotype in pop if genotype[pos] == allele])


anc_path = sys.argv[1]

anc_pop = [genotype.strip() for genotype in open(anc_path)]
pop = [genotype.strip() for genotype in sys.stdin]

genome_length = len(pop[0])

for pos in range(genome_length):
  derived_allele = get_derived_allele(pos, pop, anc_pop)

  if derived_allele == '':
    continue

  if allele_is_sgv(pos, derived_allele, anc_pop):
    print pos + 1, 1
  else:
    print pos + 1, 0
