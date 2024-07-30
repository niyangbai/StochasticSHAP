#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "engine.h"

namespace py = pybind11;

PYBIND11_MODULE(engine, m) {
    py::class_<SHAPEngine>(m, "SHAPEngine")
        .def("compute_shap_values", &SHAPEngine::compute_shap_values);

    py::class_<NaiveSHAP, SHAPEngine>(m, "NaiveSHAP")
        .def(py::init<>())
        .def("compute_shap_values", &NaiveSHAP::compute_shap_values);

    py::class_<StochasticSHAP, SHAPEngine>(m, "StochasticSHAP")
        .def(py::init<>())
        .def("compute_shap_values", &StochasticSHAP::compute_shap_values);

    py::class_<PCAStochasticSHAP, SHAPEngine>(m, "PCAStochasticSHAP")
        .def(py::init<>())
        .def("compute_shap_values", &PCAStochasticSHAP::compute_shap_values);

    py::class_<GroupedFeatureSHAP, SHAPEngine>(m, "GroupedFeatureSHAP")
        .def(py::init<>())
        .def("compute_shap_values", &GroupedFeatureSHAP::compute_shap_values);
}
