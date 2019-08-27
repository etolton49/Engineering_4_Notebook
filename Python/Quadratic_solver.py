import math
import sys


print("Quadratic Solver")
print("Enter the coefficients for ax^2 + bx + c")
x = int(input("a?"))
y = int(input("b?"))
z = int(input("c?"))

def IHateMath(a,b,c):
    discriminant = b**2 - (4*a*c)
    if discriminant < 0:#no real roots
        print("Oh no! No real roots.")
        sys.exit()
    else:
        roots = [(-1*b + math.sqrt(discriminant))/2*a, (-1*b - math.sqrt(discriminant))/2*a]
        
        return roots
print("Roots are:\t")
arr = IHateMath(x,y,z)
for a in arr:
    print(str(a))

