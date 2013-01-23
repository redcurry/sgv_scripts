# Calculate the relative fitnesses of given numbers (as stdin)

import sys

for line in sys.stdin:
  line_parts = line.strip().split()
  x = float(line_parts[0])
  y = float(line_parts[1])
  if x > 0.0:
    print y / x
