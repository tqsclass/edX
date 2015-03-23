def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    guess = 1
    if isMyNumber(guess) == 0:
        return guess
    foundNumber = False
    while not foundNumber:
        sign = isMyNumber(guess)
        print 'guess was: ', guess, ' return ',sign
        if sign == -1:
            guess += 1
        elif sign == 1:
            guess -= 1
        elif sign == 0:
            foundNumber = True
    return guess


def isMyNumber(guess):
    secret = 4
    if guess > secret:
        return 1
    elif guess < secret:
        return -1
    else:
        return 0


    
