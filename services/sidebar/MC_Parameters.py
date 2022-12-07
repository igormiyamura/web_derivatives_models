import streamlit as st

class MC_Parameters:
    def define_sidebar(self):
        st.sidebar.title("Monte Carlo Parameters")
        
        N = st.sidebar.slider('Timesteps', value=100, 
                      min_value=50, max_value=200)
        
        M = st.sidebar.slider('Number of Simulations', value=50000, 
                      min_value=10000, max_value=100000)
        
        return N, M
        