library(poweRlaw)
library(ggplot2)
power_law_line <- function(pl){
  #get Xmin fitting power law
  xmin <- pl$getXmin()
  
  #Maximum likelihood estimation is a method 
  #that determines values for the parameters of a model.
  #For each value of xmin, the mle will be used
  alpha <- pl$getPars()
  
  #get x
  x <- pl$dat
  
  #data frame plotting power law line
  x_axis <- exp(seq(log(xmin),log(max(x)),length.out = 100))
  x_axis <- unique(round(x_axis))
  y <- 10^(-alpha * (log10(x_axis) - log10(pl$internal$values[xmin])) + log10(pl$internal$freq[xmin]))
  line_fit <- data.frame(x_axis, y)
  
  # Truncate for y < 1, keeping 1 extra
  keep <- length(which(line_fit$y >= 1)) + 1
  line_fit <- line_fit[1:keep, ]
}

plot_pl <- function(filename){
  bitmap(paste0("/Users/hien/OneDrive - National University of Ireland, Galway/Documents/R/indu/log_log_plot freq_copy_number_seq/",filename,".tiff"), res = 600)
  freq_table <- read.table(paste0("/Users/hien/OneDrive - National University of Ireland, Galway/Documents/indu/sample_2K/fastaptamer_2K/",filename))
  counts <- count(freq_table$V1)
  colnames(counts) <- c('Copy', 'Frequency')
  
  ####for power law line
  counts2 <- counts[counts$Frequency > 1, ]
  vals <- rep(counts2$Copy, counts2$Frequency)
  pl <- displ$new(vals)
  
  #set Xmin
  xmin <- 5
  pl$setXmin(xmin)
  
  #estimate_pars estimates the distribution’s parameters using their maximum likelihood estimator. 
  #This estimate is conditional on the current xmin value.
  pl$setPars(estimate_pars(pl))
  
  line_fit <- power_law_line(pl)
  #plot
  img <- ggplot(counts, aes(Copy, Frequency)) +
    geom_point(col='blue', size=2) +
    geom_line(data=line_fit, aes(x_axis, y), col='red', size=1.5) + theme_bw() +
    scale_x_log10(breaks=trans_breaks('log10', function(x) 10^x),
                  labels=trans_format('log10', math_format(10^.x)),limits = c(0.8,1e+7)) +
    scale_y_log10(breaks=trans_breaks('log10', function(x) 10^x),
                  labels=trans_format('log10', math_format(10^.x)),limits = c(0.8,1e+7)) +
    xlab("Copy Number") + ylab("Frequency") +
    annotate('text', x=70, y=70, label=paste(expression(alpha), '== ',
                                             format(round(pl$pars, 2), nsmall=2)), col='red', size=3.0, parse=TRUE)
  print(img)
  invisible(dev.off())
}
