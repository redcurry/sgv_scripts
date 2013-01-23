# Get command-line arguments, which must be specified after the '--args' flag
args = commandArgs(T)

if(length(args) < 1)
{
  print('Arguments: effective_n_alleles_path output_path')
  q()
}

effective_n_alleles_path = args[1]
output_path = args[2]

# Read data (contains column headers)
effective_n_alleles_data = read.table(effective_n_alleles_path, header = T)

# Calculate heterozygosity
homozygosity = 1.0 - 1.0 / effective_n_alleles_data$n

# Setup plot file
pdf(file = output_path, width = 10, height = 1.5, useDingbats = F)
par(mar = c(3, 3, 0.5, 0.5), mgp = c(2, 0.75, 0))

barplot(homozygosity, space = 0, col = 'black',
#  names.arg = seq(1,200), axis.lty = 1,
  xaxt = 'n', yaxt = 'n', las = 1,
  xlim = c(1, 200), ylim = c(0, 1),
  xlab = 'Locus', ylab = 'Heterozygosity')

#axis(1, at = c(1, seq(25, 200, 25)))
axis(1, at = c(1, seq(10, 200, 10)))
axis(2, at = c(0, 0.5, 1), las = 1)

dev.off()
