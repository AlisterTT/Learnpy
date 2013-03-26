# -*- coding: utf-8 -*-
from sys import exit

def gold_room():
	print "这个屋子里有很多金币，你是要拿多少个呢?"

	next = raw_input("> ")
	#if "0" in next or "1" in next:
	if next.isdigit():			#第二种检查数字输入的方案，能检查0-9
		how_much = int(next)
	else:
		dead("你特么不会输入整数呀.")
	if how_much < 50:
		print "不错，小伙子不贪心，你赢了!"
		exit(0)
	else:
		dead("你太贪了，被金币砸死了!")

def bear_room():
	print "另一间屋子里有一只熊瞎子."
	print "熊瞎子抱着一罐蜂蜜."
	print "熊瞎子坐在那里挡住出口了."
	print "你怎么让熊瞎子移开呀?"
	print "1.拿走蜂蜜 / 2.嘲讽熊瞎子"
	bear_moved = False

	while True:
		next = raw_input("> ")

		if next == "1":
			dead("熊瞎子把你的脸皮扯下来了.")
		elif next == "2" and not bear_moved:
			print "熊瞎子从门旁边移开了. 你现在可以过去了."
			print "2.继续嘲讽 / 3.赶紧过去"
			bear_moved = True
		elif next == "2" and bear_moved:
			dead("撒完尿的熊瞎子回来碰见了你，扯掉了你的腿.")
		elif next == "3" and bear_moved:
			gold_room()
		else:
			print "你特么说什么呢."

def cthulhu_room():
	print "屋子里蹲着一个变态的幻术师."
	print "他一直盯着你，看的你快精神失常了."
	print "你是赶紧跑掉还是吃掉自己的头呢?"
	print "1.赶紧跑 / 2.吃掉自己的头"

	next = raw_input("> ")

	if "1" in next:
		start()
	elif "2" in next:
		dead("哇塞，真特么好吃!")
	else:
		cthulhu_room()

def dead(why):
	print why, "你死了!"
	print "1.重新开始 / 2.退出"
	
	res = raw_input("> ")

	if res == "1":
		start()
	elif res =="2":
		exit(0)
	else:
		dead("选择1或者2好么!!")

def start():
	print "你现在在一间暗室里."
	print "你的左右有两扇门."
	print "选哪一边呢?"
	print "1.左边 / 2.右边"

	next = raw_input("> ")

	if next == "1":
		bear_room()
	elif next == "2":
		cthulhu_room()
	else:
		dead("你他妈就在这里瞎转吧，饿死你.")


start()