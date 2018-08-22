import numpy as np
import random
import time
from datetime import date
from pprint import pformat
import pseudo.examples
from pseudo.generator import CustomGenerator
from pseudo.entity import Place

class RandomHotelGenerator(CustomGenerator):
    def _custom_init(self):
        self.ChineseTel_prov_codes = pseudo.examples.ChineseTel_prov_codes
        self.Names_1 = ['蓝天', '城市', '清雅', '假日', '豪泰', '华庭']
        self.Names_2 = ['旅店', '快捷酒店', '宾馆', '大酒店', '客栈']
        self.Addresses_1 = ['A', 'B', 'C', 'D', 'E', 'F']
        self.Addresses_2 = range(1,1000)

    def Name(self):
        self.check_seed()
        retstr = ''
        retstr += random.choice(self.Names_1)
        retstr += random.choice(self.Names_2)
        return retstr

    def Prov(self):
        self.check_seed()
        return random.choice(list(self.ChineseTel_prov_codes.keys()))

    def Address(self, prov):
        self.check_seed()
        retstr = ''
        retstr += prov
        retstr += random.choice(self.Addresses_1) 
        retstr += '区' 
        retstr += "%d" % random.choice(self.Addresses_2) 
        retstr += '号' 
        return retstr

    def LocalTel(self):
        self.check_seed()
        a = int(10**7)
        b = a * 10 - 1
        retstr = str(random.randint(a, b))
        return retstr

    def Tel(self, prov):
        codes = self.ChineseTel_prov_codes
        retstr = ''
        appstr = codes[prov]
        retstr += appstr
        retstr += '-'
        retstr += self.LocalTel()
        return retstr

    def Hotel(self):
        p = Place()
        p.info['name']       = self.Name()
        p.info['province']   = self.Prov()
        p.info['address']    = self.Address(p.info['province'])
        p.info['Tel']        = self.Tel(p.info['province'])
        return p
        
