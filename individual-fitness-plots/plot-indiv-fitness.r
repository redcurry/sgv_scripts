# Get command-line arguments, which must be specified after the '--args' flag
args = commandArgs(T)

if(length(args) < 1)
{
  print('Arguments: input_path output_path')
  q()
}

input_path = args[1]
output_path = args[2]

# Read data (contains column headers)
data = read.table(input_path, header = T)

# Standardize fitness
data$Fitness = data$Fitness / mean(data$Fitness)

# Setup plot file
pdf(file = output_path, width = 10, height = 1.5, useDingbats = F)
par(mar = c(3, 3, 0.5, 0.5), mgp = c(2, 0.75, 0))

plot(data$Fitness, type='l',
  xaxt = 'n', yaxt = 'n', las = 1,
  xlim = c(20, 980), ylim = c(0, 2),
  xlab = 'Individual', ylab = 'Fitness')

axis(1, at = c(1, seq(100, 1000, 100)))
axis(2, at = c(0, 1, 2), las = 1)

dev.off()
