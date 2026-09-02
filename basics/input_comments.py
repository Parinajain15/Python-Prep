# Q1. Take the user's name as input and print a greeting.
name = input("Enter your name : ")
print("Hello",name)

# Q2. Take two integers as input and print their:
# sum
# difference
# product
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
total = n1+n2
difference = n1-n2
product = n1*n2
print("sum : ",total,"difference :",difference,"product :",product)

# Q3. Take the user's name and age as input.
# Print: My name is X and I am Y years old.
name = input("Enter your name : ")
age = int(input("Enter your age : "))
print("My name is",name,"and I am",age,"years old.")

# Q4. Write a single-line comment explaining what the following code does.
x = int(input("Enter a number: "))
print(x * 2)
#takes a number from user converts it into integer type and multitplies it by 2 and gives output

# Q5. Write a program that takes a number as input and prints:
# "Even" if the number is even
# "Odd" if the number is odd
number = int(input("Enter any number : "))
if number % 2 == 0: 
    print("Even")
else: 
    print("Odd")
