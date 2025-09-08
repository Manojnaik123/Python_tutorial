# Using the bin function we can convert the decimal number to the binary number
x = 2
y = bin(x)
print(y) # prints 0b10

# decimal to octal conversion
z = oct(x)
print(z) # prints 0o2

# decimal to the hexa conversion
r = hex(11)
print(r) # 0xb


# binary to decimal conversion
print(int(y, 2))
print(int(z, 8))
print(int(r, 16))

n = 10
a,b = 0,1
for x in range(n):
    print(a)
    temp = a
    a = b
    b = temp + b


# Factorial of a number

# ---------------------------------------------------
print('-----------------------------------------------------------------')

def factorial(num):
    temp = 1
    for x in range(1, num+1):
        temp = temp*x
    return temp

print(factorial(5))

