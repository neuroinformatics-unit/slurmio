import setuptools

requirements = ["luddite"]


setuptools.setup(
    name="slurmio",
    version="0.0.4",
    author="Adam Tyson",
    author_email="adam.tyson@ucl.ac.uk",
    description="Python tools to interface with slurm",
    install_requires=requirements,
    extras_require={
        "dev": [
            "black",
            "pytest-cov",
            "pytest",
            "coveralls",
            "coverage<=4.5.4",
        ]
    },
    python_requires=">=3.6",
    url="https://github.com/adamltyson/slurmio",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
    ],
)
