
class Assertion(object):
    def __init__(self):
        pass

    def type(self, arg, t):
        assert type(arg) is t, "Expected %r to have type %r, got %r" % (arg, t, type(arg))

    def nonempty(self, arg):
        assert len(arg) > 0, "Expected %r to have length > 0, got %d" % (arg, len(arg))

    def inlist(self, arg, l):
        assert arg in l, "Expected argument to be in the list %r, got %r" % (l, arg)

    def leq(self, lesser, greater):
        assert lesser <= greater, "Expected value (got %r) to be less than or equal to value (got %r)" % (lesser, greater)


