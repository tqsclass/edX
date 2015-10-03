# Problem Set 3 - Problem 1 Music Records

songs = read.csv('songs.csv')
table(songs$year)
mj = subset(songs,artistname=='Michael Jackson')

mj[c('songtitle','Top10')]

levels(as.factor(songs$timesignature))
table(songs$timesignature)
which.max(songs$tempo)


# Part 2 Prediction Model
SongsTest = subset(songs, year < 2010)
SongsTest = subset(songs, year == 2010)

nonvars = c("year", "songtitle", "artistname", "songID", "artistID")
SongsTrain = SongsTrain[ , !(names(SongsTrain) %in% nonvars) ]
SongsTest = SongsTest[ , !(names(SongsTest) %in% nonvars) ]

SongsLog1 = glm(Top10 ~ ., data=SongsTrain, family=binomial)
summary(SongsLog1)

# Part 3 multi coliniearity
cor(SongsTrain$loudness, SongsTrain$energy)
# this works for numberic variable
SongsLog2 = glm(Top10 ~ . - loudness, data=SongsTrain, family=binomial)
summary(SongsLog2)

SongsLog3 = glm(Top10 ~ . - energy, data=SongsTrain, family=binomial)
summary(SongsLog3)


# Part 4 Predictions with Test set
predictTest = predict(SongsLog3, type="response", newdata=SongsTest)
table(SongsTest$Top10, predictTest>0.45)

# accuracy = TN + TP divided by N
(309+19)/(309+19+40+5)

# baseline = we guess "not a hit" everytime
(309+5)/(309+19+40+5)
# also use this with acc = (total not hits)(total n)
table(SongsTest$Top10)
table(SongsTest$Top10, predictTest>0.45)

# sensitivity = TP / (TP+FN)
19/(59)
# specificity = TN / (TN + FP)
309/(314)
