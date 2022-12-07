
from services.option.IOption import IOption

# Option Knock-out
class OptionKO(IOption):
    def __init__(self, data) -> None:
        self._pay = data['payoff']
        self._event = data['event']
        self._S0 = data['S0']
        
        self.reset()
        
    def __del__(self):
        del(self._pay)
        del(self._event)
        
    def get_option_value(self):
        return self._pay.payoff(self.St)
    
    def get_done(self):
        return self.done
    
    def register_value(self, s):
        self.St = s
        self.done = self._event.test_event(s)
        
        if self.done: self.option_value = 0
    
    def reset(self):
        self.St = self._S0
        self.option_value = 0
        self.done = False
        