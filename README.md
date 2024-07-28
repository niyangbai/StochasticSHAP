<p align="center">
  <img src="logo.webp" alt="StochasticSHAP Logo" width="200"/>
</p>

# Enhancing KernelSHAP with Stochastic Dimensionality Reduction

## Overview
This repository contains the implementation of Stochastic KernelSHAP methods tailored for sparse data. The aim is to enhance the robustness and interpretability of SHAP explanations while improving computational efficiency. The methods include selecting non-zero features, applying PCA for dimensionality reduction, and grouping features.

## Getting Started

### Prerequisites
Ensure you have Python 3.9 or later installed on your system. You can install all dependencies via pip or conda:
```bash
pip install requirements.txt
```
```bash
conda env create -f environment.yml
```

### Installation
Clone this repository to your local machine using:
```bash
git clone https://github.com/niyangbai/StochasticSHAP.git
```

### Usage
Navigate to the cloned repository's directory and run the main script:
```bash
python main.py
```
Replace `main.py` with the script you wish to run.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments
- Thanks to the authors and contributors of the SHAP library.
- Appreciation for the open-source community providing tools and libraries that made this project possible.

## Contact
For any queries or further discussion, feel free to contact me - niyang.bai@fau.de
