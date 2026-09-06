#Q1 — List. Take 5 numbers from the user and store them in a list. Then print the list.
n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))
n3 = int(input("Enter number 3 : "))
n4 = int(input("Enter number 4 : "))
n5 = int(input("Enter number 5 : "))
l = [ n1, n2, n3, n4, n5 ]
print(l)

#Q2 — List. Given [10, 20, 30, 40, 50], change 30 to 100 and print the list.
g = [10, 20, 30, 40, 50]
g[2]=100
print(g)

#Q3 — List. Given [10, 20, 30], take a number from the user, append it to the list, print the list.
g = [10, 20, 30]
u = int(input("Enter a number : "))
g.append(u)
print(g)

#Q4 — List. Given [10, 20, 30, 40, 50], remove 30 and print the list.
g = [10, 20, 30, 40, 50]
g.remove(30)
print(g)

#Q5 — Tuple. Create a tuple containing 5 numbers, print the tuple, its length, its first element.
t = (1,2,3,4,5)
print(t)
print(len(t))
print(t[0])

#Q6 — Set. Take 5 numbers from the user, store them in a set, print the set.
# The set should automatically remove duplicates.
u1 = int(input("Enter the first number : "))
u2 = int(input("Enter the second number : "))
u3 = int(input("Enter the third number : "))
u4 = int(input("Enter the fourth number : "))
u5 = int(input("Enter the fifth number : "))
s = {u1, u2, u3, u4, u5}
print(s)

#Q7 — Set. Given {10, 20, 30}, add 40 and remove 20.
g = {10, 20, 30}
g.add(40)
g.remove(20)

#Q8 — Dictionary. Create a dictionary containing name,age,marks. Print each value using its key.
d = { "name" : "parina", "age" : 21, "marks" : 100 }
print(d["name"], d["age"], d["marks"])

#Q9 — Dictionary. Given {"name": "Alex", "age": 20, "marks": 85}
# change the age to 21 and add "city": "Delhi".
g = {"name": "Alex", "age": 20, "marks": 85}
g["age"] = 21
g["city"] = "Delhi"
print(g)

#Q10 — Mixed. Given [10, 20, 20, 30, 30, 40],convert it into a set to remove duplicates,print the result.
g = [10, 20, 20, 30, 30, 40]
s = set(g)
print(s)