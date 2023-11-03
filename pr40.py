# Single Inheritance
class Parent:
def parent(self):
print("Parent class")
class Child(Parent):
def child(self):
print("Child class")
o = Child()
o.parent()
o.child()
Parent class
Child class
# Multiple Inheritance
class Parent1:
def parent1(self):
print("Parent-1 Class")
class Parent2:
def parent2(self):
print("Parent-2 class")
class Child(Parent , Parent2):
def child(self):
print("Child Class deriving Parent-1 & Parent-2")
o = Child()
o.parent1()
o.parent2()
o.child()
Parent Class
Parent-2 class
Child Class deriving Parent-1 & Parent-2
# Multilevel Inheritance
class Parent1:
def parent1(self):
print("Parent-1 Class")
class Parent2(Parent1):
def parent2(self):
print("Parent-2 class deriving Parent-1")
class Child(Parent2):
def child(self):
print("Child Class deriving Parent-1 & Parent-2")
o = Child()
o.parent1()
o.parent2()
o.child()
Parent-1 Class
Parent-2 class deriving Parent-1
Child Class deriving Parent-1 & Parent-2
# Hybrid Inheritance
class Parent:
def parent(self):
print("Parent class")
class Child1(Parent):
def child1(self):
print("Child1 class deriving Parent class")
class Child2(Parent):
def child2(self):
print("Child2 class deriving Parent class")
class GrandChild(Child1 , Child2):
def grandChild(self):
print("Grandchild class deriving Child1 & Child2 class")
o = GrandChild()
o.parent()
Parent class
Q41. Demonstrate Overriding and methods to overcome.
# parent class
class Parent:
# function breath
def breathe(self):
print("I breathe oxygen.")
# function feed
def feed(self):
print("I eat non - veg")
# child class
class child(Parent):
# function feed
def feed(self):
print("I eat veg.")
c = child()
c.feed()
# Some other method
c.breathe()
I eat veg.
I breathe oxygen.
