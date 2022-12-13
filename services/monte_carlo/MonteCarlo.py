
import numpy as np, streamlit as st

from datetime import datetime
from services.evolver import EvolverW

class MonteCarlo:
    def __init__(self, data) -> None:
        
        # Parametros
        self.S0, self.r, self.sigma = data['S0'], data['r'], data['sigma'] # GBM
        self.X, self.T, self.U, self.D = data['X'], data['T'], data['U'], data['D'] # Option
        self.M, self.N = data['M'], data['N'] # Monte Carlo
        
        self.OBJ_Payoff, self.OBJ_Event, self.OBJ_Option = data['payoff'], data['event'], data['option']
        self.OBJ_Process = data['process']
        self.OBJ_Method = data['method']
        
        # Objetos
        self.OBJ_EVOL = EvolverW.EvolverW(data)
        
        # Slice Variables
        self._slice_time = 0
        self._slice = np.zeros(self.M)
        
        # Output Variables
        self.option_value = 0
        self.se_value = 0
        
    def __del__(self):
        print(f'[{datetime.now()}][MonteCarlo] > Deletando objetos...')
        del(self._slice_time)
        del(self._slice)
        del(self.option_value)
        del(self.se_value)
        
        del(self.OBJ_Payoff)
        del(self.OBJ_Event)
        del(self.OBJ_Option)
        del(self.OBJ_Process)
        del(self.OBJ_Method)
        del(self.OBJ_EVOL)
        
    def run(self):
        simulation_values = {}
        for i in range(0, self.M):
            simulation_values[i] = [] # Plot price timesteps
        
        for i in range(0, self.N):
            self.OBJ_EVOL.evolve_next_slice(self._slice, i, i)
            self.OBJ_Option.receive_next_slice(self._slice, i, i)
            
            count_simulation = 0
            for v in self._slice:
                simulation_values[count_simulation].append(v)
                count_simulation += 1
            
        self.register()
        value = self.option_value
        standard_error = self.se_value
        
        return value, standard_error, simulation_values
        
    def register(self):
        self.option_value = self.OBJ_Option.get_option_value()
        self.se_value = self.OBJ_Option.get_se_value()
       