library(ggplot2)
library(reshape2)
library(dplyr)
CDF_plot <- function(filename){
  bitmap(paste0("/Users/hien/OneDrive - National University of Ireland, Galway/Documents/R/indu/cumulative_freq_plot/",filename,".tiff"), res = 600)
  data <- read.table(paste0("/Users/hien/OneDrive - National University of Ireland, Galway/Documents/R/indu/box_plot/box_plot_sample_2A/test_",filename), header = TRUE)
  colnames(data) <- c("fragment_length")
  samples <- rep(filename,nrow(data))
  data <- cbind(samples,data)
  new_data <- data %>% filter(fragment_length %in% (90:220))
  img <- ggplot(new_data, aes(x = new_data$fragment_length),linetype=3) +
    stat_ecdf() +
    theme_bw() +
    xlab("mapped fragment length") +
    scale_x_continuous(breaks=c(0,90,100,110,120,130,140,150,160,170,180,190,200,210,220))
  print(img)
  invisible(dev.off())
}


