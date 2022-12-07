import abc

class IGenerator(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_next_final_s') and 
                callable(subclass.get_next_final_s) and 
                hasattr(subclass, 'next_S') and 
                callable(subclass.next_S) and 
                hasattr(subclass, 'reset') and 
                callable(subclass.reset))