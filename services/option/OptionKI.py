
import numpy as np
from services.option.IOption import IOption

class OptionKI(IOption):
    def __init__(self, data) -> None:
        self._pay = data['payoff']
        self._event = data['event']
        
        self._T = data['T']
        self._S0 = data['S0']
        self._M = data['M']
        self._N = data['N']
        
        self._r = data['r']
        self._discount = np.exp(-data['r'] * data['T'])
        
        self.started = np.zeros(self._M)
        
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
    
    def update_started(self, s_values, t):
        for i in range(0, self._M):
            if not self.started[i]:
                self.started[i] = self._event.test_event(s_values[i])
    
    def receive_next_slice(self, s_values, i, t):
        if t + 1 == self._N:
            self._option_values = s_values.copy()
            self.update_started(s_values, t)
            self.compute_option_values(s_values)
            self.compute_values()
            
    def compute_option_values(self, s_values):
        for i in range(0, self._M):
            self._option_values[i] = self._pay.payoff(s_values[i])
            
        self.ready = True
            
    def compute_values(self):
        vl_sum, vl_sq = 0, 0
        
        if self.ready:
            for i in range(0, self._M):
                value = self._option_values[i] if self.started[i] else 0
                vl_sum += value
                vl_sq += value * value
                
            self._option_value = self._discount * vl_sum / self._M
            
            radix = vl_sq - vl_sum * vl_sum / self._M
            if radix < 0: raise f'Negative Radix: {radix}'
            
            self._se_value = self._discount * np.sqrt(radix) / self._M
            self.done = True
        
    def reset(self):
        self.done = False
        self.ready = True
        
        for i in range(0, self._M):
            self.started[i] = False