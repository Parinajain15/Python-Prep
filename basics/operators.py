# Q1. Create two numbers and perform: addition, subtraction, multiplication, division
#floor division, remainder, power
n1 = 1
n2 = 2
sub = n1 - n2
pro = n1 * n2
quo = n1 / n2
fd = n1 // n2
rem = n1 % n2
print(sum([n1, n2]), sub, pro, quo, fd, rem, pow(n1, n2))

# Q2. Take two integers as input. Print their sum, difference, product, quotient, remainder
n = int(input("Enter first number : "))
m = int(input("Enter second number : "))
sum = n+m
diff = n-m
pro = n*m
quo = n/m
rem = n%m
print(sum,diff,pro,quo,rem)

# Q3. Given: a = 17, b = 5. Predict the output: # a // b, a % b, a ** 2
a = 17
b = 5
print(a//b,a%b,a**2)
# 3, 2, 289

# Q4. Take a number as input. Check and print whether it is:
# greater than 50
# equal to 50
# less than 50
num = int(input("Enter a number : "))
print(num>50,num==50,num<50)

# Q5. Take a person's age as input.
# Print True if the person is between 18 and 60 (inclusive).
# Otherwise print False. Use 'and'.
age = int(input("Enter your age : "))
print(18<age and age<=60)

# Q6. Take a number as input.
# Print True if the number is either negative or greater than 100.
# Otherwise print False. Use 'or'.
num = int(input("Enter a number : "))
print(num<0 or num>100)

# Q7. Start with: x = 10. Use assignment operators to:
# add 5, subtract 2, multiply by 3, divide by 2, print x after each operation.
x = 10
print(x)
x+=5
print(x)
x-=2
print(x)
x*=3
print(x)
x/=2
print(x)

# Q10. Take two numbers as input. Print whether:
# 1. Both numbers are positive
# 2. At least one number is positive
# 3. Both numbers are equal
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
print(n1>0 and n2>0,n1>0 or n2>0,n1==n2)
