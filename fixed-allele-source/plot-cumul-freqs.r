bootstrap_ci = function(x, n = 10000, lower = 0.025, upper = 0.975)
{
  means = replicate(n, mean(sample(x, replace = T)))
  quantile(means, probs = c(lower, upper), na.rm = T)
}

get_box = function(x)
{
  ci = bootstrap_ci(x)
  c(ci[1], mean(x), ci[2])
}

get_freq_box = function(break_step, data)
{
  get_box(data[data$BreakStep == break_step,]$Frequency)
}

cumul = function(data, breaks)
{
  data.cut = cut(data, breaks, right = F)
  data.freq = table(data.cut)
  return(cumsum(data.freq) / length(data))
}

# Get command-line arguments, which must be specified after the '--args' flag
args = commandArgs(T)

if(length(args) < 1)
{
  print('Arguments: normal_sgv_path no_sgv_path output_path')
  q()
}

normal_sgv_path = args[1]
no_sgv_path = args[2]
output_path = args[3]

# Read data (contains column headers)
normal_sgv_data = read.table(normal_sgv_path, header = T)
no_sgv_data = read.table(no_sgv_path, header = T)

# Setup plot file and basic plot
pdf(file = output_path, width = 5, height = 5, useDingbats = F)
par(mar = c(3.1, 3.1, 0.5, 0.5), mgp = c(2, 0.75, 0))

# Basic plot
plot(0, 0, type = 'n', las = 1,
  xlim = c(0, 1),
  ylim = c(0, 1),
  xlab = 'Allele frequency when first beneficial',
  ylab = 'Cummulative frequency')

#xlabels = seq(0, 10000, 2500)
#axis(1, at = xlabels,
#  labels = prettyNum(xlabels, big.mark = ',', preserve.width = 'individual'))

legend('bottomright',
  legend = c('Normal SGV', 'No SGV'), lty = c('solid', 'dashed'), bty = 'n')

step_size = 0.025
breaks = seq(0, 0.95, by = step_size)

# DON'T ASSUME DATA HAS ALL REPLICATES
# Create Replicate column for cumul data frame
replicates = c()
for(rep in seq(20))
  replicates = c(replicates, rep.int(rep, length(breaks) - 1))

# Create BreakStep column for cumul data frame
break_steps = breaks[1:length(breaks) - 1]
break_steps_col = rep.int(break_steps, 20)

# Get cumulative distribution for each replicate
# and make them into the Frequency column
normal_sgv_freqs = c()
for(rep in seq(20))
{
  subdata = normal_sgv_data[normal_sgv_data$Replicate == rep,]
  normal_sgv_freqs = c(normal_sgv_freqs, cumul(subdata$Frequency, breaks))
}

normal_sgv_cumul = data.frame(cbind(replicates, break_steps_col,
  normal_sgv_freqs))
names(normal_sgv_cumul) = c('Replicate', 'BreakStep', 'Frequency')

# Get cumulative distribution for each replicate
# and make them into the Frequency column
no_sgv_freqs = c()
for(rep in seq(20))
{
  subdata = no_sgv_data[no_sgv_data$Replicate == rep,]
  no_sgv_freqs = c(no_sgv_freqs, cumul(subdata$Frequency, breaks))
}

no_sgv_cumul = data.frame(cbind(replicates, break_steps_col, no_sgv_freqs))
names(no_sgv_cumul) = c('Replicate', 'BreakStep', 'Frequency')

print(length(replicates))
print(length(break_steps_col))
print(length(no_sgv_freqs))

# Calculate CIs
normal_sgv_box = sapply(break_steps, get_freq_box, normal_sgv_cumul)
no_sgv_box = sapply(break_steps, get_freq_box, no_sgv_cumul)

# Lower CI
lines(break_steps + step_size, normal_sgv_box[1,], lty = 'solid', col = 'gray')
lines(break_steps + step_size, no_sgv_box[1,], lty = 'dashed', col = 'gray')

# Upper CI
lines(break_steps + step_size, normal_sgv_box[3,], lty = 'solid', col = 'gray')
lines(break_steps + step_size, no_sgv_box[3,], lty = 'dashed', col = 'gray')

# Calculate means
normal_sgv_mean = aggregate(normal_sgv_cumul$Frequency,
  by = list(normal_sgv_cumul$BreakStep), mean)
names(normal_sgv_mean) = c('BreakStep', 'Frequency')
no_sgv_mean = aggregate(no_sgv_cumul$Frequency,
  by = list(no_sgv_cumul$BreakStep), mean)
names(no_sgv_mean) = c('BreakStep', 'Frequency')

print('Normal SGV:')
normal_sgv_mean

print('No SGV:')
no_sgv_mean

# Mean (plot after CI so that the mean lines are on top of CI lines)
lines(break_steps + step_size, normal_sgv_mean$Frequency, lty = 'solid')
lines(break_steps + step_size, no_sgv_mean$Frequency, lty = 'dashed')

dev.off()
