# Plot the frequency of those allele identified by my analysis
# (found_allele_path could be fixed-allele-source-test/results/normal-sgv)

# Get command-line arguments, which must be specified after the '--args' flag
args = commandArgs(T)

if(length(args) < 1)
{
  print('Arguments: input_path found_allele_path output_path')
  q()
}

input_path = args[1]
found_allele_path = args[2]
output_path = args[3]

data = read.table(input_path, header = T, stringsAsFactors = F)
found_allele_data = read.table(found_allele_path, header = T, stringsAsFactors = F)

# Focus on just one replicate
found_allele_data = found_allele_data[found_allele_data$Replicate == 1,]

pdf(file = output_path, width = 10, height = 1.5, useDingbats = F)
par(mar = c(3, 3, 0.5, 0.5), mgp = c(2, 0.75, 0))

# Set up plot
plot(0, 0, type = 'n',
  xlim = c(0, 10000),
  ylim = c(0, 1))

#colors = rainbow(length(found_allele_data$Locus))
colors = rainbow(100)
col_i = 1

for(locus in unique(found_allele_data$Locus))
{
  allele = found_allele_data[found_allele_data$Locus == locus, 'Instruction']
  update = found_allele_data[found_allele_data$Locus == locus, 'Update']
  locusData = data[data$Locus == (locus - 1),]

  color = sample(colors, 1)
  lines(locusData$Update, locusData[, allele], col = color)
  points(update, locusData[locusData$Update == update, allele], col = color, cex = 0.5)

  col_i = col_i + 1
}

dev.off()
