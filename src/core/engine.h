#ifndef SHAP_ENGINE_H
#define SHAP_ENGINE_H

#include <vector>

class SHAPEngine {
public:
    virtual ~SHAPEngine() = default;

    // Pure virtual function to be implemented by derived classes
    virtual std::vector<double> compute_shap_values(const std::vector<std::vector<double>>& data) = 0;
};

class NaiveSHAP : public SHAPEngine {
public:
    std::vector<double> compute_shap_values(const std::vector<std::vector<double>>& data) override;
};

class StochasticSHAP : public SHAPEngine {
public:
    std::vector<double> compute_shap_values(const std::vector<std::vector<double>>& data) override;
};

class PCAStochasticSHAP : public SHAPEngine {
public:
    std::vector<double> compute_shap_values(const std::vector<std::vector<double>>& data) override;
};

class GroupedFeatureSHAP : public SHAPEngine {
public:
    std::vector<double> compute_shap_values(const std::vector<std::vector<double>>& data) override;
};

#endif // SHAP_ENGINE_H
