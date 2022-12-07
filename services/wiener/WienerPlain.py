
import numpy as np
from services.wiener.IWiener import IWiener

class WienerPlain(IWiener):
    def __init__(self, data) -> None:
        super().__init__()
        self._N = data['N']
        self._M = data['M']
        self._T = data['T']        
        
        self.dt = data['T'] / data['N']
        self.rt_dt = np.sqrt(self.dt)
        
        self.w_slice = np.zeros(self._M)
        self.n_slice = np.zeros(self._M)
        
        self.reset()
        
    def reset(self):
        for j in range(0, self._M):
            self.w_slice[j] = 0
            self.n_slice[j] = 0
            
        self._last_i = -1
        
    def evolve_next_slice(self, slice, i, t):
        if i != self._last_i + 1: raise 'WienerPlain não sequencial.'
        
        self.n_slice = np.random.normal(0, 1, size=(self._M,))
        for j in range(0, self._M):
            slice[j] = self.w_slice[j] + self.rt_dt * self.n_slice[j]
            self.w_slice[j] = slice[j]
            
        t = i * self.dt
        self._last_i = i