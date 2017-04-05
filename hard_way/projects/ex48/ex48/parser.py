class ParserError(Exception):
	pass

class Sentence(object):
	def __init__(self, slist):
		#remember we take ('noun', 'princess') tuples and convert them
		self.subject = self.parse_subject(slist)[1]
		self.verb = self.parse_verb(slist)[1]
		self.obj = self.parse_object(slist)[1]

	def peek(self, word_list):
#		print 'wordlist is', word_list
		if word_list:
			word = word_list[0]
			return word[0]
		else:
			return None

	def match(self, word_list, expecting):
		if word_list:
			word = word_list.pop(0)

			if word[0] == expecting:
				return word
			else :
				return None

		else:
			return None

	def skip(self,  word_list, word_type):
		while self.peek(word_list) == word_type:
			self.match(word_list, word_type)

	def parse_verb(self, word_list):
		self.skip(word_list, 'stop')

		if (self.peek(word_list) == 'verb'):
			return self.match(word_list, 'verb')
		else:
			raise ParserError("Excepted a verb next.")

	def parse_object(self, word_list):
		self.skip(word_list, 'stop')

		if (self.peek(word_list) == 'noun'):
			return self.match(word_list, 'noun')
		elif (self.peek(word_list) == 'direction'):
			return self.match(word_list, 'direction')
		else:
			raise ParserError("Excepted a noun or direction.")

	def parse_subject(self, word_list):
		self.skip(word_list, 'stop')

		if (self.peek(word_list) == 'noun'):
			return self.match(word_list, 'noun')
		elif (self.peek(word_list) == 'verb'):
			return ('noun', 'player')
		else:
			raise ParserError('Excepted a subject next')

	def parser_sentence(self, word_list):
		subj = self.parse_subject(word_list)
		verb = self.parse_verb(word_list)
		obj = self.parse_object(word_list)

		return Sentence(subj, verb, obj)
