#Conversion = broad term
#Casting = explicit conversion
#input() always gives you a str unless u explicitly typecast it
#bool("") = False as empty string
#bool("hello") = True as non empty
#bool("False") = True as non empty
#bool([]) = False as empty collection
#bool([1, 2]) = True as non empty collection 
#bool(0) = False as zero number
#bool(-5) = True as non zero number

# Q1. Convert the following values to the required types and print them.
# "50" → int
# "25.5" → float
# 100 → str
# 1 → bool
a = int("50")
b = float("25.5")
c = str(100)
d = bool(1)
print(a,b,c,d)

# Q2. Take two numbers as input and print their sum.
n1 = int(input("Type first number : "))
n2 = int(input("Type second number : "))
print(n1+n2)

# Q3. Take a person's age as input and print:
# "You are X years old"
# where X is the entered age.
age = int(input("Enter your age : "))
print("You are",age,"years old.")

# Q4. Predict the output before running.
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("0"))
print(bool("False"))
#false,true,false,true,true

# Q5. Fix this code so that it prints 30.
x = input()
y = input()
#print(x + y)
print(int(x)+int(y))

# Q6. What will be the type of x?
#x = int(input("Enter a number: "))
#int

# Q7. Take a decimal number as input and multiply it by 2.
# Print the result.
dec = float(input("Enter a decimal number : "))
print(dec*2) # implicit type conversion as python automatically handles the numeric types

# Q8. Take a number as input and print whether its value is True or False when converted to bool.
n = int(input("Enter a number : "))
print(bool(n))