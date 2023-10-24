class Element:
    def __init__(self, state: int, position: int, states_distribution: list[float] = [0.5, 0.5]) -> None:
        """Class that represents an element of a system

        Args:
            state (int): State of the element
            position (int): Position of the element (currently unused)
            states_distribution (list[float], optional): Probability distribution of the states. Defaults to [0.5, 0.5].
        """
        self.state = state
        self.position = position
        self.states_distribution = states_distribution
    
    def __str__(self) -> str:
        return f"({self.position} {self.state})"
