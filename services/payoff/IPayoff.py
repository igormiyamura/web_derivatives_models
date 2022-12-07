import abc

class IPayoff(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'payoff') and 
                callable(subclass.payoff))