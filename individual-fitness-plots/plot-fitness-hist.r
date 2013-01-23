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
pdf(file = output_path, width = 4, height = 3, useDingbats = F)
par(mar = c(3, 3, 0.5, 0.5), mgp = c(2, 0.75, 0))

hist(data$Fitness, xlab = 'Fitness', ylab = 'Frequency')

dev.off()
