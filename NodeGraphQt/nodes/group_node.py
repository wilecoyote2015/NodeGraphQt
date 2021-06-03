#!/usr/bin/python
from NodeGraphQt.constants import (NODE_LAYOUT_VERTICAL,
                                   NODE_LAYOUT_HORIZONTAL)
from NodeGraphQt.nodes.base_node import BaseNode
from NodeGraphQt.qgraphics.node_group import (GroupNodeItem,
                                              GroupNodeVerticalItem)


class GroupNode(BaseNode):
    """
    The ``NodeGraphQt.GroupNode`` class extends from the
    :class:``NodeGraphQt.BaseNode`` class with the ability to nest other nodes
    inside of it.

    **Inherited from:** :class:`NodeGraphQt.BaseNode`
    """

    NODE_NAME = 'Group'

    def __init__(self, qgraphics_views=None):
        qgraphics_views = qgraphics_views or {
            NODE_LAYOUT_HORIZONTAL: GroupNodeItem,
            NODE_LAYOUT_VERTICAL: GroupNodeVerticalItem
        }
        super(GroupNode, self).__init__(qgraphics_views)

    def expand(self):
        return

    def collapse(self):
        return
