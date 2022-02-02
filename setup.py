import setuptools


setuptools.setup(
    name="slurmio",
    version="0.0.6",
    author="Adam Tyson",
    author_email="adam.tyson@ucl.ac.uk",
    description="Python tools to interface with slurm",
    extras_require={
        "dev": [
            "black",
            "flake8",
            "pytest-cov",
            "pytest",
            "coverage>=5.0.3",
        ]
    },
    python_requires=">=3.6",
    url="https://github.com/adamltyson/slurmio",
    packages=setuptools.find_packages(exclude=("tests", "tests.*")),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
    ],
)
