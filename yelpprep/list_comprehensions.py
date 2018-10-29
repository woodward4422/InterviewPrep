# This is a practice for list comprehensions on HackerRank
# Given values for the dimension of a cuboid X,Y,Z find all the values of the vertexes such that x + y + z != N, which is another number inputted 
import sys 

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
n = int(sys.argv[4])

coordinates = [[x,y,z] for x in xrange(a+1) for y in xrange(b+1) for z in xrange(c+1) if (x+y+z) != n]

print(coordinates)