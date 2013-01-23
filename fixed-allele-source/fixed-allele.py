# Returns the allele if fixed, '0' otherwise

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


pos = int(sys.argv[1])
anc_path = sys.argv[2]

alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)]

anc_pop = [g.strip() for g in open(anc_path)]
pop = [g.strip() for g in sys.stdin]

# Get allele frequencies as a dictionary, e.g., {a: 0.8, b: 0.2}
anc_allele_freqs = calc_allele_freqs(anc_pop, pos)
pop_allele_freqs = calc_allele_freqs(pop, pos)

anc_fixed_allele = get_fixed_allele(anc_allele_freqs)
pop_fixed_allele = get_fixed_allele(pop_allele_freqs)

# Debug
#if anc_fixed_allele == '':
#  print >> sys.stderr, 'unfixed',
#else:
#  print >> sys.stderr, anc_fixed_allele, anc_allele_freqs[anc_fixed_allele],
#
#if pop_fixed_allele == '':
#  print >> sys.stderr, 'unfixed',
#else:
#  print >> sys.stderr, pop_fixed_allele, pop_allele_freqs[pop_fixed_allele],
#print >> sys.stderr, ''

# If allele is not fixed, print '0'
if pop_fixed_allele == '':
  print '0'

# If allele is fixed, but is the same as ancestral, print '0'
elif pop_fixed_allele == anc_fixed_allele:
  print '0'

# Otherwise, print allele
else:
  print pop_fixed_allele
