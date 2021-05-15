#plot
bitmap("2FIL_boxplot.tiff",res = 300)
#get data
FIL_data = read.table("/Users/hien/OneDrive - National University of Ireland, Galway/Documents/R/indu/box_plot/box_plot_ecuniculi/2FIL_boxplot_header",sep="\t", header = TRUE)
#box_plot
boxplot(FIL_data$fragment_length ~ FIL_data$sample, main = "The fragment length on genome of sample 2F, 2I, 2L", col=c("blue","green","yellow"),xlab = "fragment length",ylab="sample", cex=.3, horizontal = TRUE)
abline(v = 159, lty = "dotted", col = "black")
axis(1, at=159,labels=159)
invisible(dev.off())