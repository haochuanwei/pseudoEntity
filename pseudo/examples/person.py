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
        self.ChineseID_prov_codes = pseudo.examples.ChineseID_prov_codes
        self.ChineseID_multipliers = np.array([7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2])
        self.ChineseID_encodings = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        self.Female    = ['F', 'f', 'Female', 'female', '女']
        self.Male      = ['M', 'm', 'Male'  , 'male',   '男']
        self.Lastnames = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王']
        self.Firstnames_m1 = ['老', '大', '小']
        self.Firstnames_m2 = ['一', '二', '三', '四', '五', '六', '七']
        self.Firstnames_f1 = ['春', '夏', '秋', '冬']
        self.Firstnames_f2 = ['梅', '兰', '竹', '菊']

    def Name(self, gender):
        self.check_seed()
        retstr = ''
        retstr += random.choice(self.Lastnames)
        assert gender in (self.Female + self.Male), "Expected gender to be 女/男, got %r" % gender
        if gender in self.Female:
            if self.coinflip(2):
                retstr += random.choice(self.Firstnames_f1)
            retstr += random.choice(self.Firstnames_f2)
        elif gender in self.Male:
            if self.coinflip(3):
                retstr += random.choice(self.Firstnames_m1)
            retstr += random.choice(self.Firstnames_m2)
        return retstr

    def DOB(self):
        self.check_seed()
        t = random.randint(-300000000, 1100000000)
        d = date.fromtimestamp(t)
        return d

    def Gender(self):
        self.check_seed()
        return random.choice(['女', '男'])

    def Prov(self):
        self.check_seed()
        return random.choice(list(self.ChineseID_prov_codes.keys()))

    def ChineseID_last_digit(self, earlier_digits):
        c = np.array(list(map(int, list(earlier_digits))))
        last_index = int(np.dot(c, self.ChineseID_multipliers)) % 11
        last_digit = self.ChineseID_encodings[last_index]
        return last_digit

    def ChineseID(self, d=None, prov=None):
        self.check_seed()
        retstr = ''

        codes = self.ChineseID_prov_codes
        if prov is None:
            appstr = random.choice(list(codes.values()))
        else:
            assert prov in codes.keys(), "Invalid province %r" % prov
            appstr = codes[prov]
        retstr += appstr
        appstr = "%02d" % random.randint(1,15)
        retstr += appstr
        appstr = "%02d" % random.randint(1,9)
        retstr += appstr

        if d is None:
            d = self.DOB()
        assert type(d) is date, "Expected a datetime.date object, got %r" % type(d)
        yyyy = "%04d" % d.year
        mm = "%02d" % d.month
        dd = "%02d" % d.day
        appstr = yyyy + mm + dd
        retstr += appstr

        a = 0
        b = 10**3 - 1
        appstr = "%03d" % random.randint(a,b)
        retstr += appstr

        appstr = self.ChineseID_last_digit(retstr)
        retstr += appstr

        return retstr

    def Age_Gaussian(self, mu=35, sigma=6, floor=18, ceiling=70):
        self.check_seed()
        assert floor <= ceiling, "Ceiling value (got %d) must be greater than or equal to floor value (got %d)" % (ceiling, floor)
        retval = int(random.gauss(mu, sigma));
        if retval < floor:
            retval = floor
        if retval > ceiling:
            retval = ceiling
        return retval

    def Age_from_DOB(self, d):
        y = d.year
        c = date.fromtimestamp(time.time()).year
        assert y <= c, "Year of birth (got %d) must be less than or equal to the year right now (which is %d)" %(y, c)
        return c - y

    def Person(self):
        p = Person()
        p.info['dob']       = self.DOB()
        p.info['gender']    = self.Gender()
        p.info['province']  = self.Prov()
        p.info['name']      = self.Name(p.info['gender'])
        p.info['chineseID'] = self.ChineseID(p.info['dob'], p.info['province'])
        p.info['age']       = self.Age_from_DOB(p.info['dob'])
        return p
        
