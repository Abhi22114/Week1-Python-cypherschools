


  
#Lecture42- If statement

# syntax
# if conditon

age= input("Enter your age: ")
age=int(age)
if age>=14:
    print("line a")
    print("You are above")
  


#Lecture44-If-else statement
age= input("Enter your age: ")
age=int(age)
if age>=14:
    print("line a")
    print("You are above")
else:
    print("Sorry you can't play")
 
# Lecture46Nested If-else, Exercise 1 
# Exercise Solution
winning_number= 27
user_input= input("Guess any number b/w 1 & 100: ")
user_input= int(user_input)
if user_input==winning_number:
    print("YOU WIN!")
else:
    if user_input < winning_number:
        print("too low")
    else:
        print("too high")
 
