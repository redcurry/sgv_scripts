# Get command-line arguments, which must be specified after the '--args' flag
args = commandArgs(T)

if(length(args) < 1)
{
  print('Arguments: fitness_path')
  q()
}

fitness_path = args[1]

# Read data
data = read.table(fitness_path, header = F)

'Summary:'
summary(data)

'Length:'
size = length(data$V1)

means = replicate(10000, mean(sample(data$V1, replace = T)))
data_quantile = quantile(means, prob = c(0.025, 0.975))
data_mean = mean(data$V1)

'Mean:'
data_mean

'Quantile:'
data_quantile

'Lethal:'
length(data[data == 0.0])

'Strongly deleterious:'
length(data[data > 0.0 & data < 0.99])

'Mildly deleterious:'
length(data[data > 0.99 & data < 0.999])

'Nearly neutral:'
length(data[data > 0.999 & data < 1.001])

'Mildly beneficial:'
length(data[data > 1.001 & data < 1.01])

'Strongly Beneficial:'
length(data[data > 1.01])
