import numpy as np
import random
import time
import os
from datetime import date
from pprint import pformat
import pseudo.examples
from pseudo.generator import CustomGenerator
from pseudo.entity import Person

class RandomPersonGenerator(CustomGenerator):
    def __init__(self):
        super(RandomPersonGenerator, self).__init__()
        self.chineseID_prov_codes = pseudo.examples.chineseID_prov_codes
        self.chineseID_multipliers = np.array([7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2])
        self.chineseID_encodings = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        self.Female    = ['F', 'f', 'Female', 'female', '女']
        self.Male      = ['M', 'm', 'Male'  , 'male',   '男']
        self.Lastnames = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王']
        self.Firstnames_m1 = ['老', '大', '小']
        self.Firstnames_m2 = ['一', '二', '三', '四', '五', '六', '七']
        self.Firstnames_f1 = ['春', '夏', '秋', '冬']
        self.Firstnames_f2 = ['梅', '兰', '竹', '菊']

    def name(self, gender):
        self._check_seed()
        retstr = ''
        retstr += random.choice(self.Lastnames)
        self._A.inlist(gender, (self.Male + self.Female))
        if gender in self.Female:
            if self.coinflip():
                retstr += random.choice(self.Firstnames_f1)
            retstr += random.choice(self.Firstnames_f2)
        elif gender in self.Male:
            if self.coinflip():
                retstr += random.choice(self.Firstnames_m1)
            retstr += random.choice(self.Firstnames_m2)
        return retstr

    def dob(self):
        self._check_seed()
        t = random.randint(-300000000, 1100000000)
        d = date.fromtimestamp(t)
        return d

    def gender(self):
        self._check_seed()
        return random.choice(['女', '男'])

    def prov(self):
        self._check_seed()
        return random.choice(list(self.chineseID_prov_codes.keys()))

    def chineseID_last_digit(self, earlier_digits):
        c = np.array(list(map(int, list(earlier_digits))))
        last_index = int(np.dot(c, self.chineseID_multipliers)) % 11
        last_digit = self.chineseID_encodings[last_index]
        return last_digit

    def chineseID(self, d=None, prov=None):
        self._check_seed()
        retstr = ''

        codes = self.chineseID_prov_codes
        if prov is None:
            appstr = random.choice(list(codes.values()))
        else:
            self._A.inlist(prov, codes.keys())
            appstr = codes[prov]
        retstr += appstr
        appstr = "%02d" % random.randint(1,15)
        retstr += appstr
        appstr = "%02d" % random.randint(1,9)
        retstr += appstr

        if d is None:
            d = self.dob()
        self._A.type(d, date)
        yyyy = "%04d" % d.year
        mm = "%02d" % d.month
        dd = "%02d" % d.day
        appstr = yyyy + mm + dd
        retstr += appstr

        a = 0
        b = 10**3 - 1
        appstr = "%03d" % random.randint(a,b)
        retstr += appstr

        appstr = self.chineseID_last_digit(retstr)
        retstr += appstr

        return retstr

    def age_Gaussian(self, mu=35, sigma=6, floor=18, ceiling=70):
        self._check_seed()
        self._A.leq(floor, ceiling)
        retval = int(random.gauss(mu, sigma));
        if retval < floor:
            retval = floor
        if retval > ceiling:
            retval = ceiling
        return retval

    def age_from_dob(self, d):
        y = d.year
        c = date.fromtimestamp(time.time()).year
        self._A.leq(y, c)
        return c - y

    def person(self):
        p = Person()
        p.info['dob']       = self.dob()
        p.info['gender']    = self.gender()
        p.info['province']  = self.prov()
        p.info['name']      = self.name(p.info['gender'])
        p.info['chineseID'] = self.chineseID(p.info['dob'], p.info['province'])
        p.info['age']       = self.age_from_dob(p.info['dob'])
        self._cache['prev'] = p
        return p
        
