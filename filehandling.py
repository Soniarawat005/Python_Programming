#create file for saying my laptop password
# open function will create the file
# when file is not exist and write the file 

mypassword=open("password.txt","w")

#write my laptop password in file 
mypassword.write("my macbook password-luluu")

#overwrite the new password using userinput
mypassword.write(input("enter new password"))

#read the password from file
mypassword=open("password.txt","r")
mydata= mypassword.read()
if"pawan"in mydata:
    print("yes")
else:
    print("no")
    