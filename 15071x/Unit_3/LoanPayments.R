# Problem Set 3 Problem 3  Loan Payments
loans = read.csv("loans.csv")
str(loans)
summary(loans)

table(loans$not.fully.paid)

missing = subset(loans, is.na(log.annual.inc) | is.na(days.with.cr.line) | is.na(revol.util) | is.na(inq.last.6mths) | is.na(delinq.2yrs) | is.na(pub.rec))
nrow(missing)
table(missing$not.fully.paid)

install.packages("mice")

library(mice)

set.seed(144)

vars.for.imputation = setdiff(names(loans), "not.fully.paid")

imputed = complete(mice(loans[vars.for.imputation]))

loans[vars.for.imputation] = imputed
#Imputation predicts missing variable values for a given observation using the variable values that are reported. We called the imputation on a data frame with the dependent variable not.fully.paid removed, so we predicted the missing values using only other independent variables.

# Section 2
loans = read.csv('loans_imputed.csv')
set.seed(144)
split = sample.split(loans$not.fully.paid, SplitRatio = 0.70)

train = subset(loans, split==TRUE)
test = subset(loans, split==FALSE)

model1 = glm(not.fully.paid ~ ., data=train, family=binomial)
summary(model1)

#1) If we have a coefficient c for a variable, then that means the log odds (or Logit) are increased by c for a unit increase in the variable.

#2) If we have a coefficient c for a variable, then that means the odds are multiplied by e^c for a unit increase in the variable.

#Because Application A is identical to Application B other than having a FICO score 10 lower, its predicted log odds differ by -0.009317 * -10 = 0.09317 from the predicted log odds of Application B.
#Using the answer from the previous question, the predicted odds of loan A not being paid back in full are exp(0.09317) = 1.0976 times larger than the predicted odds for loan B. Intuitively, it makes sense that loan A should have higher odds of non-payment than loan B, since the borrower has a worse credit score.


