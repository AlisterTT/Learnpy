# -*- coding: utf-8 -*-
#定义一个函数
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

#调用函数并赋值
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#先定义两个变量，再调用函数的时候分别用这两个变量给参数赋值
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#把式子的结果赋予参数
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#调用前面的变量
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)