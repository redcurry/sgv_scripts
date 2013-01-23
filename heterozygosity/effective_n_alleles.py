# Outputs the effective number of allele at every locus of the given population

from __future__ import division

import sys


def calc_allele_freqs(pop, locus):

  allele_freqs = {}
  for inst in alphabet:
    allele_freqs[inst] = 0

  for genotype in pop:

    inst = genotype[locus]
    allele_freqs[inst] += 1

  # Calculate frequencies from counts
  for inst in allele_freqs:
    if allele_freqs[inst] > 0:
      allele_freqs[inst] /= len(pop)

  return allele_freqs



def calc_effective_n_alleles(allele_freqs):

  # Calculate the sum of squares of allele frequencies
  ss = sum([allele_freqs[inst] * allele_freqs[inst] for inst in alphabet])

  return 1 / ss


alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)]

pop = []
for genotype in sys.stdin:
  pop.append(genotype.strip())

genotype_length = len(pop[0])

for locus in range(genotype_length):

  # Get allele frequencies as a dictionary, e.g., {a: 0.8, b: 0.2}
  allele_freqs = calc_allele_freqs(pop, locus)

  effective_n_alleles = calc_effective_n_alleles(allele_freqs)

  print locus, effective_n_alleles
