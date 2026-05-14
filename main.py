#Booleans value
#print(10 > 9)
#print(10 == 9)
#print(10 < 9)


#a = 200
#b = 33

#if b > a:
    #print("b is greater than a")
#else:
    #print("b is not greater than a")



#Evaluate Values and Variables
#print(bool("Hello"))
#print(bool(15))

#x = "Hello"
#y = 15

#print(bool(x))
#print(bool(y))


#Most Values are True
#print(bool("abc"))
#print(bool(123))
#print(bool(["apple", "banana", "cherry"]))


#Some values are False
#print(bool(False))
#print(bool(None))
#print(bool(0))
#print(bool(""))
#print(bool(()))
#print(bool([]))
#print(bool({}))

#class myClass():
    #def __len__(self):
        #return 0

#myObj = myClass()
#print(bool(myObj))


#Function can Return a Boolean
#def myFunction():
    #return True

#print(myFunction())


#def myFunction():
    #return True

#if myFunction():
    #print("YES")
#else:
    #print("NO")


#x = 200
#print(isinstance(x, int))


#Exercise 1
print(10 > 5) # True
print(3 < 1) # False

#Exercise 2
is_student = True

print(is_student)

#Exercise 3
x = 15
y = 10

print(x > y)
print(x == y)

#Exercise 4
print(bool("Hello")) #True
print(bool("")) #False

#Exercise 5
print(bool(1)) #True
print(bool(0)) #False


#Exercise 6
age = 20

if age >= 18:
    print("You are adult")
else:
    print("You are teenager")

#Short solution:
print((age >= 18))


#Exercise 7
password = "python123"

if password == "python123":
    print(True)
else:
    print(False)

#Short solution
print(password == "python123")
#Exercise 8
x = 5
y = 10

if x < y and y > 3:
    print(True and True) #Don't need to write twice True
else:
    print(False and False) #Don't need to write twice False

#Bonus
print(bool("Python")) #True - because here we have a value
print(bool([])) #False - because is empty list
#Fixed syntax error


#Overall 5.80