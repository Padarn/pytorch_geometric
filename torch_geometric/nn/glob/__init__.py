from .glob import global_add_pool, global_mean_pool, global_max_pool
from .glob import GlobalPooling
from .attention import GlobalAttention
from .gmt import GraphMultisetTransformer

__all__ = [
    'global_add_pool',
    'global_mean_pool',
    'global_max_pool',
    'GlobalPooling',
    'GlobalAttention',
    'GraphMultisetTransformer',
]

classes = __all__

from torch_geometric.deprecation import deprecated  # noqa
from torch_geometric.nn.aggr import Set2Set  # noqa
from torch_geometric.nn.aggr import SortAggr  # noqa

Set2Set = deprecated(
    details="use 'nn.aggr.Set2Set' instead",
    func_name='nn.glob.Set2Set',
)(Set2Set)


@deprecated(
    details="use 'nn.aggr.GlobalSortAggr' instead",
    func_name='nn.glob.global_sort_pool',
)
def global_sort_pool(x, index, k):
    module = SortAggr(k=k)
    return module(x, index=index)
