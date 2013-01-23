# Replaces the given allele in the population (from stdin)
# with another allele gotten from the existing variation at that locus

import sys
import random

def main():
  try:
    pos = int(sys.argv[1]) - 1
    allele = sys.argv[2]
  except IndexError:
    print 'Arguments: pos allele'
    exit(1)

  pop = [genotype.strip() for genotype in sys.stdin]

  for genotype in pop:
    if has_allele(genotype, pos, allele):
      print replace_allele_with_sgv(genotype, pos, allele, pop)
    else:
      print genotype


def has_allele(genotype, pos, allele):
  return genotype[pos] == allele


def replace_allele_with_sgv(genotype, pos, allele, pop):
  sgv_allele = get_sgv_allele_except(pos, pop, genotype[pos])
  return replace_allele(genotype, pos, sgv_allele)


def get_sgv_allele_except(pos, pop, except_allele):
  random_genotype = random.choice(pop)
  while has_allele(random_genotype, pos, except_allele):
    random_genotype = random.choice(pop)
  return random_genotype[pos]


def replace_allele(genotype, pos, allele):
  return genotype[:pos] + allele + genotype[pos + 1:]


main()
