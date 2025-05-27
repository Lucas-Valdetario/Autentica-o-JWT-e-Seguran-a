from abc import ABC, abstractmethod
from typing import Dict

class ViewInterface(ABC):
    """Interface para as Views"""
    
    @abstractmethod
    def handle(self, http_request: Dict) -> Dict:
        """Método abstrato para manipulação de requisições"""
        raise NotImplementedError("Deve implementar o método handle")