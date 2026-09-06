n = float(input("Enter the first number : "))
m = float(input("Enter the second number : "))
o = input("Enter operator ( +, -, *, /, %, **) :  ")
if o == '+':
        print(n+m)
elif o == '-':
        print(n-m)
elif o == '*' :
        print(n*m)      
elif o == '/':
    if m == 0:
        print("Cannot divide by zero")
    else:
        print(n / m)
elif o == '%':
    if m == 0:
        print("Cannot divide by zero")
    else:
        print(n % m)      
elif o == '**':
        print(n**m)  
else:
        print("Invalid operator")