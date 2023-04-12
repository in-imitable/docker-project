#Creating an empty list
myList=[]

#Ask from user the range of numbers 
num = int(input("How many number do you want to store? "))

#Add all number to the list using for loop
for i in range(0, num):
    n = int(input("Enter: "))
    myList.append(n)

#Print all number add in list
print("Your all itmes here:")
print(myList)

total1=0
# Define a for loop to sum all items in list
for item in range(0, len(myList)):
    total1 = total1 + myList[item]
#print all total value
print("Sum of all itmes in list: ", total1)

#creating an empty list to store even items
evenList=[]
total2=0

#Creating a for loop to find even number
for item in myList:
    #Check even number
    if item % 2 == 0:
        print(item, end=" ")
        evenList.append(item)

# Define a for loop to sum all even items in list
for item in range(0, len(evenList)):
    total2 = total2 + evenList[item]
#print all total value
print("\nSum of all even itmes in list: ", total2)




    
