import matplotlib.pyplot as plt

class SHAPPlot:
    @staticmethod
    def plot_shap_values(shap_values, feature_names):
        # TODO: Implement the SHAP values plotting
        plt.figure()
        plt.bar(feature_names, shap_values)
        plt.xlabel("Features")
        plt.ylabel("SHAP Values")
        plt.title("SHAP Values for Features")
        plt.show()
