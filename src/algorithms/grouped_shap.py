import numpy as np
import engine

class GroupedFeatureSHAP:
    def __init__(self):
        self.engine = engine.GroupedFeatureSHAP()

    def compute_shap_values(self, data: np.ndarray) -> np.ndarray:
        return np.array(self.engine.compute_shap_values(data.tolist()))
