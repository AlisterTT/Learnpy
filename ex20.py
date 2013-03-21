# -*- coding: utf-8 -*-

from sys import argv

script, input_file = argv

def print_all(f):   #定义一个函数，函数的参数名为f
	print f.read()  #对获得的文件f进行读取操作并显示出来

def rewind(f):
	f.seek(0)    #由于之前读完，得将指针返回第0个字符

def print_a_line(line_count, f):
	print line_count, f.readline()   #readline每运行一次读一行

current_file = open(input_file)  #将一开始载入的文件打开

print "First let's print the whole file:\n"

print_all(current_file)   #用函数操作打开的文件

print "Now let's rewind, kind of like a tape."

rewind(current_file)   #之前已经对文件进行了读取，返回指针重新读取

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1   # x+=y 同等于 x=x+y
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
