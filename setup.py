from setuptools import setup, find_packages

setup(
    name="mission-analysis-tool",
    version="0.1.0",
    description="Space systems mission analysis tool",
    author="araigumaichi",
    author_email="araigumaichi@github.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.21.0",
        "dask>=2023.0.0",
        "matplotlib>=3.5.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=1.0.0",
        ],
    },
    python_requires=">=3.8",
)