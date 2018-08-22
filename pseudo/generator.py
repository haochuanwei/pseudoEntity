import random
import time

class CustomGenerator(object):
    def __init__(self):
        tic = int(time.time() * 1000)
        random.seed(a=tic)
        self.maxdraws = 100
        self.draws = 0
        self._custom_init()

    def _custom_init(self):
        pass

    def check_seed(self):
        self.draws += 1
        if self.draws > self.maxdraws:
            tic = int(time.time() * 1000)
            random.seed(a=tic)
            self.draws = 0

    def coinflip(self, s=2):
        self.check_seed()
        p = random.randint(0, 9999)
        if p % s == 0:
            return True
        else:
            return False

