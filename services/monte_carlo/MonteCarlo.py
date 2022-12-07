
import numpy as np, streamlit as st
from services.evolver import EvolverW

class MonteCarlo:
    def __init__(self, data) -> None:
        # Streamlit
        self.my_bar = st.progress(0)
        
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
        self._slice_time = self.T
        self._slice = np.zeros(self.M)
        
        # Output Variables
        self.option_value = 0
        self.se_value = 0
        
        
    def run(self):
        simulation_values = {}
        
        for i in range(0, self.N):
            simulation_values[i] = [] # Plot price timesteps
            
            self.OBJ_EVOL.evolve_next_slice(self._slice, i, self._slice_time)
            self.OBJ_Option.evolve_next_slice(self._slice, i, self._slice_time)
            
            self.my_bar.progress(i/self.N) # Progress Bar
            
        value = self.option_value
        standard_error = self.se_value
        
        return value, standard_error, simulation_values
        
    def register(self):
        self.option_value = self.OBJ_Option.get_option_value()
        self.se_value = self.OBJ_Option.get_se_value()
       