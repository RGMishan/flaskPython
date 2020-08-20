class Point:
    def __init__(self,i,j): #init means info that we need 
        #self is variable representing the class i and j are values 
        self.i = i #access the point i value and store in self.i
        self.j = j

p = Point(3,5) #create new point with init and pass the value in point
print(p.i)
print(p.j)