
from services.option import OptionKO, OptionEuro, OptionKI
from services.payoff import PayoffCall, PayoffPut
from services.events import STDoubleBarrier
from services.process import GeneratorGBM
from services.methods import AccumulatorTerminal
from services.wiener import WienerPlain

class InputManager:
    def __init__(self, data) -> None:
        self._data = data
        
    def set_option(self, t_option):
        if t_option == 'o':
            return OptionKO.OptionKO(self._data)
        if t_option == 'i':
            return OptionKI.OptionKI(self._data)
        elif t_option == 'e':
            return OptionEuro.OptionEuro(self._data)
        else:
            raise 'Tipo de Opção não identificada.'
        
    def set_payoff(self, t_payoff):
        if t_payoff == 'c':
            return PayoffCall.PayoffCall(self._data)
        elif t_payoff == 'p':
            return PayoffPut.PayoffPut(self._data)
        elif t_payoff == 'b':
            raise 'Bond não implementado'
        else:
            raise 'Tipo de Payoff não identificado.'
    
    def set_event(self, t_event):
        if t_event == 'n':
            return None
        elif t_event == 'd':
            return STDoubleBarrier.STDoubleBarrier(self._data)
        else:
            raise 'Tipo de Evento não identificado.'
    
    def set_process(self, t_process):
        if t_process == 'g':
            return GeneratorGBM.GeneratorGBM(self._data)
        else:
            raise 'Tipo de Processo não identificado.'
        
    def set_method(self, t_method):
        if t_method == 't':
            return AccumulatorTerminal.AccumulatorTerminal(self._data)
        else:
            raise 'Tipo de Método não identificado.'
        
    def set_wiener(self, t_wiener):
        if t_wiener == 'wp':
            return WienerPlain.WienerPlain(self._data)
        else:
            raise 'Tipo de Wiener não identificado.'