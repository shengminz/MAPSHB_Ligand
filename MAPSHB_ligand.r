library(gbm)
colname = c('res_aa', 'atom_aa', 'atom_ligand', 'chrg_aa', 'chrg_ligand', 'res_aa_n3', 'res_aa_n2', 'res_aa_n1',  
            'res_aa_1', 'res_aa_2', 'res_aa_3', "pKa", "pKb", "logP", "aa_atom", "seq_num_aa", 
            "name_ligand", "atom_ligand", "seq_num_ligand", "distance")
# Load data and model
load("./MAPSHB_Ligand.RData")
x_test <- read.csv("./temp", header=F, sep="", col.names = colname)
x_test$atom_ligand[which(is.na(x_test$atom_ligand))] = "NA"
pred_prob <- matrix(0, dim(x_test)[1], 10)

# Factorize variable
for(i in 1:11){
  x_test[, i] <- factor(x_test[, i], levels=levels(train_hb[, i]))
}

# Make prediction
for(i in 1:10){
  pred_prob[ , i] <- predict(models[[i]], x_test, n.trees = 5000, type="response")
}
if (length(pred_prob[,1:10]) == 10) {
  prob <- mean(pred_prob[,1:10])
} else {
  prob <- apply(pred_prob[,1:10], 1, mean)
}

# Creat output file
output <- data.frame(x_test[, c(1, 16, 15, 17, 19, 18, 20)], prob)
aa <- 0
ligand <- 0
for(i in 1:dim(output)[1]){
  aa[i] = paste(paste(as.character(output[i, 1]), as.character(output[i, 2]), sep="_"), as.character(output[i, 3]), sep="@")
  ligand[i] = paste(paste(as.character(output[i, 4]), as.character(output[i, 5]), sep="_"), as.character(output[i, 6]), sep="@")
}
output_data <- data.frame(aa, ligand, output[, 7], output[, 8])
names(output_data) <- c("Amino Acid", "Ligand", "R from structure (A)", "Predicted Probability")

# Write csv file
write.csv(output_data, "predict_results.csv")
