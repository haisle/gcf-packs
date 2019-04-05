# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Library for running a computation across multiple devices.
"""

from __future__ import print_function as _print_function

from tensorflow._api.v2.compat.v1.distribute import cluster_resolver
from tensorflow._api.v2.compat.v1.distribute import experimental
from tensorflow.python.distribute.cross_device_ops import CrossDeviceOps
from tensorflow.python.distribute.cross_device_ops import HierarchicalCopyAllReduce
from tensorflow.python.distribute.cross_device_ops import NcclAllReduce
from tensorflow.python.distribute.cross_device_ops import ReductionToOneDevice
from tensorflow.python.distribute.distribute_lib import DistributionStrategy as Strategy
from tensorflow.python.distribute.distribute_lib import DistributionStrategyExtended as StrategyExtended
from tensorflow.python.distribute.distribute_lib import InputContext
from tensorflow.python.distribute.distribute_lib import InputReplicationMode
from tensorflow.python.distribute.distribute_lib import ReplicaContext
from tensorflow.python.distribute.distribute_lib import get_loss_reduction
from tensorflow.python.distribute.distribution_strategy_context import get_distribution_strategy as get_strategy
from tensorflow.python.distribute.distribution_strategy_context import get_replica_context
from tensorflow.python.distribute.distribution_strategy_context import has_distribution_strategy as has_strategy
from tensorflow.python.distribute.distribution_strategy_context import in_cross_replica_context
from tensorflow.python.distribute.mirrored_strategy import MirroredStrategy
from tensorflow.python.distribute.one_device_strategy import OneDeviceStrategy
from tensorflow.python.distribute.reduce_util import ReduceOp
from tensorflow.python.training.server_lib import Server

del _print_function
