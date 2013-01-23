import sys

try:
  beneficial_fitness = float(sys.argv[1])
except IndexError:
  print 'Arguments: beneficial_fitness'
  exit(1)

fits = [float(x) for x in sys.stdin]

# Rule:
# Both fitnesses must be greater than the required
#   for them to be considered good; if so, print out the max
# If there's only one fitness, then that's it
# If there no fitnesses, I don't know what happened,
#   but make it as if it didn't matter (neutral)

if len(fits) == 0:
  print 1.0
elif len(fits) == 1:
  print fits[0]
else:
  if fits[0] > beneficial_fitness and fits[1] > beneficial_fitness:
    print max(fits)
  else:
    print 1.0
