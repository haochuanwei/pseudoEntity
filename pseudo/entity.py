from pprint import pformat

class CustomEntity(object):
    def __init__(self):
        self.info = {}
        self._custom_init()

    def _custom_init(self):
        pass

    def bio(self):
        return pformat(self.info)

class Person(CustomEntity):
    def _custom_init(self):
        self.info['name']    = "John Doe"
        self.info['gender']  = "Male"
        self.info['age']     = 30

class Place(CustomEntity):
    def _custom_init(self):
        self.info['name']    = "Hudson's"
        self.info['address'] = "221B Baker Street"



