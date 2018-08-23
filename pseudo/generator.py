import random
import time
from utils.assertion import Assertion

class CustomGenerator(object):
    def __init__(self):
        tic = int(time.time() * 1000)
        random.seed(a=tic)
        self._A = Assertion()
        self._maxdraws = 100
        self._draws = 0
        self._cache = {}

    def _check_seed(self):
        self._draws += 1
        if self._draws > self._maxdraws:
            tic = int(time.time() * 1000)
            random.seed(a=tic)
            self._draws = 0

    def coinflip(self, s=0.5):
        self._check_seed()
        p = random.uniform(0.0, 1.0)
        if p <= s:
            return True
        else:
            return False

