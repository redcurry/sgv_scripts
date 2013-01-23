# Get command-line arguments, which must be specified after the '--args' flag
args = commandArgs(T)

if(length(args) < 1)
{
  print('Arguments: input_path output_path')
  q()
}

input_path = args[1]
output_path = args[2]

data = read.table(input_path, header = T, stringsAsFactors = F)

pdf(file = output_path, width = 8.5, height = 11)
par(mfrow = c(20, 1), mar = c(0,0,0,0), mai = c(0,0,0,0),
  col.lab = 'white', col.axis = 'white')

for(locus in unique(data$Locus))
{
  locusData = data[data$Locus == locus,]
  locusData = locusData[, 3:28]
  locusMatrix = as.matrix(locusData)
  locusMatrix = t(locusMatrix)
  barplot(locusMatrix, space = 0, border = F, col = rainbow(26),
    axes = F, axesnames = F)
}
