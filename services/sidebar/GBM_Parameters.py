import streamlit as st

class GBM_Parameters:
    def define_sidebar(self):
        st.sidebar.title("GBM Parameters")
        
        S0 = st.sidebar.slider('Stock Price (S0)', value=100, 
                      min_value=50, max_value=150)

        r = st.sidebar.slider('Inter-period Interest Rate (r)', value=0.05, 
                      min_value=0.0, max_value=0.1, step=0.01)

        sigma = st.sidebar.slider('Volatility', value=0.2, 
                      min_value=0.0, max_value=0.4, step=0.01)
        
        return S0, r, sigma