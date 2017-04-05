from nose.tools import *
#from ex48.parser import parser_sentence, Sentence, ParserError
from ex48.parser import Sentence

def add(a, b):
	return a+b

def sentence_test():
#	result = parser_sentence([('noun','me'), ('verb', 'play'), ('noun', 'football')])
	slist = [('noun','me'), ('verb', 'play'), ('noun', 'football')]
	result = Sentence(slist)
	assert_equal(result.subject, 'me')
	assert_equal(result.verb, 'play')
	assert_equal(result.obj, 'football')
#	res2 = Sentence(['my','name','bian'])
#	assert_raises(ParserError, Sentence, [('noun','me')])
#	with assert_raises(TypeError) as cm:
#		parser_sentence([('noun','me')])
#		add(0,'2')
#	ex = cm.exception
#	print 'ex is hahahhahah',type(ex)
#	print 'ex code is', ex.code
