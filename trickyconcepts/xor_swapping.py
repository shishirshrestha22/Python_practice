#This is the program which swaps 2 values without using temporary variables.

a = 5
b = 10
print(f"before swapping a={a} & b={b}")
a = a^b
b = a^b
a = a^b
print("\nAfter Swapping:")
print(f"a is {a}")
print(f"b is {b}")


#explanation
# Take two numbers
# a = 5     binary: 0101
# b = 10    binary: 1010

# XOR rule:
# same bits -> 0
# different bits -> 1

# Step 1: a = a ^ b
# 0101 ^ 1010 = 1111 (15)
# a = a ^ b   # a becomes 15

# Step 2: b = a ^ b
# 1111 ^ 1010 = 0101 (5) -> original value of a
# b = a ^ b    b becomes 5

# Step 3: a = a ^ b
# 1111 ^ 0101 = 1010 (10) -> original value of b
# a = a ^ b    a becomes 10

# Final result: values are swapped
# print(a, b)   Output: 10 5
