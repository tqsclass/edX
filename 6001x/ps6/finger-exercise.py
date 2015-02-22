class Queue(object):

    def __init__(self):
        self.queue = []

    def insert(self,e):
        self.queue.append(e)
        #print self.queue

    def remove(self):
        if len(self.queue) > 0:
            e = self.queue[0]
            del self.queue[0]
            #print self.queue
            return e
        else:
            raise ValueError()


q = Queue()
q.insert(3)
q.insert(7)
q.insert(6)
q.insert(8)
q.remove()
print q.insert(22)
print q
print q.remove()
print q.remove()
print q.remove()
print q.remove()
print q.remove()
print q.remove()
print q.remove()
print q.remove()





class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self,s2):
        assert type(s2) == type(self)
        iset = intSet()
        for val in self.vals:
            if s2.member(val):
                iset.insert(val)
        return iset
        
        return self.intersection(s2)
        

    def __len__(self):
        #assert type(self) == type(s)
        return len(self.vals)















class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
        
    def __eq__(self,o):
        assert type(other) == type(self)
        if (self.x == o.x) and (self.y == o.y):
            return True
        else:
            return False

    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ', '+str(self.getY()) + ')'

