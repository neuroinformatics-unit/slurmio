import os
from slurmio import slurmio

sacct_file = os.path.join("tests", "data", "sacct.txt")


def test_slurm_environment():
    with open(sacct_file, "r") as file:
        sacct_ob = slurmio.SacctWrapper(file)

    params = slurmio.SlurmJobParameters(sacct_ob)
    assert 12 == params.requested_cores
    assert 168000 == params.requested_memory
    assert 1 == params.requested_nodes
    assert 24 == params.allocated_cores
    assert 336000000000 == params.allocated_memory
    assert 1 == params.allocated_nodes
    assert "test_slurm_job" == params.job_name
    assert 606501 == params.job_id
