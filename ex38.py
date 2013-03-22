# -*- coding: utf-8 -*-
ten_things = "Apples Oranges Crows Telephones Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')	#把句子分割为单词列表
#列出一个备用单词列表
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:		#检查条件，当stuff的元素数不全为10的时候循环
	next_one = more_stuff.pop()		#输出more_stuff最后一项内容
	print "Adding: ", next_one
	stuff.append(next_one)			#在stuff里面添加刚才输出的内容
	print "There's %d items now." % len(stuff)		#统计stuff里面的单词数目

print "There we go: ", stuff      #输出stuff

print "Let's do some things with stuff."

print stuff[1]		#输出stuff第二个元素
print stuff[-1] # 输出stuff最后一个元素
print stuff.pop()	#默认输出stuff最后一个元素
print ' '.join(stuff) #打印stuff并在元素之间加上空格
print '#'.join(stuff[3:5]) #列表切片，打印第三个元素到第五个元素，等同于range(3,5)，中间加入井号