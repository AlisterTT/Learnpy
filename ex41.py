# -*- coding: utf-8 -*-
class TheThing(object):		#后面加object是规定

	def __init__(self):
		self.number = 0

	def some_function(self):
		print "I got called."

	def add_me_up(self, more):
		self.number += more
		return self.number

# two different things，用TheThing类定义 a 和 b，里面分别是 self = a 和 self = b
a = TheThing()
b = TheThing()

a.some_function()	# 这一句实际上是 some_function(a)
b.some_function()

print a.add_me_up(20)	# 运行 add_me_up函数，其中 more = 20
print b.add_me_up(30)

print a.number		
print b.number

# Study this. This is how you pass a variable
# from one class to another. You will need this.
class TheMultiplier(object):

	def __init__(self, base):
		self.base = base

	def do_it(self, m):
		return m * self.base

x = TheMultiplier(a.number)		# 这里面 self = x, base = a.number
print x.do_it(b.number)		# 这里面 m = b.number