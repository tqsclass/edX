IBM = read.csv("data/IBMStock.csv")
GE = read.csv("data/GEStock.csv")
Boeing = read.csv("data/BoeingStock.csv")
CocaCola = read.csv("data/CocaColaStock.csv")
ProcterGamble = read.csv("data/ProcterGambleStock.csv")

IBM$Date= as.Date(IBM$Date, "%m/%d/%y")
GE$Date = as.Date(GE$Date, "%m/%d/%y")
Boeing$Date = as.Date(Boeing$Date, "%m/%d/%y")
CocaCola$Date = as.Date(CocaCola$Date, "%m/%d/%y")
ProcterGamble$Date = as.Date(ProcterGamble$Date, "%m/%d/%y")

summary(IBM)
summary(GE)
summary(Boeing)
summary(CocaCola)
summary(ProcterGamble)

sd(ProcterGamble$StockPrice)

plot(CocaCola$Date,CocaCola$StockPrice,col="red")
lines(ProcterGamble$Date, ProcterGamble$StockPrice,col="blue")
abline(v=as.Date(c("2000-03-01")), lwd=2)
abline(v=as.Date(c("1983-03-01")), lwd=2)

plot(CocaCola$Date[301:432], CocaCola$StockPrice[301:432], type="l", col="red", ylim=c(0,210))
lines(ProcterGamble$Date[301:432], ProcterGamble$StockPrice[301:432],col="green")
lines(IBM$Date[301:432], IBM$StockPrice[301:432],col="blue")
lines(Boeing$Date[301:432], Boeing$StockPrice[301:432],col="orange")
lines(GE$Date[301:432], GE$StockPrice[301:432],col="purple")
abline(v=as.Date(c("2000-03-01")), lwd=2)
abline(v=as.Date(c("1997-09-01")), lwd=2)
abline(v=as.Date(c("1997-11-01")), lwd=2)
abline(v=as.Date(c("2004-01-01")), lwd=2)
abline(v=as.Date(c("2005-01-01")), lwd=2)

tapply(IBM$StockPrice,months(IBM$Date),mean)
tapply(GE$StockPrice,months(GE$Date),mean)
tapply(Boeing$StockPrice,months(Boeing$Date),mean)
tapply(CocaCola$StockPrice,months(CocaCola$Date),mean)
tapply(ProcterGamble$StockPrice,months(ProcterGamble$Date),mean)




