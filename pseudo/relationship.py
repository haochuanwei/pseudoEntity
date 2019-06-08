from pprint import pformat
import datetime

class CustomRelationship(object):
    def __init__(self):
        self.info     = {}
        self.involved = {}

    def describe(self):
        retstr = ''
        retstr += pformat(self.info)
        involved_dict = {k : self.involved[k].info for k in self.involved.keys()}
        retstr += '\n' + pformat(involved_dict)
        return retstr

class Event(CustomRelationship):
    def __init__(self):
        super(Event, self).__init__()
        dt = datetime.datetime.fromtimestamp(0.0)
        self.info['date'] = dt.date()
        self.info['time'] = dt.time()

class Lodging(Event):
    def __init__(self, person, hotel):
        super(Lodging, self).__init__()
        self.involved['person'] = person
        self.involved['hotel']  = hotel



