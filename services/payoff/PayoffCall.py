
from services.payoff.IPayoff import IPayoff

class PayoffCall(IPayoff):
    def __init__(self, data) -> None:
        self._X = data['X']
    
    def payoff(self, S):
        return max(0, S - self._X)