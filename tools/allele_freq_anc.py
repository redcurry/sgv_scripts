# Outputs the allele frequency in the ancestral population (given as a file)
# of each allele that is fixed in the current population (given as stdin)

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


# Returns the fixed allele at locus in allele_freqs
def get_fixed_allele(allele_freqs):

  max_freq = 0.0
  max_inst = ''
  for inst in alphabet:
    if allele_freqs[inst] > max_freq:
      max_freq = allele_freqs[inst]
      max_inst = inst

  if max_freq >= FIXED_FREQ:
    return max_inst
  else:
    return ''


if len(sys.argv) < 2:
  print 'Arguments: anc_pop_path'
  exit(1)

anc_pop_path = sys.argv[1]

alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)]

anc_pop = []
for genotype in open(anc_pop_path):
  anc_pop.append(genotype.strip())

pop = []
for genotype in sys.stdin:
  pop.append(genotype.strip())

genotype_length = len(pop[0])

for locus in range(genotype_length):

  # Get allele frequencies as a dictionary, e.g., {a: 0.8, b: 0.2}
  allele_freqs = calc_allele_freqs(pop, locus)

  # Get the ancestral allele frequencies
  anc_allele_freqs = calc_allele_freqs(anc_pop, locus)

  anc_fixed_allele = get_fixed_allele(anc_allele_freqs)
  fixed_allele = get_fixed_allele(allele_freqs)

  # Skip if current pop kept anc's fixed allele
  if fixed_allele == anc_fixed_allele:
    print locus, 'NA'
    continue

  if fixed_allele != '':
    # Print ancestral frequency
    print locus, anc_allele_freqs[fixed_allele]
  else:
    print locus, 'NA'
