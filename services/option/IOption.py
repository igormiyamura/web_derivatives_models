import abc

class IOption(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_option_value') and 
                callable(subclass.get_option_value) and 
                hasattr(subclass, 'get_se_value') and 
                callable(subclass.get_se_value) and 
                hasattr(subclass, 'get_done') and 
                callable(subclass.get_done) and
                hasattr(subclass, 'compute_values') and 
                callable(subclass.compute_values) and 
                hasattr(subclass, 'receive_next_slice') and 
                callable(subclass.receive_next_slice) and 
                hasattr(subclass, 'reset') and 
                callable(subclass.reset))