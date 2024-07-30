from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        "shap_engine",
        ["src/core/engine.cpp", "src/algorithms/shap_wrapper.cpp"],
    ),
]

setup(
    name="SparseSHAP",
    version="0.1.0",
    author="Niyang Bai",
    author_email="niyang.bai@fau.de",
    description="A Python package for efficient SHAP value computation in sparse datasets",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/niyangbai/SparseSHAP',
    packages=["src.algorithms", "src.plotting", "src.simulation", "src.tests"],
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    install_requires=[
        "numpy",
        "matplotlib",
        "pybind11",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: C++",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
