from urllib import urlopen,urlretrieve
import re

fname, headers = urlretrieve('http://www.python.org')
with open(fname) as f:
	string =  f.read()

m = re.compile('<a href="([^"]+)" .*?>about</a>', re.IGNORECASE)
match = m.search(string)
print match.group(1)
print match.group(0)
