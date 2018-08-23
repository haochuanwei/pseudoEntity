import numpy as np
import random
import time
from datetime import date
from pprint import pformat
import pseudo.examples
from pseudo.generator import CustomGenerator
from pseudo.entity import Place

class RandomHotelGenerator(CustomGenerator):
    def __init__(self):
        super(RandomHotelGenerator, self).__init__()
        self.chineseTel_prov_codes = pseudo.examples.chineseTel_prov_codes
        self.names_1 = ['蓝天', '城市', '清雅', '假日', '豪泰', '华庭']
        self.names_2 = ['旅店', '快捷酒店', '宾馆', '大酒店', '客栈']
        self.addresses_1 = ['A', 'B', 'C', 'D', 'E', 'F']
        self.addresses_2 = range(1,1000)

    def name(self):
        self._check_seed()
        retstr = ''
        retstr += random.choice(self.names_1)
        retstr += random.choice(self.names_2)
        return retstr

    def prov(self):
        self._check_seed()
        return random.choice(list(self.chineseTel_prov_codes.keys()))

    def address(self, prov):
        self._check_seed()
        retstr = ''
        retstr += prov
        retstr += random.choice(self.addresses_1) 
        retstr += '区' 
        retstr += "%d" % random.choice(self.addresses_2) 
        retstr += '号' 
        return retstr

    def local_tel(self):
        self._check_seed()
        a = int(10**7)
        b = a * 10 - 1
        retstr = str(random.randint(a, b))
        return retstr

    def tel(self, prov):
        codes = self.chineseTel_prov_codes
        retstr = ''
        appstr = codes[prov]
        retstr += appstr
        retstr += '-'
        retstr += self.local_tel()
        return retstr

    def place(self):
        p = Place()
        p.info['name']       = self.name()
        p.info['province']   = self.prov()
        p.info['address']    = self.address(p.info['province'])
        p.info['tel']        = self.tel(p.info['province'])
        self._cache['prev']  = p
        return p
        
    hotel = place
