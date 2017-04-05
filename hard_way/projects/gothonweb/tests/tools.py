#!/usr/bin/python2
from nose.tools import *
import re

def assert_response(resp, contains=None, matches=None, headers=None, status="200"):
    assert status in resp.status, "Expected response %r not in %r" %(status, resp.status)

    if status == "200":
        assert resp.data, "Respond data is empty."

    if contains:
        assert contains in resp.data, "Respond does not contains %r" % contains

    if matches:
        reg = re.compile(matches)
        assert reg.matches(resp.data), "Respond does not match %r" % matches

    if headers:
        assert_equal(resp.headers, headers)


