#!/usr/bin/python
from NodeGraphQt.base.node import NodeObject
from NodeGraphQt.qgraphics.node_group import GroupNodeItem


class GroupNode(NodeObject):

    NODE_NAME = 'Group Node'

    def __init__(self):
        super(GroupNode, self).__init__(GroupNodeItem())
