"""
slurmio
===============

Wrappers around slurm command line utilities for querying available resources
etc.

"""

import re
import os


class SacctWrapper:
    """
    Takes the output of the slurm "sacct" command (via pipe or file) and
    sets the attributes based on the output
    """

    def __init__(self, file):
        for idx, line in enumerate(file):
            if idx == 0:
                line = re.sub(" +", " ", line.strip())
                names = line.split("|")
            elif idx == 1:
                line = re.sub(" +", " ", line.strip())
                values = line.split("|")

        for idx, value in enumerate(values):
            if value == "":
                value = None
            setattr(self, names[idx], value)


def sacct():
    """
    Wrapper around the slurm "sacct" command. Returns an object, and each
    property is the (unformatted) value according to sacct.

    Would also work with .e.g:
    # with open("/home/Desktop/sacct.txt", "r") as file:

    :return: SacctWrapper object, with attributes based on the output of sacct
    """
    with os.popen("sacct -j $SLURM_JOB_ID -l --parsable2") as file:
        return SacctWrapper(file)


class SlurmJobParameters:
    """
    Convenience class to request slurm job parameters
    """

    # TODO: add "available_memory" property

    def __init__(self, sacct_object=None):
        if sacct_object is None:
            self.sacct_object = sacct()
        else:
            self.sacct_object = sacct_object

    @property
    def allocated_cores(self):
        """
        Returns the amount of cores allocated by slurm (not requested).
        :return: Number of cores
        """
        return int(self.sacct_object.AllocCPUS)

    @property
    def allocated_memory(self):
        """
        Returns the amount of memory allocated by slurm (not requested). In MB.
        :return: Memory in bytes
        """
        parts = self.sacct_object.AllocTRES.split(",")
        memory = int(parts[1].split("=")[1])
        return memory * 10 ** 6

    @property
    def allocated_nodes(self):
        """
        Returns the number of nodes allocated by slurm (not requested).
        :return: Number of nodes
        """
        parts = self.sacct_object.AllocTRES.split(",")
        num_nodes = int(parts[2].split("=")[1])
        return num_nodes

    @property
    def requested_cores(self):
        """
        Returns the amount of cores requested from slurm.
        :return: Number of cores
        """
        parts = self.sacct_object.ReqTRES.split(",")
        memory = int(parts[0].split("=")[1])
        return memory

    @property
    def requested_memory(self):
        """
        Returns the amount of memory requested from slurm.. In MB.
        :return: Memory in MB
        """
        parts = self.sacct_object.ReqTRES.split(",")
        memory = int(parts[1].split("=")[1])
        return memory

    @property
    def requested_nodes(self):
        """
        Returns the number of nodes requested from slurm.
        :return: Number of nodes
        """
        parts = self.sacct_object.ReqTRES.split(",")
        num_nodes = int(parts[2].split("=")[1])
        return num_nodes

    @property
    def get_job_name(self):
        """
        Returns the job name given to slurm
        :return: Job Name
        """
        return self.sacct_object.JobName

    @property
    def job_name(self):
        """
        Returns the job name given to slurm
        :param sacct_object: Object with properties matching the output of sacct.
        :return: Job Name
        """
        return self.sacct_object.JobName

    @property
    def job_id(self):
        """
        Returns the job name given to slurm
        :return: Job ID
        """
        return int(self.sacct_object.JobID)
