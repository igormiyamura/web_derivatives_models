
import numpy as np
from services.process.IGenerator import IGenerator

class GeneratorGBM(IGenerator):
    def __init__(self, data) -> None:
        self._M = data['M']
        self._N = data['N']
        self._S0 = data['S0']
        self._sigma = data['sigma']
        
        # Path Parameters
        self.dt = data['T'] / data['N']
        self.drift = (data['r'] - 0.5 * data['sigma'] * data['sigma']) * self.dt
        self.s_root_t = data['sigma'] * np.sqrt(self.dt)
        
    # def get_next_final_s(self):
    #     self.St = self.next_S(self.St)
    #     return self.St
            
    # def next_S(self, S):
    #     return S * np.exp(self.drift + self.s_root_t * np.random.normal(0, 1))
    
    def evolve_next_slice(self, slice, i, t):
        drift_t = self.drift * t
        for j in range(0, self._M):
            slice[j] = self._S0 * np.exp(drift_t + self._sigma * slice[j])
            
        return slice
            
    
    def reset(self):
        self.St = self._S0