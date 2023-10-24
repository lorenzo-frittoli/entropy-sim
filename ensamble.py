import random
from math import log2, prod
from itertools import product

from element import Element


class Ensamble:
    def __init__(self, length: int) -> None:
        """Ensable class that represents a system of Element objects.

        Args:
            length (int): _description_
        """
        self.elements = [Element(random.randint(0, 1), i, [0.2, 0.8]) for i in range(length)]
        
    def __str__(self) -> str:
        return ", ".join([str(e) for e in self.elements])
    
    def calculate_entropy(self) -> float:
        """Calculates the entropy of the system based on its elements' variables

        Returns:
            float: entropy of the system
        """
        probabilities = [prod(c) for c in product(*[e.states_distribution for e in self.elements])]
        return -sum([p * log2(p) for p in probabilities])
    