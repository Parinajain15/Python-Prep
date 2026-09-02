# Q1. Create a string containing your full name. Print the string and its length.
name = "Parina Jain"
print(name, len(name))

# Q2. Given:text = "Python Programming"
# Print:
# a) First character
# b) Last character
# c) First 6 characters
# d) Reverse of the string
text = "Python Programming"
print(text[0])
print(text[-1])
print(text[0:6])
print(text[::-1])

# Q3. Check whether the following are present in text: "Python" , "Java" 
# Print the results using 'in'.
text = "Python Programming"
print("Python" in text)
print("Java" in text)

# Q4. Find the index of:
# a) "P"
# b) "o"
# c) "Java"
# Print the results.
# Remember: find() returns -1 if the value is not found.
text = "Python Programming"
print(text.find('P'))
print(text.find('o'))
print(text.find("Java"))

# Q5. Replace "Python" with "Java" in text = "I am learning Python". Print the new string.
# Also print the original string afterwards.
# Observe whether replace() changes the original string.\
text = "I am learning Python"
new_text = text.replace("Python","Java")
print(new_text)
print(text)

# Q6. Given text = "Python Is Fun". Print: a) Everything in uppercase b) Everything in lowercase
text = "Python Is Fun"
print(text.upper())
print(text.lower())

# Q7. Predict the output before running:
text = "Hello World"
print("hello" in text)
print("Hello" in text)
print(text.find("o"))
print(text.find("z"))
#false,true,4,-1

# Q8.Take a sentence as input. Print:
# a) Its length
# b) The sentence in uppercase
# c) The sentence in lowercase
# d) Whether the word "Python" is present
name = input("what are u learning : ")
print(len(name))
print(name.upper())
print(name.lower())
print("Python" in name)

# Q9. Take a string as input and print it in reverse. Example: Input: Python  Output: nohtyP
name = input("Enter a string : ") 
print(name[::-1])