import sqlite3
import sys

conn = sqlite3.connect("mdb.db")
curs = conn.cursor()

query = "SELECT * FROM food WHERE %s" % sys.argv[1]
print query
curs.execute(query)
print curs.description
names = [f[0] for f in curs.description]
for row in curs.fetchall():
	for pair in zip(names, row):
		print '%s: %s'%pair
	print

