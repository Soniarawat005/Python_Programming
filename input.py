# #list can store multiple data, data can be different types int str 
# #list can store the duplicate data 
# #list is an ordered data set-sorting ascending descending

# #create list and store your friends name 
# friendlist = ["isha","nikhil","yash","naman","sonia"]
# print(friendlist)
# #add the age of your friends into list 
# #append will add the data into end of the list 
# friendlist.append(36)
# friendlist.append(26)
# friendlist.append(29)
# friendlist.append(5)

# print(friendlist)

# #add the data into list using index number 
# friendlist.insert(0,"isha")
# print(friendlist)


# #to access the data usind index no 
# print(friendlist[2]) 

# #to delete the data from list 
# friendlist.remove("yash")
# print(friendlist)

# #pop will delete the data using index 
# friendlist.pop(3)  

#access the complete list 
#for name in friendlist 
#   print(name)
friendlist.sort()
#add the 5 favt city name in list
#add my favt city kasol in index 0
# remove the llast city in list-using pop
# #sorting the list data
# #print the list data 


# list- it can store multiple data with different datatype ordered,changeable,duplicate
#tuple- it is unchangeable 
#set- unordered,unchangeable,no duplicate
#dictionary- 
# 



#list in python
#list stores multiple data
myList = ["pawan","ivan","deepanshu"]
#tuple stores multiple data 
mytuple = ("pawan","ivan","deepanshu")
#set store multiple data 
myset = {"pawan","ivan","deepanshu"}
#dictionary stores multiple data 
mydict = {"name":"pawan", "email":"p@gamil.com"}

#to check the data type of all above data set 
print("list:", type(myList), "tuple:",type(mytuple))
print("set:"), type(myset), "dict:",type(mydict)

#access data from data set 
print("list:", myList[0])
print("tuple:", mytuple[0],"dict:", mydict["name"])

#access complete data from the data set 
for data in myList:
    print("list",data)
for item in myset:
    print("set",item)
for value in mytuple:
    print("tuple",value)
for x in mydict.values():
    print("dict",x)

#tuple and set is unchangeable dict and list is changeable
#list, tuple duplicate item 
#set, dict no duplicate item 

#to update the data in all data set 
myList[0]= "tripti"
print(myList)
myset[0]= "tripti"
print(myset) 
mytuple[0]= "tripti"
print(mytuple)
mydict["name"]= "tripti"
print(mydict)

#add new value in data set 
myList.append("sonia")
myset.add("sonia")
mydict.update({"name":"sonia"})
print("list",myList,"tuple",mytuple,"dict",mydict,
       "set",myset)


#to remove the data from data set 
mydict.pop("name")
myList.pop(0)
myset.remove("pawan")
print("list",myList,"tuple",mytuple,"dict",mydict,
      "set",myset)

#Covert tuple to list
convertlist = list(mytuple)
print(type(convertlist))

convertlist.append("rohan")




    
    
