from urllib import urlopen
import re
p = re.compile('<meta name="(.*?)" content="(.*?)">')
text = urlopen("http://python.org/community/jobs").read()
for url, name in p.findall(text):
	print '%s %s' %(url, name)
