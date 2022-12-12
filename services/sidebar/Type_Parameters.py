import streamlit as st

class Type_Parameters:
    def format_func(box_dict, key):
        return box_dict[key]
    
    def option_types(self):
        st.write("### Tipo da Opção:")
        opt_col1, opt_col2, opt_col3 = st.columns(3)
        
        DICT_PAYOFF = {
            'Call': 'c',
            'Put': 'p',
            'Bond': 'b'
        }
        payoff = opt_col1.selectbox('Tipo de Payoff', options=list(DICT_PAYOFF.keys()))

        DICT_EVENTS = {
            'No Event': 'n',
            'Double Barrier': 'd'
        }
        event = opt_col2.selectbox('Tipo de Evento', options=list(DICT_EVENTS.keys()))
        
        DICT_OPTIONS = {
            'Average': 'a',
            'European': 'e',
            'Knock-Out': 'o',
            'Knock-In': 'i'
        }
        option = opt_col3.selectbox('Tipo da Opção', options=list(DICT_OPTIONS.keys()))

        return DICT_PAYOFF[payoff], DICT_EVENTS[event], DICT_OPTIONS[option]
    
    def process_types(self):
        st.write("### Tipo de Processo:")
        
        DICT_PROCESS = {
            'GBM': 'g'
        }
        process = st.selectbox('Tipo de Processo', options=list(DICT_PROCESS.keys()))
        return DICT_PROCESS[process]
        
    def method_types(self):
        st.write("### Tipo de Método:")
        
        DICT_METHODS = {
            'Accumulate': 't'
        }
        method = st.selectbox('Tipo de Método', options=list(DICT_METHODS.keys()))
        return DICT_METHODS[method]
    
    def wiener_types(self):
        st.write("### Tipo de Wiener Process:")
        
        DICT_WIENER = {
            'Wiener Plain': 'wp'
        }
        wiener = st.selectbox('Tipo de Wiener', options=list(DICT_WIENER.keys()))
        return DICT_WIENER[wiener]