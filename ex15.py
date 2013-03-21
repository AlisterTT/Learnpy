# -*- coding: utf-8 -*-
from sys import argv  #引入模组

script, filename = argv  #定义读取文件的名称

txt = open(filename)  #用open命令获得filename文件

print "Here's your file %r:" % filename  #显示文件名
print txt.read()  #对之前open获得的文件进行read操作

print "Type the filename again:"
file_again = raw_input(">")  #再次获取文件名

txt_again = open(file_again)  #获得的文件定义到txt_again上面

print txt_again.read()  #对txt_again进行read操作