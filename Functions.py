"""
def table(num):
    for i in range(1,11):
        print(num,"*",i,"=",num*i)

n=int(input("Enter any number"))
table(n)

def compare(x,y):
    if x>y:
        print("{} is greater than {}".format(x,y))
    else:
        print("{} is greater than {}".format(y,x))
        
a=int(input("Enter first number:\t"))
b=int(input("Enter second number:\t"))

compare(a,b)

def Average(n1,n2,n3,n4):
    a=(n1+n2+n3+n4)/4
    print(a)

b=int(input("Enter first number:\t")) 
c=int(input("Enter second number:\t"))
d=int(input("Enter third number:\t"))
e=int(input("Enter first number:\t"))
Average(b,c,d,e)


def cube(num):
    return num**3

n1=int(input())
c=cube(n1)
print(c)

def abc():
    a="Chitkara"
    print("Hello",a)
abc()

def abc(a,b):
    print(b)
    return a+b

b=abc(30,20)
print(b)


def countvowels(str1):
    count=0
    vowels=['a','e','i','o','u']
    for s in str1:
        if s.lower() in vowels:
            count+=1
    return count
msg=input("enter any string")
c=countvowels(msg)
print("Total vowels in",msg,"are",c)

#Count the number of characters in a string

def count_characters(s):
    count = 0
    for _ in s:
        count += 1
    return count

# Example usage
my_string = "Hello, world!"
print("Total characters:", count_characters(my_string))
"""
#To count how many times a character is present in the string 

# class Parent():
#     def __init__(self):
#         self.value = "Chitkara University, Punjab"
#     def show(self):
#         print(self.value)

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.value = "Dept. of CSE, CUIET"
#     def show(self):
#         print(self.value)

# obj1 = Parent()
# obj2 = Child()

# obj1.show()
# obj2.show()

# class Parent:
#     def show(self):
#         print("Chitkara University")
# class Child(Parent):
#     def show(self):
#         print("Dept. of CSE, CUIET")

# child = Child()
# child.show() 

# class Parent1():
#     def show(self):
#         print("Chitkara University, Punjab")
#     def display(self):
#         print("Chitkara University, Rajpura")

# class Parent2():
#     def display(self):
#         print("Chitkara University, HP")
    

# class Child(Parent2, Parent1):
#     # def show(self):
#     #     print("Dept. of CSE, CUIET")
#     pass
    

# obj = Child()

# obj.show()
# obj.display()

class Parent():
    def display(self):
        print("Chitkara University, Rajpura")

class Child(Parent):
    def show(self):
        print("CUIET")
    

class Grandchild(Child):
    def show(self):
        print("Dept. of CSE, CUIET")
    
    

obj = Grandchild()

obj.show()
obj.display()
c = Child()
c.show()
c.display()

class Parent():
    def show(self):
        print("Chitkara University, Punjab")
class child(Parent):
    def show(self):
        Parent.show(self)
        print("Dept. of CSE, CUIET")

obj = Child()
obj.show()

class A:
    def __init__(self, a):
        self.a = A
    def __add__(self, o):
        return self.a + o.a
ob1=A(1)
ob2=A(2)
ob3=A("Chitkara")
ob4=A("University")

print(ob1 + ob2)
print(ob3 + ob4, "\n")

print(A.__add__(ob1, ob2))
print(A.__add__(ob3, ob4),"\n")

print(ob1.__add__(ob2))
print(ob3.__add__(ob4))


















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































