import abc

class IMethods(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_option_value') and 
                callable(subclass.get_option_value) and 
                hasattr(subclass, 'get_se_value') and 
                callable(subclass.get_se_value) and 
                hasattr(subclass, 'register_value') and 
                callable(subclass.register_value))