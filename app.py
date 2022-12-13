
import streamlit as st, numpy as np, pandas as pd, timeit
from datetime import datetime
import matplotlib.pyplot as plt

from services.sidebar import GBM_Parameters, Option_Parameters, MC_Parameters, Type_Parameters
from services.monte_carlo import MonteCarlo
from services.manager import InputManager

class App:
    def __init__(self):        
        # Streamlit
        
        
        self._GBM_Parameters = GBM_Parameters.GBM_Parameters()
        self._Option_Parameters = Option_Parameters.Option_Parameters()
        self._MC_Parameters = MC_Parameters.MC_Parameters()
        self._Type_Parameters = Type_Parameters.Type_Parameters()
        
        st.title('Implementing Models of Financial Derivatives')
        S0, r, sigma = self._GBM_Parameters.define_sidebar()
        X, T, U, D = self._Option_Parameters.define_sidebar()
        N, M, MC_RUNS = self._MC_Parameters.define_sidebar()
        
        payoff, event, option = self._Type_Parameters.option_types()
        process = self._Type_Parameters.process_types()
        method = self._Type_Parameters.method_types()
        wiener = self._Type_Parameters.wiener_types()
        
        self.data = self.define_data(S0, r, sigma, X, T, U, D, M, N, MC_RUNS, payoff, event, option, process, method, wiener)
        
        self._IM = InputManager.InputManager(self.data)
        self.data = self.define_objetos()
        
    def plot_simulations(self, simulations, n_lines=100):
        for i in range(0, n_lines):
            plt.plot(simulations[i])
            
        plt.title(f'Caminhos do ativo com [{self.data["N"]}] steps')
        st.pyplot(plt)
        
    def define_data(self, S0, r, sigma, X, T, U, D, M, N, MC_RUNS, payoff, event, option, process, method, wiener):
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
            'MC_RUNS': MC_RUNS,
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
    # print(data)
    
    run = st.button('Rodar Simulação')
    
    if run:
        my_bar = st.progress(0)
        
        df_mc = pd.DataFrame()
        for i in range(0, data['MC_RUNS']):
            start = timeit.default_timer()
            
            mc = MonteCarlo.MonteCarlo(data)
            v, se, simulations = mc.run()
            
            stop = timeit.default_timer()
            res = [i+1, v, se, stop - start]

            df = pd.DataFrame([res], columns=['Run #', 'Price', 'Standard Error', 'Time'])
            df_mc = pd.concat([df_mc, df])
            del(mc)
            
            my_bar.progress(i/(data['MC_RUNS']-1)) # Progress Bar
            
        col1, col2, col3 = st.columns(3)
        col1.metric('Option Value', np.round(df_mc['Price'].mean(), 4))
        col2.metric('Standard Error', np.round(df_mc['Standard Error'].mean(), 4))
        col3.metric('Time', np.round(df_mc['Time'].sum(), 4))
        
        st.dataframe(df_mc)
        
        # Montar gráfico do Payoff
        with st.expander('View graph'):
            app.plot_simulations(simulations, n_lines=100)
        
    
    
    