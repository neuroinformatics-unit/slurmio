import os

from slurmio import SacctWrapper, SlurmJobParameters

sacct_file = os.path.join("tests", "data", "sacct.txt")


def test_slurm_environment():
    with open(sacct_file, "r") as file:
        sacct_ob = SacctWrapper(file)

    params = SlurmJobParameters(sacct_ob)

    assert 606501 == params.job_id
    assert "test_slurm_job" == params.job_name
    assert "cpu" == params.partition
    assert 12 == params.requested_cores
    assert 12 == params.allocated_cores
    assert 1 == params.requested_nodes
    assert 1 == params.allocated_nodes
    assert 18000000 == params.requested_memory
    assert 18000000 == params.allocated_memory

    assert "12" == params._trackable_resources["cpu"]
    assert "18G" == params._trackable_resources["mem"]
    assert "1" == params._trackable_resources["node"]
