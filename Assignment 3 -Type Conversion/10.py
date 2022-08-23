'''Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and display the result in binary format'''
a = 0o25 #octal number
b = 0x39 #hexadecimal number
a1 = bin(a)
b1 = bin(b)
add = a1+b1
print("Sum of Binary number is",add)