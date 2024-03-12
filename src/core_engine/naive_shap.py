import shap
from abc_core import AbstractSHAP

class NaiveSHAP(AbstractSHAP):
    def __init__(self, model, model_type='tree', explainer_type='Kernel'):
        self.model = model
        self.model_type = model_type
        self.explainer = self._create_explainer(explainer_type)

    def _create_explainer(self, explainer_type):
        if explainer_type == 'Tree':
            return shap.TreeExplainer(self.model)
        elif explainer_type == 'Kernel':
            return shap.KernelExplainer(self.model.predict, data=shap.kmeans(self.data, k=5))
        elif explainer_type == 'Deep':
            return shap.DeepExplainer(self.model, self.data)
        elif explainer_type == 'Linear':
            return shap.LinearExplainer(self.model, self.data)
        else:
            raise ValueError("Unsupported explainer type")

    def compute_shap_values(self, X):
        return self.explainer.shap_values(X)

    def plot_summary(self, X):
        shap_values = self.compute_shap_values(X)
        shap.summary_plot(shap_values, X)