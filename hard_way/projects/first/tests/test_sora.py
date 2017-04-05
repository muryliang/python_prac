# -*- coding: utf-8 -*-

from nose.tools import *
import sora

def setup():
	print "SETUP!"

def teardown():
	print "TEAR DOWN!"

def test_basic():
	print "I RAN!"

setup()
teardown()
test_basic()
