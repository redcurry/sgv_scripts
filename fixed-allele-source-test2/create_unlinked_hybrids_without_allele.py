# Given a population as stdin, and a position and instruction as arguments,
# creates random hybrids (such that the probability of each allele
# coming from one parent is 0.5), and prints those hybrids
# that do not have the specified allele


import sys
import random


N_HYBRIDS = 10000


def create_random_hybrid_from_pop(pop):
  parents = choose_parents(pop)
  hybrid = create_random_hybrid(parents)
  return hybrid


def choose_parents(pop):
  parent_1 = random.choice(pop)
  parent_2 = random.choice(pop)
  return [parent_1, parent_2]


def create_random_hybrid(parents):
  length = len(parents[0])
  hybrid_parts = [random.choice(parents)[i] for i in range(length)]
  hybrid = list_to_string(hybrid_parts)
  return hybrid


def list_to_string(alist):
  return ''.join(alist)


def has_allele(sequence, pos, inst):
  return sequence[pos] == inst


if len(sys.argv) < 2:
  print 'Arguments: pos inst'
  exit(1)

pos = int(sys.argv[1])
inst = sys.argv[2]

pop = [genotype.strip() for genotype in sys.stdin]

for i in range(N_HYBRIDS):
  hybrid = create_random_hybrid_from_pop(pop)
  while has_allele(hybrid, pos, inst):
    hybrid = create_random_hybrid_from_pop(pop)
  print hybrid
