from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

class BuildExt(build_ext):
    def build_extensions(self):
        ct = self.compiler.compiler_type
        opts = ['-O2']
        if ct == 'msvc':
            opts.append('/EHsc')
        else:
            opts.append('-std=c++11')
        for ext in self.extensions:
            ext.extra_compile_args = opts
        build_ext.build_extensions(self)

setup(
    name='SparseSHAP',
    version='0.1.0',
    author='Niyang Bai',
    author_email='niyang.bai@fau.de',
    description='A Python package for efficient SHAP value computation in sparse datasets',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/your-python-package',
    packages=['src', 'src.core', 'src.python_interface', 'src.plotting', 'src.simulation', 'src.tests'],
    ext_modules=[Extension('src.core.shap_engine', ['src/core/shap_engine.cpp'])],
    cmdclass={'build_ext': BuildExt},
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'pytest',
        'pybind11'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: C++',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
