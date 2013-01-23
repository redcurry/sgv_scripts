import sys


def main():
  try:
    pos = int(sys.argv[1]) - 1
    allele = sys.argv[2]
  except IndexError:
    print 'Arguments: pos allele'
    exit(1)

  pop = get_pop_from_stream(sys.stdin)

  allele_freq = get_allele_freq(pos, allele, pop)
  print allele_freq


def get_pop_from_stream(stream):
  return [genotype.strip() for genotype in stream]


def get_allele_freq(pos, allele, pop):
  allele_count = get_allele_count(pos, allele, pop)
  return float(allele_count) / len(pop)


def get_allele_count(pos, allele, pop):
  return sum([1 for genotype in pop if genotype[pos] == allele])


main()
