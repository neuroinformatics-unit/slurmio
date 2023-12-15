"""
slurmio
===============

Wrappers around SLURM command line utilities for querying available resources
etc.

"""

import os
import re


class SlurmEnvironmentError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str(self.message)


class SacctWrapper:
    """
    Takes the output of the SLURM "sacct" command (via pipe or file) and
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

    Also works with .e.g:
    # with open("/home/Desktop/sacct.txt", "r") as file:

    :return: SacctWrapper object, with attributes based on the output of sacct
    """

    try:
        # if in slurm environment
        os.environ["SLURM_JOB_ID"]
        with os.popen(
            "sacct -j $SLURM_JOB_ID --format=jobid,partition,"
            "jobname,reqmem,reqcpus,alloccpus,"
            "reqnodes,allocnodes,reqtres,alloctres --parsable2"
        ) as file:
            return SacctWrapper(file)
    except KeyError:
        raise SlurmEnvironmentError(
            "'SLURM_JOB_ID' cannot be found in the environment. "
            "Please ensure you are running 'slurmio' in a SLURM job."
        )


class SlurmJobParameters:
    """
    Convenience class to request slurm job parameters
    """

    def __init__(self, sacct_object=None):
        if sacct_object is None:
            self.sacct_object = sacct()
        else:
            self.sacct_object = sacct_object

    @property
    def job_id(self) -> int:
        """
        Returns the job ID
        :return: Job ID
        """
        return int(self.sacct_object.JobID)

    @property
    def job_name(self) -> str:
        """
        Returns the job name
        :return: Job Name
        """
        return self.sacct_object.JobName

    @property
    def partition(self) -> str:
        """
        Returns the partition name
        :return: Partition name
        """
        return self.sacct_object.Partition

    @property
    def requested_cores(self) -> int:
        """
        Returns the number of cores requested
        :return: Number of cores
        """
        return int(self.sacct_object.ReqCPUS)

    @property
    def allocated_cores(self) -> int:
        """
        Returns the number of cores allocated
        :return: Number of cores
        """
        return int(self.sacct_object.AllocCPUS)

    @property
    def requested_nodes(self) -> int:
        """
        Returns the number of nodes requested
        :return: Number of nodes
        """
        return int(self.sacct_object.ReqNodes)

    @property
    def allocated_nodes(self) -> int:
        """
        Returns the number of nodes allocated
        :return: Number of nodes
        """
        return int(self.sacct_object.AllocNodes)

    @property
    def requested_memory(self) -> int:
        """
        Returns the amount of memory requested
        :return: Memory in bytes
        """

        return convert_mem_to_bytes(self.sacct_object.ReqMem)

    @property
    def allocated_memory(self) -> int:
        """
        Returns the amount of memory allocated
        :return: Memory in bytes
        """
        return convert_mem_to_bytes(self._trackable_resources["mem"])

    @property
    def _trackable_resources(self) -> dict:
        """
        Returns Trackable resources. These are the resources allocated
        to the job/step after the job started running.
        For pending jobs this should be blank.
        :return: Dictionary of trackable resources
        """
        return dict(
            item.split("=") for item in self.sacct_object.AllocTRES.split(",")
        )


def convert_mem_to_bytes(s):
    if s.endswith("G"):
        return int(s[:-1]) * 10**9
    else:
        return int(s)
