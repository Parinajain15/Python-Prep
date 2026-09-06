# Q1. Take a number as input. Print "Positive" if it is greater than 0,
# "Negative" if it is less than 0 and "Zero" if it is equal to 0.
n = int(input("Enter a number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# Q2. Take a number as input. Check whether it is even or odd. Print "Even" or "Odd".
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q3. Take a person's age as input. Print:
# "Child" if age is below 13
# "Teenager" if age is 13–19
# "Adult" if age is 20 or above
a = int(input("Enter your age: "))
if a < 13:
    print("Child")
elif 13 <= a <= 19:
    print("Teenager")
else:
    print("Adult")


# Q4. Take marks as input. Print:
# "A" for 90–100
# "B" for 80–89
# "C" for 70–79
# "D" for 60–69
# "F" for below 60
m = int(input("Enter marks: "))
if 90 <= m <= 100:
    print("A")
elif 80 <= m <= 89:
    print("B")
elif 70 <= m <= 79:
    print("C")
elif 60 <= m <= 69:
    print("D")
else:
    print("F")


# Q5. Take two numbers as input. Print which number is greater.
# If they are equal, print "Both are equal."
n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
if n > m:
    print("First number is greater")
elif n < m:
    print("Second number is greater")
else:
    print("Both numbers are equal")


# Q6. Take a number as input. Check whether it is divisible by both 3 and 5. Print True or False.
n = int(input("Enter a number: "))
if n % 3 == 0 and n % 5 == 0:
    print("True")
else:
    print("False")


# Q7. Take a person's age as input. Print "Eligible" if the age is between 18 and 60 (inclusive).
# Otherwise print "Not eligible."
a = int(input("Enter your age: "))
if 18 <= a <= 60:
    print("Eligible")
else:
    print("Not eligible")


# Q8. Take three numbers as input.
# Print the largest number.
# If there is a tie for the largest value, your program
# should still work correctly.
n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
o = int(input("Enter third number: "))
print(max(n, m, o))


# Q9. Take a username and password as input.
# Print "Login successful" only if:
# username is "admin"
# AND password is "1234"
# Otherwise print "Invalid credentials."
u = input("Enter username: ")
p = input("Enter password: ")
if u == "admin" and p == "1234":
    print("Login successful")
else:
    print("Invalid credentials")

# Q10. Take a year as input. Check whether it is a leap year. A year is a leap year if:
# it is divisible by 400 OR it is divisible by 4 but NOT divisible by 100
# Print "Leap year" or "Not a leap year."   
y = int(input("Enter a year : "))
if y % 400 == 0:
    print("Leap year")
elif y % 4 == 0 and y % 100 != 0:
    print("Leap year")    
else:
    print("Not a leap year")