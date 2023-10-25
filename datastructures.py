#list mutable,ordered

mylist=["EriC","Maria","Joan","Mercy","Gloria","Brian"]
mylist2=["2","78","56","89","3"]
mylist2.sort()
mylist.sort()
print(mylist)
print(f"My name is {mylist[0]}")
print("My name is" +mylist[0])
print(f"My sorted list {mylist2}")

#tuple imutable,ordered

my_tuple=("Kenya", "Uganda","Tanzania","Ethiopia","Somalia")
# my_tuple[2]="congo" - This will give an error 'object does not support ite assignmen' because you v=can never change value of items in a tuple unlike in lists
print(my_tuple)
print(f"My country is {my_tuple[0]}")
print(f"Our neighbouring countries are {my_tuple[1]} and {my_tuple[2]}")

#set unordered

fruits={"Oranges","Apples","Banana","Grapes"}
print(fruits)
# print(f"I love eating {fruits[0][1][2]} and {fruits [3]}") - testing whether it will obey the list

#dictionaries
employees={"Name":"Maria","Age":21,"Gender":"Female","Salary":"300,000"}
print("Employee's Name:%s"% employees["Name"])
print("Employee's Age:%d"% employees["Age"])


