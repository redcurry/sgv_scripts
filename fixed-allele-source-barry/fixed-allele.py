import sys


FIXED_MIN_FREQ = 0.95


def main():
  try:
    pos = int(sys.argv[1]) - 1
    anc_path = sys.argv[2]
  except IndexError:
    print 'Arguments: pos anc_path'
    exit(1)

  anc_pop = get_pop_from_stream(open(anc_path))
  pop = get_pop_from_stream(sys.stdin)

  derived_allele = get_derived_allele(pos, pop, anc_pop)
  print_derived_allele(derived_allele)


def get_pop_from_stream(stream):
  return [genotype.strip() for genotype in stream]


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


def get_allele_freq(pos, allele, pop):
  allele_count = get_allele_count(pos, allele, pop)
  return float(allele_count) / len(pop)


def get_allele_count(pos, allele, pop):
  return sum([1 for genotype in pop if genotype[pos] == allele])


def print_derived_allele(derived_allele):
  print derived_allele if derived_allele != '' else '0'


main()
