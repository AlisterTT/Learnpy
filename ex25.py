# -*- coding: utf-8 -*-

def break_words(stuff):
	"""This function will break up words for us.
	此功能作用是将句子中的单词单独列成表"""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words.
	将单词列表按顺序排列"""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it off.
	只打印第一个单词，类似readline"""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after popping it off.
	只打印最后一个单词"""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words.
	引用一开始的break_words来重新获得完整的单词列表"""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Print the first and last words of the sentence.
	打印单词列表第一个和最后一个单词"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one.
	打印顺序单词列表的第一个和最后一个单词"""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
