#Concept	What it does
#range()	Generates a sequence of numbers
#for	    Repeats for each item
#while	    Repeats while condition is true
#break	    Stops the entire loop
#continue	Skips current iteration

#Q1. Print numbers from 1 to 10 using a for loop.
for i in range(1,11,1):
    print(i)

#Q2. Print even numbers from 2 to 20 using range()
for i in range(2,21,2):
    print(i)

#Q3. Print numbers from 10 down to 1 using a for loop 
for i in range(10,0,-1):
    print(i)
    
#Q4. Take a number n and print numbers from 1 to n using a while loop
n = int(input("Enter a number : "))
i=1
while ( i <= n):
    print(i)
i += 1

#Q5. Take a number n and calculate the sum of numbers from 1 to n using a for loop.
n = int(input("Enter a number : "))
sum = 0
for i in range(1,n+1):
    sum += i

print(sum)

#Q6. Take a number n and print its multiplication table from 1 to 10.
n = int(input("Enter a number : "))
for i in range(1,11):
    print(i*n)

#Q7. Print numbers from 1 to 20, but skip multiples of 3 using continue.
for i in range(1,21):
    if i%3==0:
        continue
    print(i)

#Q8. Print numbers from 1 to 100, but stop completely when you reach 50 using break.
for i in range(1,100):
    if i==50:
        break
    print(i)

#Q9. Take numbers from the user repeatedly using a while loop. Stop when the user enters 0.
n = int(input("Enter a number: "))
while n != 0:
    n = int(input("Enter a number: "))

#Q10. Take a number n and count how many numbers from 1 to n are even.
n = int(input("Enter a number : ")) 
count = 0
for i in range(1,n+1):
    if i%2==0:
        count+=1
        
print(count)