# Problem Set 4 Problem 1
#
#
gerber = read.csv("gerber.csv")
str(gerber)
summary(gerber)

voters = subset(gerber, gerber$voting == 1)
nrow(voters)/nrow(gerber)

tapply(gerber$voting, gerber$civicduty, mean)
tapply(gerber$voting, gerber$hawthorne, mean)
tapply(gerber$voting, gerber$self, mean)
tapply(gerber$voting, gerber$neighbors, mean)

logicM = glm(voting ~ neighbors + civicduty + self + hawthorne, data=gerber, family=binomial)
summary(logicM)

predict = predict(logicM, type="response")
table(gerber$voting, predict > 0.3)
(51966+134513)/(51966+134513+56730+100875)

table(gerber$voting, predict > 0.5)
# MODEL ONLY PREDICTS FALSE

library(ROCR)
ROCRpred = prediction(predict, gerber$voting)
auc = as.numeric(performance(ROCRpred, "auc")@y.values)

ROCRperf = performance(ROCRpred, "tpr", "fpr")
plot(ROCRperf)
plot(ROCRperf, colorize=TRUE)

# section 2
library(rpart)
library(rpart.plot)
CARTmodel = rpart(voting ~ civicduty + hawthorne + self + neighbors, data=gerber)
prp(CARTmodel)
CARTmodel2 = rpart(voting ~ civicduty + hawthorne + self + neighbors, data=gerber, cp=0.0)
prp(CARTmodel2)


civicvoters = subset(voters,voters$civicduty == 1)
civic = subset(gerber,gerber$civicduty == 1)
# nrow each and divide = % of civic duty voting

CARTmodel3 = rpart(voting ~ civicduty + hawthorne + self + neighbors + sex, data=gerber, cp=0.0)
prp(CARTmodel3)

control = subset(voters, voters$control == 1)
male = subset(control, sex == 0)
nrow(male)/nrow(control)

# section 3

CARTmodel4 = rpart(voting ~ control, data=gerber, cp=0.0)
CARTmodel5 = rpart(voting ~ control + sex, data=gerber, cp=0.0)
prp(CARTmodel4, digits=6)
prp(CARTmodel5, digits=6)
abs(0.296638 - 0.34)

LogModelSex = glm(voting ~ control + sex, data=gerber, family=binomial)
summary(LogModelSex)

Possibilities = data.frame(sex=c(0,0,1,1),control=c(0,1,0,1))
predict1 = predict(LogModelSex, newdata=Possibilities, type="response")
predict1

abs(predict1[4] - 0.290456)

LogModel2 = glm(voting ~ sex + control + sex:control, data=gerber, family="binomial")
summary(LogModel2)

predict2 = predict(LogModel2, newdata=Possibilities, type="response")
predict2
abs(predict2[4] - 0.290456)


