# Given a population as stdin, and a position and instruction as arguments,
# creates random hybrids (the Avida way), and prints those hybrids
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
  chunk = get_random_chunk(length)
  return create_hybrid(parents, chunk)


def get_random_chunk(length):
  start_pos = random.randint(0, length - 1)
  size = random.randint(1, length - 1)
  return get_chunk(start_pos, size, length)


def get_chunk(start_pos, size, length):
  chunk_pos = range(start_pos, start_pos + size)
  return [wrapped_pos(pos, length) for pos in chunk_pos]


def wrapped_pos(pos, length):
  return pos % length


def create_hybrid(parents, chunk):
  length = len(parents[0])
  hybrid_parts = [choose_parent_inst(parents, chunk, i) for i in range(length)]
  return list_to_string(hybrid_parts)


def choose_parent_inst(parents, chunk, pos):
  return parents[1][pos] if pos in chunk else parents[0][pos]


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
