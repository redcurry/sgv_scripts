import sys
import random


GENOME_LENGTH = 200
REPLICATES = 1200  # extra in cose no sgv is found or genotype is inviable
FIXED_FREQ = 0.95
SGV_FREQ = 1.0 - FIXED_FREQ


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
      allele_freqs[inst] /= float(len(pop))

  return allele_freqs


def insts(pop, pos):
  return [genotype[pos] for genotype in pop]


def most_frequent(alist):
  salist = sorted(alist)
  best_count = 0
  best_item = salist[0]
  prev_item = best_item
  count = 0
  for item in salist:
    if item != prev_item:
      if count > best_count:
        best_count = count
        best_item = prev_item
      count = 0
    else:
      count += 1
    prev_item = item
  if count > best_count:
    best_count = count
    best_item = prev_item
  return best_item


def get_consensus(pop):
  return ''.join([most_frequent(insts(pop, pos)) \
    for pos in range(GENOME_LENGTH)])


def mutate(genotype, pos, inst):
  return genotype[:pos] + inst + genotype[pos + 1:]


if len(sys.argv) < 2:
  print 'Arguments: type (random or sgv)'
  exit()

type = sys.argv[1]


alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)]

pop = [genotype.strip() for genotype in sys.stdin]

#if type == 'random':
# for rep in range(REPLICATES):
#   pos = random.randint(0, GENOME_LENGTH - 1)
#   inst = random.choice(alphabet)
#   mutant = mutate(consensus, pos, inst)
#   print mutant
#elif type == 'sgv':
# Get all allele frequencies as a list of dictionaries for each locus

allele_freqs = [calc_allele_freqs(pop, pos) for pos in range(GENOME_LENGTH)]

for rep in range(REPLICATES):
  # Pick a random genotype
  genotype = random.choice(pop)

  # Pick a random position that is not fixed
  pos = random.randint(0, GENOME_LENGTH - 1)
  while max(allele_freqs[pos].values()) > FIXED_FREQ:
    pos = random.randint(0, GENOME_LENGTH - 1)

  # Pick an allele from the possible sgv choices at that locus,
  # such that it's frequency is > SGV_FREQ (random mutation) and
  # such that it's different from the genotype's current allele
  inst_set = [allele for allele in set(allele_freqs[pos].keys()) \
    if allele_freqs[pos][allele] > SGV_FREQ and allele != genotype[pos]]
  if len(inst_set) > 0:
    if type == 'sgv':
      inst = random.choice(inst_set)
    else:
      inst = random.choice(list(set(alphabet) - set(genotype[pos])))
  else:
    continue

  mutant = mutate(genotype, pos, inst)

  # Print sequence before and after
  print genotype, mutant
