import streamlit as st

class Option_Parameters:
    def define_sidebar(self):
        st.sidebar.title("Option Parameters")
        
        X = st.sidebar.slider('Exercise Price (X)', value=100, 
                      min_value=50, max_value=150)

        T = st.sidebar.slider('Time Periods (T)', value=1, 
                      min_value=0, max_value=5)
        
        U = st.sidebar.slider('U', value=120, 
                      min_value=50, max_value=150)

        D = st.sidebar.slider('D', value=90, 
                      min_value=50, max_value=150)

        return X, T, U, D