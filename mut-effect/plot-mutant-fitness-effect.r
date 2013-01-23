# Get command-line arguments, which must be specified after the '--args' flag
args = commandArgs(T)

if(length(args) < 1)
{
  print('Arguments: sgv_fitness_path random_fitness_path output_path')
  q()
}

sgv_fitness_path = args[1]
random_fitness_path = args[2]
output_path = args[3]

# Read data
sgv_data = read.table(sgv_fitness_path, header = F)
random_data = read.table(random_fitness_path, header = F)
summary(sgv_data)
summary(random_data)

# Setup plot file
pdf(file = output_path, width = 5, height = 5, useDingbats = F)
par(mar = c(3.1, 3.1, 0.5, 0.5), mgp = c(2, 0.75, 0))

#xlabels = seq(0, 10000, 2500)
#axis(1, at = xlabels,
#  labels = prettyNum(xlabels, big.mark = ',', preserve.width = 'individual'))

#legend('bottomright',
#  legend = c('Normal SGV', 'No SGV'), lty = c('solid', 'dashed'), bty = 'n')

sgv_means = replicate(100, mean(sample(sgv_data$V1, replace = T)))
sgv_quantile = quantile(sgv_means, prob = c(0.025, 0.975))

sgv_lower_ci = sgv_quantile['2.5%']
sgv_upper_ci = sgv_quantile['97.5%']

sgv_mean = mean(sgv_data$V1)

sgv_mean
sgv_quantile

random_means = replicate(100, mean(sample(random_data$V1, replace = T)))
random_quantile = quantile(random_means, prob = c(0.025, 0.975))

random_lower_ci = random_quantile['2.5%']
random_upper_ci = random_quantile['97.5%']

random_mean = mean(random_data$V1)

random_mean
random_quantile

# Number of lethal
'Number of lethal'
length(sgv_data[sgv_data == 0.0])
length(random_data[random_data == 0.0])

# Number of beneficial
print('Number of beneficial')
length(sgv_data[sgv_data > 1.05])
length(random_data[random_data > 1.05])

s_values = c(1 - sgv_mean, 1 - random_mean)

plot(c(1, 2), s_values, xaxt = 'n', las = 1, pch = 16,
  xlim = c(0.5, 2.5), ylim = c(0, 0.08),
  xlab = 'Source of mutation', ylab = 'Mean fitness effect of mutation')

axis(1, at = c(1, 2), labels = c('SGV', 'Random'))

arrows(c(1, 2), c(1 - sgv_lower_ci, 1 - random_lower_ci),
  c(1, 2), c(1 - sgv_upper_ci, 1 - random_upper_ci),
  code = 3, angle = 90, length = 0.05)

dev.off()
