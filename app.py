
import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt

from services.sidebar import GBM_Parameters, Option_Parameters, MC_Parameters, Type_Parameters
from services.monte_carlo import MonteCarlo
from services.manager import InputManager

class App:
    def __init__(self):
        self._GBM_Parameters = GBM_Parameters.GBM_Parameters()
        self._Option_Parameters = Option_Parameters.Option_Parameters()
        self._MC_Parameters = MC_Parameters.MC_Parameters()
        self._Type_Parameters = Type_Parameters.Type_Parameters()
        
        st.title('Implementing Models of Financial Derivatives')
        S0, r, sigma = self._GBM_Parameters.define_sidebar()
        X, T, U, D = self._Option_Parameters.define_sidebar()
        N, M = self._MC_Parameters.define_sidebar()
        
        payoff, event, option = self._Type_Parameters.option_types()
        process = self._Type_Parameters.process_types()
        method = self._Type_Parameters.method_types()
        wiener = self._Type_Parameters.wiener_types()
        
        self.data = self.define_data(S0, r, sigma, X, T, U, D, M, N, payoff, event, option, process, method, wiener)
        
        self._IM = InputManager.InputManager(self.data)
        self.data = self.define_objetos()
        
    def plot_simulations(self, simulations, n_lines=100):
        for i in range(0, n_lines):
            plt.plot(simulations[i])
            
        st.pyplot(plt)
        
    def define_data(self, S0, r, sigma, X, T, U, D, M, N, payoff, event, option, process, method, wiener):
        return {
            'S0': S0, 
            'r': r, 
            'sigma': sigma, 
            'X': X, 
            'T': T, 
            'U': U,
            'D': D,
            'M': M, 
            'N': N,
            'payoff': payoff,
            'event': event,
            'option': option,
            'process': process,
            'method': method,
            'wiener': wiener
        }
        
    def define_objetos(self):
        self.data['payoff'] = self._IM.set_payoff(t_payoff=self.data['payoff'])
        self.data['event'] = self._IM.set_event(t_event=self.data['event'])
        self.data['option'] = self._IM.set_option(t_option=self.data['option'])
        self.data['process'] = self._IM.set_process(t_process=self.data['process'])
        self.data['method'] = self._IM.set_method(t_method=self.data['method'])
        self.data['wiener'] = self._IM.set_wiener(t_wiener=self.data['wiener'])
        
        return self.data

if __name__ == "__main__":
    app = App()
    data = app.data
    print(data)
    
    run = st.button('Rodar Simulação')
    
    if run:
        print(data)
        mc = MonteCarlo.MonteCarlo(data)
        v, se, simulations = mc.run()
        
        app.plot_simulations(simulations, n_lines=100)  
        st.write(f'Option Value: {v}')
        st.write(f'Standard Error: {se}')
    
    
    