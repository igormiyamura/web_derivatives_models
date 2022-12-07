import abc

class IEvents(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'test_event') and 
                callable(subclass.test_event))