# Outputs the frequency of every allele at every locus of the given population

from __future__ import division

import sys


FIXED_FREQ = 0.95


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



alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)]

pop = []
for genotype in sys.stdin:
  pop.append(genotype.strip())

genotype_length = len(pop[0])

for locus in range(genotype_length):

  # Get allele frequencies as a dictionary, e.g., {a: 0.8, b: 0.2}
  allele_freqs = calc_allele_freqs(pop, locus)

  max_freq = 0.0
  max_inst = ''
  for inst in alphabet:
    if allele_freqs[inst] > max_freq:
      max_freq = allele_freqs[inst]
      max_inst = inst

  if max_freq >= FIXED_FREQ:
    sys.stdout.write(max_inst)
  else:
    sys.stdout.write('-')

print
