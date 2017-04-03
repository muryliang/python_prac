import fileinput, re

fieldpattern = r'\[(.+?)\]'

pattern = re.compile(fieldpattern)

scope = {}
def replacement(match):
	group = match.group(1)
	try:
		return str(eval(group, scope))
	except SyntaxError:
		exec group in scope
		return ""

lines = ''
for line in fileinput.input():
	lines +=  line.replace('\n','') 

print pattern.sub(replacement, lines),

