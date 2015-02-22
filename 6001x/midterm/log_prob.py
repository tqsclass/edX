def myLog(x,b):
    '''
    x > 0
    b >= 2
    '''
    base = b
    count = 1

    if base > x:
        return 0
    else:
        value = base
        while value <= x:
            #print value, value*value, x
            value *= base
            count = count + 1
            if count > 10:
                break
        
    return count-1


#print myLog(16,2)
#print myLog(15,3)
#print myLog(2,3)

def laceStrings(s1,s2):

    lace = ''
    short = min(len(s1),len(s2))

    for i in range(short):
        lace = lace + s1[i]+s2[i]
        #print i, lace

    if len(s1) > len(s2):
        lace = lace + s1[short:]
    elif len(s1) < len(s2):
        lace = lace + s2[short:]
    else:
        pass  # strings were equal length

    return lace



def laceStringsRecurJK(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            #PLACE A LINE OF CODE HERE
            print 's1 empty? ',s1
            return s2
        if s2 == '':
            #PLACE A LINE OF CODE HERE
            print 's2 empty? ',s2
            return s1
        else:
            #PLACE A LINE OF CODE HERE
            print 's1: ',s1
            print 's2: ',s2
            return s1[0]+helpLaceStrings(s2,s1[1:],'')
    return helpLaceStrings(s1, s2, '')

def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return s2
        if s2 == '':
            return s1
        else:
            return s1[0]+helpLaceStrings(s2,s1[1:],'')
    return helpLaceStrings(s1, s2, '')



print laceStringsRecur('abcd','efghi')
print

print laceStringsRecur('abcde','fghi')
print laceStringsRecur('JK','jk')

        
    
