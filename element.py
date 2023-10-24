class Element:
    def __init__(self, state: int, position: int, states_distribution: list[float] = [0.5, 0.5]) -> None:
        self.state = state
        self.position = position
        self.states_distribution = states_distribution
    
    def __str__(self) -> str:
        return f"({self.position} {self.state})"
