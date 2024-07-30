import numpy as np
import engine

class StochasticSHAP:
    def __init__(self):
        self.engine = engine.StochasticSHAP()

    def compute_shap_values(self, data: np.ndarray) -> np.ndarray:
        return np.array(self.engine.compute_shap_values(data.tolist()))
