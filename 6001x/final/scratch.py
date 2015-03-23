x = [2,1]
y = [2,1]
z = False
if x == y:
    if sorted(x) == sorted(y):
         if x.sort() == y.sort():
               z =  x.sort() == sorted(y)
print z


def sort1(lst):
    swapFlag = True
    iteration = 0
    while swapFlag:
        swapFlag = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                temp = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = temp
                swapFlag = True

        L = lst[:]  # the next 3 questions assume this line just executed
        print iteration, lst
        iteration += 1
    return lst

sort1(range(10,0,-1))
print

def sort2(lst):
    for iteration in range(len(lst)):
        minIndex = iteration
        minValue = lst[iteration]
        for j in range(iteration+1, len(lst)):
            if lst[j] < minValue:
                minIndex = j
                minValue = lst[j]
        temp = lst[iteration]
        lst[iteration] = minValue
        lst[minIndex] = temp

        L = lst[:]  # the next 3 questions assume this line just executed
        print iteration, lst
    return lst

rl = range(10,0,-1)
ul = [10,5,8,3,7,1]
sort2(rl)


def sort3(lst):
    out = []
    for iteration in range(0,len(lst)):
        new = lst[iteration]
        inserted = False
        for j in range(len(out)):
            if new < out[j]:
                out.insert(j, new)
                inserted = True
                break
        if not inserted:
            out.append(new)

        L = out[:]  # the next 3 questions assume this line just executed
        print iteration, out
    return out

print
print "unordered list: ",ul
sort3(ul)

def sort4(lst):
    def unite(l1, l2):
        print len(l1), len(l2)
        if len(l1) == 0:
            return l2
        elif len(l2) == 0:
            return l1
        elif l1[0] < l2[0]:
            return [l1[0]] + unite(l1[1:], l2)
        else:
            return [l2[0]] + unite(l1, l2[1:])

    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:
        front = sort4(lst[:len(lst)/2])
        back = sort4(lst[len(lst)/2:])

        L = lst[:]  # the next 3 questions assume this line just executed
        print "front back",front, back
        return unite(front, back)

rl = range(10,0,-1)
ol = range(1,11)
print
print "reverse list: ",rl
print sort4(rl)
print "\nunordered list: ",ul
print sort4(ul)
print "\nordered list: ",ol
print sort4(ol)

    
