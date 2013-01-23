# Prints the sequences (from stdin) that have the specified allele

import sys

if len(sys.argv) < 2:
  print 'Arguments: pos inst [has_allele]'
  exit(1)

pos = int(sys.argv[1]) - 1
inst = sys.argv[2]

if len(sys.argv) > 3:
  has_allele = sys.argv[3]
else:
  has_allele = '1'

pop = [g.strip() for g in sys.stdin]

for genotype in pop:
  if genotype[pos] == inst:
    if has_allele != '0':
      print genotype
  else:
    if has_allele == '0':
      print genotype
