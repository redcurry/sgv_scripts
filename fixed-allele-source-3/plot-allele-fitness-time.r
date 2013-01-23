# Get command-line arguments, which must be specified after the '--args' flag
args = commandArgs(T)

if(length(args) < 1)
{
  print('Arguments: allele_fitness_time_path output_path')
  q()
}

allele_fitness_time_path = args[1]
output_path = args[2]

# Read data (contains column headers)
allele_fitness_time = read.table(allele_fitness_time_path, header = T)

# Setup plot file
pdf(file = output_path, width = 10, height = 1.5, useDingbats = F)
par(mar = c(3, 3, 0.5, 0.5), mgp = c(2, 0.75, 0))

plot(allele_fitness_time$Update, allele_fitness_time$Fitness - 1,
  type = 'l', xaxt = 'n', yaxt = 'n', las = 1,
  xlim = c(0, 10000), ylim = c(0, 0.5),
  xlab = 'Time (updates)', ylab = 'Fitness effect (s)')

xlabels = seq(0, 10000, 2500)
axis(1, at = xlabels,
  labels = prettyNum(xlabels, big.mark = ',', preserve.width = 'individual'))

axis(2, at = c(0, 0.25, 0.5), las = 1)

dev.off()
