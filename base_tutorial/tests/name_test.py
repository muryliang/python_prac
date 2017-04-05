import bin.name as nm
from nose.tools import *

def aa_test_aa():
    book = {}
    nm.init(book)
    nm.store(book, "bian ming liang")
    assert_equals(nm.lookup(book, "first", "bian"), ["bian ming liang"])
    assert_equals(nm.lookup(book, "middle", ""), None)


