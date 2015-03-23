#Exercises Unit 2

#
wines = read.csv('data/wine.csv')
str(wines)
summary(wines)
modelQQ4 = lm(Price ~ HarvestRain + WinterRain, data=wines)
cor(wines$HarvestRain,wines$WinterRain)

