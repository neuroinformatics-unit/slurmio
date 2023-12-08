[![Python Version](https://img.shields.io/pypi/pyversions/slurmio.svg)](https://pypi.org/project/slurmio)
[![PyPI](https://img.shields.io/pypi/v/slurmio.svg)](https://pypi.org/project/slurmio)
[![Downloads](https://pepy.tech/badge/slurmio)](https://pepy.tech/project/slurmio)
[![Development Status](https://img.shields.io/pypi/status/slurmio.svg)](https://github.com/neuroinformatics-unit/slurmio)
[![Tests](https://img.shields.io/github/workflow/status/neuroinformatics-unit/slurmio/tests)](https://github.com/neuroinformatics-unit/slurmio/actions)
[![codecov](https://codecov.io/gh/neuroinformatics-unit/slurmio/graph/badge.svg?token=utApXQgGMa)](https://codecov.io/gh/neuroinformatics-unit/slurmio)

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
>>> from slurmio import SlurmJobParameters
>>> slurm_parameters = SlurmJobParameters()
>>> slurm_parameters.job_id
994986
>>> slurm_parameters.job_name
'bash'
>>> slurm_parameters.partition
'cpu'
>>> slurm_parameters.requested_cores
10
>>> slurm_parameters.allocated_cores
10
>>> slurm_parameters.requested_nodes
10
>>> slurm_parameters.allocated_nodes
10
>>> slurm_parameters.requested_memory
10240 # in bytes
>>> slurm_parameters.allocated_memory
10240 # in bytes
