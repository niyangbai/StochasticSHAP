from abc import ABC, abstractmethod

class AbstractSHAP(ABC):
    @abstractmethod
    def explain(self):
        pass