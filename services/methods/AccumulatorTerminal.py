
import numpy as np
from services.methods.IMethods import IMethods

class AccumulatorTerminal(IMethods):
    def __init__(self, data) -> None:
        self.M = 0
        self.acc_values, self.acc_sqrt = 0, 0
        self._discount = np.exp(-data['r'] * data['T'])
        
    def get_option_value(self):
        return self._discount * self.acc_values / self.M
        
    def get_se_value(self):
        radix = self.acc_sqrt - self.acc_values * self.acc_values / self.M
        if radix < 0: raise f'Negative Radix: {radix}'
        
        return self._discount * np.sqrt(radix) / self.M
        
    def register_value(self, new_value):
        self.acc_values += new_value
        self.acc_sqrt += new_value * new_value
        self.M += 1
        