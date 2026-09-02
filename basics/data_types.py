#Python is dynamically typed
#You dont have to tell Python the type
# Python Data Types are 2 - Primitive and Collection

# Q1. Create one variable of each:
# int, float, str, bool
# Print their values and their types.
number = 24
price = 33.33
name = "Parina"
isstudent = True #true false always capital T/F compulsory
print(type(number), type(price), type(name), type(isstudent))

# Q2. Identify the data type of each variable using type().
a = 25
b = 25.5
c = "25"
d = False
print(type(a), type(b), type(c), type(d))

# Q3. Create:
# a list containing 3 numbers
# a tuple containing 3 numbers
# a set containing 3 unique numbers
# a dictionary containing your name and age
# Print their types.
l = [1,2,3,]
t = ( 6,7,8)
s = {10,20,30}
d = {"name": "parina", "age": 21}
print(type(l), type(t), type(s), type(d))

# Q4. Predict the output before running the code.
x = 10
y = "10"
print(type(x))
print(type(y))
print(x == y)
#int,str,false

# Q5. Convert the following values into the required data types.
# Then print their values and types.
# "25" → int
# "25.5" → float
# 100 → str
# 1 → bool
a = int("25")
b = float("25.5")
c = str(100)
d = bool(1)
print(a,type(a),b,type(b),c,type(c),d,type(d))

# Q6. Fix the following code so that it prints 30.
age = "25"
years = 5
print(int(age) + years)

# Q7. Predict the output and explain why.
a = 10
b = 10.0
print(a == b)
print(type(a))
print(type(b))
#True as Python considers these numerically equal even though their types are different. , int, float

# Q8. What is the difference between:
# x = 10
# x = "10"
# Explain what changes and why.
#first is int second is str because " " data type changes because of diff syntax 
