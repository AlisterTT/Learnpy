# -*- coding: utf-8 -*-
# this one is like your scripts with argv
def print_two(*args):  #定义一个函数，括号内为调用参数，必须用冒号结束本行
	arg1, arg2 = args  #将参数解包
	print "arg1: %r, arg2: %r" % (arg1, arg2)  #将解包后的每个参数都打印出来

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):  #跳过整个参数解包过程，直接用变量名
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
	print "I got nothin'."

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()