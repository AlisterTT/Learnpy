# -*- coding: utf-8 -*-
## Animal is a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Make a class named Dog that is-a Animal.
class Dog(Animal):

	def __init__(self, name):
		## From self get the name attribution and set it to name.
		self.name = name

## Make a class named Cat that is-a Animal.
class Cat(Animal):

	def __init__(self, name):
		## From self get the name attribution and set it to name.
		self.name = name

## Class Person has-a __init__ thattakes self and name parameters.
class Person(object):

	def __init__(self, name):
		## From self get the name attribution and set it to name.
		self.name = name

		## Person has a pet of some kind.
		self.pet = None

## Make a class named Employee that is-a Person.
class Employee(Person):

	def __init__(self, name, salary):
		## 找到父类Person，调用里面的 __init__(name)函数
		super(Employee, self).__init__(name)
		## From self get the salary attribution and set it to name.
		self.salary = salary

## Fish is an object.
class Fish(object):
	pass

## Make a class named Salmon that is-a Fish.
class Salmon(Fish):
	pass

## Make a class named Halibut that is-a Fish.
class Halibut(Fish):
	pass

## rover is a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## From mary get the pet attribute and set it to satan.
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## Set flipper to an instance of class Fish.
flipper = Fish()

## Set crouse to an instance of class Salmon.
crouse = Salmon()

## Set harry to an instance of class Halibut.
harry = Halibut()