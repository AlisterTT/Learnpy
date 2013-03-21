# -*- coding: utf-8 -*- 
from sys import argv
from os.path import exists

script, from_file, to_file = argv  #提取两个文件

print "Copying from %s to %s" % (from_file, to_file)

# We could do these two on one line too, how?
in_file = open(from_file)  #获得需要读取的文件
indata = in_file.read()  #对文件进行读取操作，获得数据

print "The input file is %d bytes long" % len(indata)  #显示获得数据的字节数

print "Does the output file exist? %r" % exists(to_file) 
#exists命令将文件名字符串作为参数，如果文件存在返回True，不存在则返回False
print "Ready, hit RETURN to continue, CTRL-C to abort. "
raw_input() #这里相当于一个中断

out_file = open(to_file, 'w') #获得文件，访问方式为写入模式
out_file.write(indata) #对文件进行写入操作

print "Alright, all done."

out_file.close()
in_file.close()  #关闭读取的东西