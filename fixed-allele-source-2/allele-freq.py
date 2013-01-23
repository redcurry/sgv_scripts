# Returns the allele frequency at the specified position

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


pos = int(sys.argv[1])
inst = sys.argv[2]

alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)]

pop = [g.strip() for g in sys.stdin]

# Get allele frequencies as a dictionary, e.g., {a: 0.8, b: 0.2}
pop_allele_freqs = calc_allele_freqs(pop, pos)

print pop_allele_freqs[inst]
