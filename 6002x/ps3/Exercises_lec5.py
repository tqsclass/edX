import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    count_triples = 0
    count_nottriples = 0
    for trial in range(numTrials):
        bucket = ['red','red','red','green','green','green']
        draws = []
        while len(bucket) > 3:
            draws.append(random.choice(bucket))
            bucket.remove(draws[-1])
            #print 'chose ',draws[-1],' bucket now ',bucket
        #print draws

        # score it!
        color = draws[0]
        isTriple = True
        for draw in range(1,len(draws)):
            #print 'Draw ',draw,': compare color ',color,' against ',draws[draw],
            if color != draws[draw]:
                #print ' ==> not 3 of a kind'
                isTriple = False
                count_nottriples += 1
                break
            else:
                pass
                #print ' looks good ... keep going',isTriple
                
        if isTriple == True:
            count_triples += 1
            
    #print count_triples, count_nottriples
    return count_triples / float(numTrials)

print noReplacementSimulation(1000000)
print noReplacementSimulation(1000000)
print noReplacementSimulation(1000000)

            
## As done by the graders
##def oneTrial():
##    '''
##    Simulates one trial of drawing 3 balls out of a bucket containing
##    3 red and 3 green balls. Balls are not replaced once
##    drawn. Returns True if all three balls are the same color,
##    False otherwise.
##    '''
##    balls = ['r', 'r', 'r', 'g', 'g', 'g']
##    chosenBalls = []
##    for t in range(3):
##        # For three trials, pick a ball
##        ball = random.choice(balls)
##        # Remove the chosen ball from the set of balls
##        balls.remove(ball)
##        # and add it to a list of balls we picked
##        chosenBalls.append(ball)
##    # If the first ball is the same as the second AND the second is the same as the third,
##    #  we know all three must be the same color.
##    if chosenBalls[0] == chosenBalls[1] and chosenBalls[1] == chosenBalls[2]:
##        return True
##    return False
##
##def noReplacementSimulation(numTrials):
##    '''
##    Runs numTrials trials of a Monte Carlo simulation
##    of drawing 3 balls out of a bucket containing
##    3 red and 3 green balls. Balls are not replaced once
##    drawn. Returns the a decimal - the fraction of times 3 
##    balls of the same color were drawn.
##    '''
##    numTrue = 0
##    for trial in range(numTrials):
##        if oneTrial():
##            numTrue += 1
##
##    return float(numTrue)/float(numTrials)

