# -*- coding: utf-8 -*-
def scan(str):
	direction = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
	verb = ['go', 'stop', 'kill', 'eat']
	stop = ['the', 'in', 'of', 'from', 'at', 'it']
	noun = ['door', 'bear', 'princess', 'cabinet']
	glossary = [direction, verb, stop, noun]
	names = ['direction', 'verb', 'stop', 'noun']

	index = {}	# index的形式为字典
	for x in glossary:		# x是词的类型，glossary的类型是列表
		for y in x:		# y即是所给的词语，y类型为列表
			index.update({y : names[glossary.index(x)]})	# 找出x在glossary中的位置,对应names相同位置的元素

	output = []	# output形式为列表
	words = str.split()		# 把str的句子分离成单词
	for name in words:
		key = index.get(name)
		if name.isdigit():		# 当name为数字的时候
			output.append(('number', int(name)))	# name必须为整数

		elif key != None:
			output.append((index.get(name), name))	# 获得name的value

		else:
			output.append(('error', name))

	return output