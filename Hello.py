#name = input("What is your name: ")
#age = int(input("How old are you: "))
#print("\n" + "Thanks",(name.title()),"for using my program")

#days = age * 365
#minutes = age * 525948
#seconds = age * 31556926
#print("\n" + name.title(), "you have been alive for",days,"days,",minutes,"minutes,",seconds,"seconds.")

#items = ['Book', 'Apple', 'Dog', 'Camel']
    
#if ('Book' and 'Banana' in items):
    #print("items present".upper())
#else:
    #print("items not present".upper())
    
#if ('Sandwich' or 'Dog' in items):
    #print("one/both items are present".upper())
#else:
    #print("one/both items are not presnt". upper())
    
#for items in items: 
    #print("\n" + "i love my " + items)


#ListNum = [2, -1, 0, -4, 3, 4, 10, 100, 1200, 14]
#print(ListNum)
#print("The Minimum number in the List is:", min(ListNum))
#print("The Maximum number in the List is:", max(ListNum))
#print("The Sum of all the numbers are:", sum(ListNum))

#making a sliced list
#NewList = ListNum[0:5]
#print("\n" + "New List ==>", NewList)

#using for loops w slice list
#for ListNum in ListNum[5:10]:
    #print("\n" + "New List ==>", ListNum)

#copying list using slicing list
#items = ["Book", "Apple", "Dog", "Camel"]
#cpy_items = items[:]
#cpy_items.append("Tulip")
#print("\n" + "New List ==>", cpy_items)

#using tuples, they are like list, the values can't be changed but overwritten, and it uses a () not []
#tup = (2020, 500)

#Dictionaries
#car = {"Toyota": "Camry", "Cylinder": "V6"}
#print("Car Model:", car["Toyota"])
#print("Engine Type:", car["Cylinder"])
#car["Color"] = "Green"
#print(car)
#del car["Cylinder"]
#print("After Deletion:", car)

#while loops
#i = 2
#while(i <= 7):
    #print(i, "Time(s)")
    #i += 1

#i = ''
#name = "Write a name: "
#while(i != 'q'):
    #i = input(name)

#using break and continue
#i = 1
#user = ""

#while(i <= 5):
    #user = input("Enter a name: ") #case sensitive
    
    #if(user == "jesse"):
        #break
    #elif(user == "soph"):
        #continue
    #elif(user == "cody"):
        #print("Hello Cody")
    #else:
        #print("you entered:", user)
    #i += 1
    
#using functions
#def fullname(fname, lname): #fname & lname are parameters
    #print("Your name is:", lname, fname)
    
#firstname = input("Firstname: ")
#lastname = input("Lastname: ")

#fullname(firstname, lastname) #firstname & lastname are arguments


#classes
#class Person():
    #def insert(self, name, age, idNum):
        #self.name = name
        #self.age = age
        #self.idNum = idNum
    
    #def output(self):
        #print("Your name is", self.name, "Your age is", self.age, "Your ID is", self.idNum)
        
#outside the class
#j = Person()
#j.insert('John', '33', '1234567890')
#j.output()

class Person():
    def __init__(self, name, age, idNum):
        self.name = name
        self.age = age
        self.idNum = idNum
        
    def output(self):
        print("Your name is", self.name, "Your age is", self.age, "Your ID is", self.idNum)

#we use the constructor inside here
john = Person('John', '33', '1234567890')

#accessing class object's variable or function
#print(john.name)
#print(john.age)
#print(john.idNum)
#print(john.output())

#making multiple instances of a class
m = Person('Melissa', '55', '0987654321')

#class inheritance simply means creating a class child of a parent class
class Man():
    def strong(self):
        print("Men are strong!")

class Child(Person, Man):
    pass

kid = Child('Johnny', '5', '123')
kid.output()

kid.strong()