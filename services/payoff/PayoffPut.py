
from services.payoff.IPayoff import IPayoff

class PayoffPut(IPayoff):
    def __init__(self, data) -> None:
        self._X = data['X']
    
    def payoff(self, S):
        return max(0, self._X - S)