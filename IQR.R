#get B raw data
B_length = read.table("/Users/hien/OneDrive - National University of Ireland, Galway/Documents/R/indu/box_plot/box_plot_sample_2B/raw_B/2B_raw_fragment_length",sep="\t", header = FALSE)
colnames(B_length) = c("length")
Q3_B = quantile(B_length$length, 0.75)
Q1_B = quantile(B_length$length, 0.25)
#get B data
B_length = read.table("/Users/hien/OneDrive - National University of Ireland, Galway/Documents/R/indu/box_plot/box_plot_sample_2B/2B_fragment_length",sep="\t", header = FALSE)
colnames(B_length) = c("length")
Q3_B = quantile(B_length$length, 0.75)
Q1_B = quantile(B_length$length, 0.25)

#get D data
D_length = read.table("/Users/hien/OneDrive - National University of Ireland, Galway/Documents/R/indu/box_plot/box_plot_human/2D_fragment_length",sep="\t", header = FALSE)
colnames(D_length) = c("length")
Q3_D = quantile(D_length$length, 0.75)
Q1_D = quantile(D_length$length, 0.25)

#get G data
G_length = read.table("/Users/hien/OneDrive - National University of Ireland, Galway/Documents/R/indu/box_plot/box_plot_human/2G_fragment_length",sep="\t", header = FALSE)
colnames(G_length) = c("length")
Q3_G = quantile(G_length$length, 0.75, type = 2)
Q1_G = quantile(G_length$length, 0.25, type = 2)

#get J data
J_length = read.table("/Users/hien/OneDrive - National University of Ireland, Galway/Documents/R/indu/box_plot/box_plot_human/2J_fragment_length",sep="\t", header = FALSE)
colnames(J_length) = c("length")
Q3_J = quantile(J_length$length, 0.75, type = 2)
Q1_J = quantile(J_length$length, 0.25, type = 2)

#get E data
E_length = read.table("/Users/hien/OneDrive - National University of Ireland, Galway/Documents/R/indu/box_plot/box_plot_pfalciparum/2E_fragment_length",sep="\t", header = FALSE)
colnames(E_length) = c("length")
Q3_E = quantile(E_length$length, 0.75, type = 2)
Q1_E = quantile(E_length$length, 0.25, type = 2)

#get F data
F_length = read.table("/Users/hien/OneDrive - National University of Ireland, Galway/Documents/R/indu/box_plot/box_plot_ecuniculi/2F_fragment_length",sep="\t", header = FALSE)
colnames(F_length) = c("length")
Q3_F = quantile(F_length$length, 0.75, type = 2)
Q1_F = quantile(F_length$length, 0.25, type = 2)

#get I data
I_length = read.table("/Users/hien/OneDrive - National University of Ireland, Galway/Documents/R/indu/box_plot/box_plot_ecuniculi/2I_fragment_length",sep="\t", header = FALSE)
colnames(I_length) = c("length")
Q3_I = quantile(I_length$length, 0.75, type = 2)
Q1_I = quantile(I_length$length, 0.25, type = 2)

#get L data
L_length = read.table("/Users/hien/OneDrive - National University of Ireland, Galway/Documents/R/indu/box_plot/box_plot_ecuniculi/2L_fragment_length",sep="\t", header = FALSE)
colnames(L_length) = c("length")
Q3_L = quantile(L_length$length, 0.75, type = 2)
Q1_L = quantile(L_length$length, 0.25, type = 2)
