<p align="center">
  <img src="logo.webp" alt="StochasticSHAP Logo" width="200"/>
</p>

# Enhancing KernelSHAP with Stochastic Dimensionality Reduction

## Overview
This repository presents a novel approach aimed at enhancing the interpretability of machine learning models, especially in high-dimensional datasets. By integrating stochastic dimensionality reduction techniques with KernelSHAP, we aim to provide clearer and more reliable explanations of model predictions. Our methodology focuses on super-pixel segmentation and SHAP value averaging, addressing computational challenges and improving the interpretability of complex AI systems.

## Features
- **Stochastic Dimensionality Reduction:** Innovative technique to manage high-dimensional data, making KernelSHAP computations more feasible and efficient.
- **Super-pixel Segmentation:** Utilizes super-pixels to reduce complexity while retaining essential information for interpretation.
- **SHAP Value Averaging:** Enhances the robustness of SHAP explanations by averaging results over multiple stochastic iterations.

## Project Structure

The structure of this repository is organized as follows to ensure easy navigation and comprehension:

- `/data`: Directory for datasets used in the project. Includes raw data, processed data, and any intermediate datasets created during the analysis.
- `/notebooks`: Jupyter notebooks for exploratory data analysis, model development, and testing are stored here.
- `/reference`: Includes reference materials such as papers, articles, and any other documents that support the understanding of the project.
- `/results`: Output results such as models, figures, logs, and performance metrics are saved in this folder.
- `/scripts`: Contains reusable and standalone scripts used for various tasks like data preprocessing, model training, and result analysis.
- `/src`: Source code of the project. 
- `/thesis`: Draft, expose and final thesis can be found here.
- `.gitignore`: Specifies intentionally untracked files to ignore.
- `environment.yml`: YAML file for reproducing the conda environment.
- `LICENSE`: The MIT License file for the project.
- `README.md`: Markdown file with an overview of the project, instructions for installation, usage, and other important information.
- `requirements.txt`: Lists all the Python dependencies necessary to run the project.


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
For any queries or further discussion, feel free to contact me - bainiyang@gmail.com.
