import numpy as np
import time
from naive_shap import NaiveSHAP
from stochastic_shap import StochasticSHAP
from pca_stochastic_shap import PCAStochasticSHAP
from grouped_feature_shap import GroupedFeatureSHAP

def compare_efficiency(data: np.ndarray):
    algorithms = {
        "NaiveSHAP": NaiveSHAP(),
        "StochasticSHAP": StochasticSHAP(),
        "PCAStochasticSHAP": PCAStochasticSHAP(),
        "GroupedFeatureSHAP": GroupedFeatureSHAP()
    }

    results = {}
    for name, algo in algorithms.items():
        start_time = time.time()
        shap_values = algo.compute_shap_values(data)
        end_time = time.time()
        results[name] = end_time - start_time
        print(f"{name} took {results[name]:.4f} seconds")

    return results

if __name__ == "__main__":
    # Generate some sample data
    data = np.random.rand(100, 10)
    compare_efficiency(data)
