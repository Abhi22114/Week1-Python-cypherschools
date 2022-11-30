#Lecture33 - String Methods Part1
# string methods part one
name="AbHijEEt KuMaR"

# 1 len() function
length = len(name)
print(length)

# 2 lower() method
print(name.lower())

# 3 upper() method
print(name.upper())

#4 title() method
print(name.title())

#5 count() method
print(name.count("a"))
  
#Lecture34 - Chapter 2 in Exercise 3
name, char= input("Enter comma seprated name and character :  ").split(",")
print(f"length of your name is {len(name)}")
print(f"character count: {name.lower().count(char.lower())}")
  
