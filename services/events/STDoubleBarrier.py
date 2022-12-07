
from services.events.IEvents import IEvents

class STDoubleBarrier(IEvents):
    def __init__(self, data) -> None:
        self._U = data['U']
        self._D = data['D']
        
        if self._U <= self._D: raise f'U ({self._U}) precisa, necessariamente, ser maior que D ({self._D})'
        
    def test_event(self, s):
        return (s <= self._D) or (self._U <= s)
    
    