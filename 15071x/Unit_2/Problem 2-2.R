#Problem Set 2 problem 2
pisaTrain = read.csv('data/pisa2009train.csv')
pisaTest = read.csv('data/pisa2009test.csv')

str(pisaTrain)
str(pisaTest)
summary(pisaTrain)
summary(pisaTest)

tapply(pisaTrain$readingScore,pisaTrain$male==1,mean)

pisaTrain = na.omit(pisaTrain)
pisaTest = na.omit(pisaTest)
str(pisaTrain)
str(pisaTest)

summary(testPisa$raceeth)
pisaTrain$raceeth = relevel(pisaTrain$raceeth, "White")
pisaTest$raceeth = relevel(pisaTest$raceeth, "White")

lmScore = lm(readingScore ~ .,data=pisaTrain)
lmScore
summary(lmscore)

predictions = predict(lmScore,pisaTrain)

# Compute  R^2
SSE = sum((predictions - pisaTrain$readingScore)^2)
SST = sum((mean(pisaTrain$readingScore) - pisaTrain$readingScore)^2)
R2 = 1 - SSE/SST
R2

# Compute the RMSE
RMSE = sqrt(SSE/nrow(pisaTrain))
RMSE

## Alternate Way (correct way!)
#The training-set RMSE can be computed by first computing the SSE:
#    
#    SSE = sum(lmScore$residuals^2)
# 
# and then dividing by the number of observations and taking the square root:
#     
#     RMSE = sqrt(SSE / nrow(pisaTrain))
# 
# A alternative way of getting this answer would be with the following command:
#     
#     sqrt(mean(lmScore$residuals^2)).

# following gives incorrect answer, but I guessed correctly....
# just look it up from summary(lmScore) grade coefficent * 2 grades
grade9 = subset(pisaTrain,pisaTrain$grade ==9)
grade11 = subset(pisaTrain,pisaTrain$grade == 11)
mean(predict(lmScore,grade9))
mean(predict(lmScore,grad11))

predTest = predict(lmScore, newdata = pisaTest)
summary(predTest)


# Compute  R^2 test set
# correct:  This can be calculated with sqrt(mean((predTest-pisaTest$readingScore)^2)).
SSE = sum((predTest - pisaTest$readingScore)^2)
SST = sum((mean(pisaTrain$readingScore) - pisaTest$readingScore)^2)
SSE
SST
R2 = 1 - SSE/SST
R2

# Compute the RMSE
RMSE = sqrt(SSE/nrow(pisaTest))
RMSE

summary(pisaTrain)

# correct -> baseline = mean(pisaTrain$readingScore)
# correct -> This can be computed with sum((baseline-pisaTest$readingScore)^2)
SSE_Baseline = sum((518.00 - pisaTest$readingScore)^2)
SSE_Baseline
