counts <- read.csv(file="counts.csv", header=TRUE, sep=",")
datalist = list()
genes=sample(counts$X,2000,replace=FALSE)
for (i in 1:1000){
  x<-which(counts$X == genes[i])
  N  <-  5                                    # the number of random values to replace
  #row=counts[x,2:51]
  inds <- sample(1:40,N,replace=FALSE)
  gene=as.character(counts[x,1])
  sample=inds
  dat <- data.frame(gene,sample)
  datalist[[i]] <- dat 
  #inds <- round(runif(N, 1, length(row)))    # draw random values from [1, length(vec)]
  for (j in inds){counts[x,j+1] <- 0}         # use the random values as indicies to vec, for which to replace
}


for (y in 1001:2000){
  z<-which(counts$X == genes[y])
  N  <-  5                                    # the number of random values to replace
  #row=counts[y,52:101]
  inds1 <- sample(61:100,N,replace=FALSE)
  gene=as.character(counts[z,1])
  sample=inds1
  dat <- data.frame(gene,sample)
  datalist[[y]] <- dat 
    #inds <- round(runif(N, 1, length(row)))    # draw random values from [1, length(vec)]
  for (k in inds1){counts[y,k+1] <- 0}        # use the random values as indicies to vec, for which to replace
}
big_data = do.call(rbind, datalist)
write.table(big_data, file = "mock_key.tsv",row.names=FALSE, sep="\t", quote = FALSE)
write.table(counts, file = "Counts_0.tsv",row.names=FALSE, sep="\t", quote = FALSE)
