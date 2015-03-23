class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name

def insert(atMe, newFrob):

    current = atMe
    inserted = False
    insert = False

    if current.myName() == newFrob.myName():
        #print ' they are equal'
        newFrob.setAfter(current.getAfter())
        newFrob.setBefore(current)
        current.setAfter(newFrob)
        if type(newFrob.getAfter()) != type(None):
                newFrob.getAfter().setBefore(newFrob)
        return

    #print '\nconsider ', newFrob.myName(), ' at ',current.myName()
    while newFrob.myName() >= current.myName():
        #print newFrob.myName(),' is greater than ',current.myName()
        if type(current.getAfter()) == type(None):
            #print newFrob.myName(),' is equal to ',current.myName()
            newFrob.setBefore(current)
            current.setAfter(newFrob)
            inserted = True
            #print 'they were > or equal, add at right end'
            return
        else:
            insert = True
            current = current.getAfter()
            #print newFrob.myName(),' has insert flag for ',current.myName()

     ## test for > but not at end
    if insert:
        #print 'enter insert block with current = ',current.myName(),current.getBefore().myName()     
        newFrob.setAfter(current)
        newFrob.setBefore(current.getBefore())
        current.setBefore(newFrob)
        newFrob.getBefore().setAfter(newFrob)
        inserted = True
        #print 'leave insert block with newFrob = ',newFrob.myName(),newFrob.getBefore().myName() ,newFrob.getAfter().myName()    
        return
            
                
    while newFrob.myName() <= current.myName():
        if type(current.getBefore()) == type(None):
            newFrob.setAfter(current)
            current.setBefore(newFrob)
            inserted = True
            #print 'they were < or equal, add at left end'
            return
        else:
            insert = True
            current = current.getBefore()

    if insert:
        newFrob.setAfter(current.getAfter())
        newFrob.setBefore(current)
        current.setAfter(newFrob)
        newFrob.getAfter().setBefore(newFrob)
        inserted = True
        return
    
    #print 'we fell through all of the loops'
    
def findFront(start):

    print start.myName()
    if type(start.getBefore()) != type(None):
        return findFront(start.getBefore())
    else:
        print 'at the front? ',start.myName()
        return start

    

eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')
betty = Frob('betty')
print eric.myName(), andrew.myName(), ruth.myName()

print '\n done with creation\n'

insert(eric, andrew)
print 'after eric, andrew ',eric.getBefore(), eric.getAfter()
print 'after eric, andrew ',andrew.getBefore(), andrew.getAfter()

insert(eric, ruth)
print 'after eric, ruth ',eric.getBefore(), eric.getAfter()
print 'after eric, ruth ',ruth.getBefore(), ruth.getAfter()

insert(eric, fred)
print 'after eric, fred ',eric.getBefore(), eric.getAfter()
print 'after eric, fred ',fred.getBefore(), fred.getAfter()

insert(ruth, martha)
print 'after ruth, martha ',ruth.getBefore(), ruth.getAfter()
print 'after ruth, martha ',martha.getBefore(), martha.getAfter()

insert(andrew,betty)
#insert(ruth,ruth)
#insert(eric,eric)

def printList(andrew):
    node = andrew
    print '\n\n',node.myName()
    while type(node.getAfter()) != type(None):
        print node.getAfter().myName()
        node = node.getAfter()
        
printList(andrew)

print '\nTest findFront'
front = findFront(martha)
print type(front),front.myName()
