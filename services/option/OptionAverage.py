
import numpy as np
from services.option.IOption import IOption

class OptionAverage(IOption):
    def __init__(self, data) -> None:
        self._pay = data['payoff']
        
        self._T = data['T']
        self._S0 = data['S0']
        self._M = data['M']
        self._N = data['N']
        
        self._r = data['r']
        self._discount = np.exp(-data['r'] * data['T'])
        self._acc_values = np.zeros((1, self._M))
        
        self.reset()
        
    def __del__(self):
        del(self._pay)
        
    def get_option_value(self):
        if not self.done: self.compute_values()
        return self._option_value
    
    def get_se_value(self):
        if not self.done: self.compute_values()
        return self._se_value
    
    def get_done(self):
        return False
    
    def evolve_next_slice(self, s_values, i, t):
        for j in range(0, self._M):
            self._acc_values[j] += s_values[j]
            
    def compute_values(self):
        vl_sum, vl_sq = 0, 0
        
        for i in range(0, self._M):
            value = self._pay.payoff(self._acc_values[i] / (1 + self._N))
            vl_sum += value
            vl_sq += value * value
            
        self._option_value = self._discount * vl_sum / self._M
        
        radix = vl_sq - vl_sum * vl_sum / self._M
        if radix < 0: raise f'Negative Radix: {radix}'
        
        self._se_value = self._discount * np.sqrt(radix) / self._M
        self.done = True
        
    def reset(self):
        self.done = False
        for i in range(0, self._M):
            self._acc_values[i] = self._S0
            