# Week 2 - Climate Change
climate = read.csv('data/climate_change.csv')
str(climate)
summary(climate)

train = subset(climate,Year <= 2006)
test  = subset(climate,Year > 2006)

model1 = lm(Temp ~ MEI + CO2 + CH4 + N2O + CFC.11 + CFC.12 + TSI + Aerosols, data=train)
model1
summary(model1)

cor(train)
cor(train) > 0.70

model_n2o = lm(Temp ~ MEI + TSI + N2O + Aerosols,data=train)
str(model_n2o)
summary(model_n2o)

model3 = step(model1)
model3
summary(model3)

temps = predict(model3, newdata=test)
temps
test$Temp
test$Temp - temps

sse = sum((temps - test$Temp)^2)
sst = sum((mean(train$Temp)- test$Temp)^2)
sse
sst
R2 = 1 - sse/sst
R2


