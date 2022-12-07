import abc

class IWiener(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'evolve_next_slice') and 
                callable(subclass.evolve_next_slice) and
                hasattr(subclass, 'reset') and 
                callable(subclass.reset))