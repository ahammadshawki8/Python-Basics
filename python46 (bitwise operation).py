# Bitwise operators

# bitwise operators does operations on bits,
# it doesn't do operations with the value.

# What is bits?
# when we convert the values to binary,
# the 0's and 1's are called bits.
# BTW:
    # we can convert integers to binary using bin() function.
    # we can convert binary to integers using int() function.
    
# there are 6 bitwise operators in python.
# 1. Bitwise AND            %
# 2. Bitwise OR             |
# 3. Bitwise XOR            ^
# 4. Bitwise Complement     ~
# 5. Bitwise Left Shift     <<
# 5. Bitwise Right Shift    >>

# Bitwise AND
a = 20
b = 4
print(a & b)
# the answer gives us 4
# Why?
# Note:
    # In bitwise AND:
        # if all the input is 1, then the output is 1
        # otherwise 0
# so the binary forms of 20 and 4 are 00010100 ans 00000100 respectively.
# after applying bitwise AND operator the output will be 00000100(bin),
# which is 4 in decimal.

# Bitwise OR
a = 20
b = 4
print(a | b)
# the answer is 20
# Why?
# Note:
    # In bitwise OR:
        # if any of the input is 1, then the output is 1
        # if all the input is 0, then output 0
# so after applying bitwise OR operator in 00010100 and 00000100,
# we get 00010100(bin) which is 20(dec)

# Bitwise Xor:
a = 20
b = 4
print(a ^ b)
# the answer is 16
# Why:
# Note:
    # In bitwise XOR:
        # if all inputs are same, then the output is 0.
        # if they are different then 1.
# so after applying bitwise XOR operator in  00010100 and 00000100,
# we get 00010000(bin) which is 16(dec)

# Bitwise Complement:
# this is also called as bitwise not operator.
# it is an unary operater (means contains one operand)
# NOTE:
    # this operator flips the bits,
        # 0 becomes 1 and 1 becomes 0 in output.
a = 20
print(~20)
# the answer is -21
b = 50
print(~50)
# the answer is -51
# NOTE:
    # the formula of bitwise complement operator.
        # (~x) = -(x+1)
# as the binary of 2 is 00010100, if we use bitwise complement in it,
# it becomes 11101011 which is the binary form of -21

# Bitwise Left Shift:
# it will shift the bits towards left.
# the genereal form is:
    # x << n ; x is the integer and n is total number of shifts.
a = 20
print(a << 2)
# we can see that the answer is 80.
# the binary of 2 in 00010100, after the bitwise left shift operation,
# we get 01010000 which is the binary of 80.
# NOTE:
    # it is not a circular shift that -
        # we need to add the first shifted bits to the end of the binary number.
    # we need to always add 0's at the end of the binary number.
    # this wont channge for either positive or negative number.

# Bitwise Right Shift:
# it will shift the bits towards right.
# the genereal form is:
    # x >> n ; x is the integer and n is total number of shifts.
a = 20
print(a >> 2)
# we can see that the answer is 5.
# the binary of 2 in 00010100, after the bitwise right shift operation,
# we get 00000101 which is the binary of 5.
# NOTE:
    # it is not a circular shift that -
        # we need to add the last shifted bits to the fronnt of the binary number.
    # if the number is positive,
        # we need to add 0's at the front of the binary number.
    # if the number is negative,
        # we need to add 1's at the front of the binary number.

# NOTE:
    # Adding numbers matters in bitwise right shift(>>), but not in bitwise left shift(<<).
