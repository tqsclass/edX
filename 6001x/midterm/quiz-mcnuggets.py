def McNuggets(n):


    max20 = n / 20
    max9 = n/9
    max6 = n/6

    #print 'Testing ',n,max6,max9,max20

    for a in range(max6+1):
        for b in range(max9+1):
            for c in range(max20+1):
                if (6*a +9*b +20*c) == n:
                    #print a,b,c,' will do it for ',  n
                    return True
    return False;


print McNuggets(20)
print McNuggets(9)
print McNuggets(6)
print McNuggets(15)
print McNuggets(18)
print McNuggets(200)

