from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("slurmio")
except PackageNotFoundError:
    # package is not installed
    pass

from slurmio.slurmio import (
    SlurmJobParameters,
    SacctWrapper,
    SlurmEnvironmentError,
)
