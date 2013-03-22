# -*- coding: utf-8 -*-
class Song(object):

	def __init__(self, lyrics):		# __int__ 类的构造函数，用于初始化成员等
		self.lyrics = lyrics		# self 指代被访问的 object 或者 instance 的一个变量

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

# 把类实例化
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
# 实例化
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
