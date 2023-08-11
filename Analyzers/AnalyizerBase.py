from abc import ABC, abstractmethod
from typing import List


class AnalyzerBaseClass(ABC):
    def __init__(self):
        self.name = None
        self.certifying_question = None
        self.data = None
        self.text = None
    
    @abstractmethod
    def analyze(self) -> List:
        pass

    @abstractmethod
    def set_up_data(self):
        pass