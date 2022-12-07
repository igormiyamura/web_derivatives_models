
from services.evolver.IEvolver import IEvolver

# Evolves with an underlying Wiener Process
class EvolverW(IEvolver):
    def __init__(self, data) -> None:
        super().__init__()
        self._und = data['process']
        self._wie = data['wiener']
        
        self._und.reset()
        self._wie.reset()
        
    def evolve_next_slice(self, slice, i, t):
        self._wie.evolve_next_slice(slice, i, t)
        self._und.evolve_next_slice(slice, i, t)