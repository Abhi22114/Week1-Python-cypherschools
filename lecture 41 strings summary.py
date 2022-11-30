
#strings

name= "abhijeet"
# string indexing
print(name[1])
#string slicing
print(name[-1:0:-1])
#take user input
#name=input()
#take two user inputs
uname,age=input().split(",")
print(uname)
print(age)
#len function
print(len(name))
# lower, upper, title method
print(uname.lower())
print(uname.upper())
print(uname.title())
# find, replace, center method
print(uname.center(len(name)+8,"*"))
print(name.find(uname))
# strings are immutable
