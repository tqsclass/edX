#Section 1
getwd()
csp = read.csv('data/CPSData.csv')
cntry_code = read.csv('data/CountryCodes.csv')
metro_code = read.csv('data/MetroAreaCodes.csv')
str(csp)
summary(csp)
sort(table(csp$State)) 
sort(table(csp$Citizenship))
sum(sort(table(csp$Citizenship)))
sort(table(csp$Race))
table(csp$Race,csp$Hispanic)

#Section 2
table(csp$Region, is.na(csp$Married))
table(csp$Sex, is.na(csp$Married))
table(csp$Age, is.na(csp$Married))
table(csp$Citizenship, is.na(csp$Married))

table(csp$State, is.na(csp$MetroAreaCode))
table(csp$Region, is.na(csp$MetroAreaCode))
tapply(is.na(csp$MetroAreaCode),csp$State,mean)
sort(tapply(is.na(csp$MetroAreaCode),csp$State,mean))

#Section 3
csp = merge(csp,metro_code,by.x="MetroAreaCode",by.y="Code",all.x=TRUE)
str(csp)
summary(csp)
sort(tapply(csp$Hispanic,csp$MetroArea,mean))
sort(tapply(csp$Race=='Asian',csp$MetroArea,mean))
sort(tapply(csp$Education == "No high school diploma", csp$MetroArea, mean,na.rm=TRUE))

#Problem 4
csp = merge(csp,cntry_code,by.x="CountryOfBirthCode",by.y="Code",all.x=TRUE)
str(csp)
summary(csp)

tapply(csp$Country != 'United States',csp$MetroArea == 'New York-Northern New Jersey-Long Island, NY-NJ-PA',mean,na.rm=TRUE)
table(csp$MetroArea == "New York-Northern New Jersey-Long Island, NY-NJ-PA", csp$Country != "United States")

table(csp$MetroArea,csp$Country=='India')
table(csp$MetroArea,csp$Country=='Brazil')
table(csp$MetroArea,csp$Country=='Somalia')

#another, better way to do it!
sort(tapply(csp$Country == "India", csp$MetroArea, sum, na.rm=TRUE))
sort(tapply(csp$Country == "Brazil", csp$MetroArea, sum, na.rm=TRUE))
sort(tapply(csp$Country == "Somalia", csp$MetroArea, sum, na.rm=TRUE))
