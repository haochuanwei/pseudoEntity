from pprint import pformat

class CustomEntity(object):
    def __init__(self):
        self.info = {}

    def bio(self):
        return pformat(self.info)

class Person(CustomEntity):
    def __init__(self):
        super(Person, self).__init__()
        self.info['name']    = "John Doe"
        self.info['gender']  = "Male"
        self.info['age']     = 30

class Place(CustomEntity):
    def __init__(self):
        super(Place, self).__init__()
        self.info['name']    = "Hudson's"
        self.info['address'] = "221B Baker Street"



