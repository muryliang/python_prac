def flatten(nest):
    try:
        for sublist in nest:
            for element in flatten(sublist):
                yield element
    except TypeError:
        print "in except"
        yield nest


def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new
