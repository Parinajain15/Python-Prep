#Q1 Create a function called greet() that prints "Hello, Python!" and call the function.
def greet():
    print("Hello, Python!")

greet()    

#Q2 Create a function called add(a, b) that takes two numbers and prints their sum. 
# Call it with 10 and 20.
def add(a,b):
    print(a+b)

add(10,20)

#Q3 Create a function called square(n) that takes a number and returns its square. 
# Call it with 5 and print the returned result.
def square(n):
    return n * n

print(square(5))

#Q4 Create a function called is_even(n) that takes a number and returns True if it is even,
# otherwise returns False. Call it with 8 and print the result.
def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

print(is_even(8))    

#Q5 Create a function called largest(a, b) that takes two numbers and returns 
# the larger number.  Call it with 15 and 10 and print the result.
def largest(a, b):
    return max(a,b)

print(largest(15,10))

#Q6 Create a function called count_vowels(text) that takes a string and returns 
# the number of vowels (a, e, i, o, u). Call it with "Python Programming" and print the result.
def count_vowels(text):
    count = 0

    for char in text:
        if char in "aeiou":
            count += 1

    return count

print(count_vowels("Python Programming"))

#Q7 Create a function called reverse_text(text) that takes a string and
#  returns the string reversed. Call it with "Python" and print the result.
def reverse_text(text):
    return text[::-1]

print(reverse_text("Python"))

#Q8 Create a function called factorial(n) that takes a number and returns its 
# factorial using a for loop. Call it with 5 and print the result.
def factorial(n):
    p = 1

    for i in range(n, 0, -1):
        p *= i

    return p

print(factorial(5))

#Q9 Create a function called count_digits(n) that takes an integer and returns the 
# number of digits in it. Call it with 12345 and print the result.
def count_digits(n):
    count = 0

    while n > 0:
        n = n // 10
        count += 1

    return count

print(count_digits(12345))

#Q10 Create a function called is_palindrome(text) that takes a string and returns 
# True if the string reads the same forwards and backwards, otherwise returns False.
#  Call it with "madam" and print the result.
def  is_palindrome(text):
     if text[::-1] == text:
         return True
     else:
         return False

print(is_palindrome("madam"))