from setuptools import setup, find_packages
import pathlib

# Read the README file for long description
this_directory = pathlib.Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="pandas-outliers",
    version="1.0.1",
    author="Kiran Hamza",
    author_email="",
    description="A simple library that adds .outliers() method to pandas DataFrame for easy outlier detection.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/pandas-outliers/",
    packages=find_packages(),
    install_requires=["pandas", "numpy", "scikit-learn", "scipy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
