# Unit 4 Problem 2

letters = read.csv("letters_ABPR.csv")
letters$isB = as.factor(letters$letter == "B")

library(caTools)
set.seed(1000)
spl = sample.split(letters$isB, SplitRatio = 0.5)
train = subset(letters, spl==TRUE)
test = subset(letters, spl==FALSE)

table(test$isB)
1175/(1175+383)

library(rpart)
library(rpart.plot)
CARTb = rpart(isB ~ . - letter, data=train, method="class")
prp(CARTb)

# Make predictions
PredictCARTb = predict(CARTb, newdata = test, type = "class")
table(test$isB, PredictCARTb)

library(randomForest)

# Build random forest model
set.seed(1000)
forest = randomForest(isB ~ . - letter, data=train, method="class")

# Make predictions
PredictForest = predict(forest, newdata = test)
table(test$isB, PredictForest)

(374+1165)/(374+1165+10+9)

# Secion 2
letters$letter = as.factor( letters$letter )
set.seed(2000)
spl = sample.split(letters$letter, SplitRatio = 0.5)
train = subset(letters, spl==TRUE)
test = subset(letters, spl==FALSE)

table(test$letter)
401/nrow(test)

CARTl = rpart(letter ~ . - isB, data=train, method="class")
prp(CARTl)

# Make predictions
PredictCARTl = predict(CARTl, newdata = test, type = "class")
table(test$letter, PredictCARTl)
(348+318+363+340)/nrow(test)

# Build random forest model
set.seed(1000)
forest2 = randomForest(letter ~ . - isB, data=train)

# Make predictions
PredictForest2 = predict(forest2, newdata = test)
table(test$letter, PredictForest2)

(380+373+391+383)/nrow(test)

