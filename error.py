#error 
print[x]

#error handling
try:
    print[x]
except NameError:
    print("'x' is not defined")

#error 2 
#y=1/0
try:
    y=1/0
except ZeroDivisionError:
    print("divide by zero error")   

#error 3
name="pawan"
#no=int(name)
try:
    no=int(name)
except ValueError:
    print("string can not convert into interger")

#error 4
friends=["sonia","isha","nikhil"]
#friends[4] 
try:
    friends[4]
except IndexError:
    print("your calling wrong index")


 #error 5
amount=500
email="p@gamil.com"
#total=amount+email
try:
    total=amount+email
except TypeError:
    print("this error is datatype error")

