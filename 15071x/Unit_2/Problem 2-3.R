#Problem Set 2 Problem 3
FluTrain = read.csv('data/FluTrain.csv')
str(FluTrain)
summary(FluTrain)


# correct is:  subset(FluTrain, ILI == max(ILI)
#         or:  which.max(FluTrain$ILI)
max(FluTrain$ILI)
week = subset(FluTrain, FluTrain$ILI > 7.4)
week

max(FluTrain$Queries)
week = subset(FluTrain, FluTrain$Queries > 0.99)
week

hist(FluTrain$ILI)
plot(FluTrain$Queries, log(FluTrain$ILI))

FluTrend1 = lm(log(ILI) ~ Queries, data=FluTrain)
FluTrend1
summary(FluTrend1)

c = cor(log(FluTrain$ILI),FluTrain$Queries)
c

FluTest = read.csv('data/FluTest.csv')
str(FluTest)
summary(FluTest)

PredTest1 = exp(predict(FluTrend1, newdata=FluTest))
which(FluTest$Week == "2012-03-11 - 2012-03-17")
PredTest1[11]

( FluTest$ILI[11] - PredTest1[11])/ FluTest$ILI[11]

# The RMSE can be calculated by first computing the SSE:
#     
#     SSE = sum((PredTest1-FluTest$ILI)^2)
# 
# and then dividing by the number of observations and taking the square root:
#     
#     RMSE = sqrt(SSE / nrow(FluTest))
# 
# Alternatively, you could use the following command:
#     
#     sqrt(mean((PredTest1-FluTest$ILI)^2)).
sqrt(mean((PredTest1-FluTest$ILI)^2))


# Section 4
install.packages("zoo")
library(zoo)

ILILag2 = lag(zoo(FluTrain$ILI), -2, na.pad=TRUE)
FluTrain$ILILag2 = coredata(ILILag2)
summary(ILILag2)

plot(log(ILILag2),log(FluTrain$ILI))


FluTrend2 = lm(log(ILI) ~ Queries+log(ILILag2), data=FluTrain)
FluTrend2
summary(FluTrend2)

#Section 5
ILILag2 = lag(zoo(FluTest$ILI), -2, na.pad=TRUE)
FluTest$ILILag2 = coredata(ILILag2)
summary(ILILag2)


FluTrain$ILI[416:417]
FluTest$ILILag2[1:4]
FluTest$ILILag2[1] = FluTrain$ILI[416]
FluTest$ILILag2[2] = FluTrain$ILI[417]
FluTest$ILILag2[1:4]

PredTest2 = exp(predict(FluTrend2, newdata=FluTest))

# We can obtain the test-set predictions with:
#     
#     PredTest2 = exp(predict(FluTrend2, newdata=FluTest))
# 
# And then we can compute the RMSE with the following commands:
#     
#     SSE = sum((PredTest2-FluTest$ILI)^2)
# 
# RMSE = sqrt(SSE / nrow(FluTest))
# 
# Alternatively, you could use the following command to compute the RMSE:
#     
#     sqrt(mean((PredTest2-FluTest$ILI)^2)).
# 
# The test-set RMSE of FluTrend2 is 0.294.
sqrt(mean((PredTest2-FluTest$ILI)^2))




