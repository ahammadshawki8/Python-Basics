# module 26
# math module
import math

# we can see all the methods of math module.
print(dir(math))

# we can see that we have different important methods here.
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh',
#  'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh',
#  'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor',
#  'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 
# 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm',
#  'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

# calculate natural logarithm
print(math.log(10))

# calculate common logarithm
print(math.log10(100))

# calculate 2 based logarithm
print(math.log2(1024))

# calculate factorial of any number
print(math.factorial(9))

# calculate square root of any positive number
print(math.sqrt(100))

# calculate square root of any negative number.
# here the square root of any negative number is a complex number.
import cmath # we need to import cmath module which stands for complexmath
print(cmath.sqrt(-20))

# using floor method
# floor method rounds a number to its lower nearest integer.
print(math.floor(2.34))

# using ceil method
# ceil method rounds a number to its higher nearest integer.
print(math.ceil(2.34))

# print the value of pi
import math
print(math.pi)

# calculate the area of a circle.
def circle_area(radius):
    area=math.pi*(radius**2)
    return area
print(circle_area(10))

# using Euelers constant
print(math.e)

# convert degrees to radians
print(math.radians(180))

# convert radians to degrees
print(math.degrees(3))

# basic trigonometry
# using sin method
print(math.sin(math.pi/2))# here the arguement is given in radians.

# using cos method
print(math.cos(0))

# using tan method
print(math.tan(math.pi/4))

# calculate gcd of numbers
print(math.gcd(120,90))
