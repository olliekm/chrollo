from base_sampler import BaseSampler
from api.utils.grid_search_sampler import GridSearchSampler
from api.utils.baysian_optimization_sampler import BayesianOptimizationSampler

def get_sampler(sampler_name: str) -> BaseSampler:
    """
    Factory function to get the appropriate sampler instance based on the sampler name.
    """
    name = sampler_name.lower()
    if name in ("grid", "grid_search"):
        return GridSearchSampler()
    elif name in ("bayesian", "bayesian_optimization", "bayes_opt"):
        return BayesianOptimizationSampler()
    else:
        raise ValueError(f"Unknown sampler name: {sampler_name}")
