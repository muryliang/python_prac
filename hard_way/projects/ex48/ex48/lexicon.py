
"""this is a word list"""
word_list = {'north': 'direction',
			 'south': 'direction',
			 'east' : 'direction',
			 'go'	: 'verb',
			 'kill' : 'verb',
			 'eat'  : 'verb',
			 'the'  : 'stop',
			 'in'   : 'stop',
			 'of'   : 'stop',
			 'bear' : 'noun',
			 'princess': 'noun',
			 '3'		: 'number',
			 '91234'  : 'number',
			 '1234'  : 'number',
			 'ASDFADFASDF': 'error',
			 'IAS'  : 'error'
			 }

def convert_number(s):
	""" convert string into number if possible, otherwise just return original string"""
	try:
		return int(s)
	except ValueError:
		return s

def scan(word):
	""" split list of words, search each one in the dict and get the type"""
#	ret_list = []
#	for unit in word.split():
#		ret_list.append((word_list.get(unit.lower(), None), convert_number(unit)))
#	return ret_list
	ret_list = [ (word_list.get(unit, None), convert_number(unit)) for unit in word.split()]
	print ret_list
	return ret_list
