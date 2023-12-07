[![Python Version](https://img.shields.io/pypi/pyversions/slurmio.svg)](https://pypi.org/project/slurmio)
[![PyPI](https://img.shields.io/pypi/v/slurmio.svg)](https://pypi.org/project/slurmio)
[![Downloads](https://pepy.tech/badge/slurmio)](https://pepy.tech/project/slurmio)
[![Development Status](https://img.shields.io/pypi/status/slurmio.svg)](https://github.com/adamltyson/slurmio)
[![Tests](https://img.shields.io/github/workflow/status/adamltyson/slurmio/tests)](
    https://github.com/adamltyson/slurmio/actions)
[![Coverage Status](https://coveralls.io/repos/github/adamltyson/slurmio/badge.svg?branch=main)](https://coveralls.io/github/instituteofcancerresearch/slurmio?branch=main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
# slurmio
Python tools to read [SLURM](https://slurm.schedmd.com/documentation.html) job
parameters.

### Installation
Pip
```bash
pip install slurmio
```

Conda
```bash
conda install -c conda-forge slurmio
```

From source:
```bash
git clone https://github.com/neuroinformatics-unit/slurmio
cd slurmio
pip install .
```


### Usage
```bash
>>> from slurmio.slurmio import SlurmJobParameters
>>> SlurmJobParameters().job_id
994986
>>> SlurmJobParameters().job_name
'bash'
>>> SlurmJobParameters().requested_cores
10
>>> SlurmJobParameters().allocated_cores
24
>>> SlurmJobParameters().requested_memory
10240 # in bytes
>>> SlurmJobParameters().allocated_memory
24576000000 # in bytes
>>> SlurmJobParameters().requested_nodes
1
>>> SlurmJobParameters().allocated_nodes
1
