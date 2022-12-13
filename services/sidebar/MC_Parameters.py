import streamlit as st

class MC_Parameters:
    def define_sidebar(self):
        st.sidebar.title("Monte Carlo Parameters")
        
        N = st.sidebar.slider('Timesteps', value=100, 
                      min_value=50, max_value=500)
        
        M = st.sidebar.slider('Number of Simulations', value=50000, 
                      min_value=10000, max_value=100000)
        
        mc_runs = st.sidebar.slider('Number of Simulations', value=5, 
                      min_value=1, max_value=10)
        
        return N, M, mc_runs
        