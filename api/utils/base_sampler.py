from abc import ABC, abstractmethod

class BaseSampler(ABC):
    @abstractmethod
    def sample(self, search_space: dict, past_trials: list) -> dict:
        """Generate a new set of hyperparameters to try."""
        pass    

