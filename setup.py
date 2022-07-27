#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import setuptools

class pkg_info:
    __version__ = '0.2.5'
    __status__ = 'Work in Progress'
    __license__ = 'MIT'

    __author__ = 'Johnny Chan'

    __module_name__ = 'NodeGraphQt'
    __url__ = 'https://github.com/jchanvfx/NodeGraphQt'


if __name__ == '__main__':
    setuptools.setup(
        name=pkg_info.__module_name__,
        version=pkg_info.__version__,
        author=pkg_info.__author__,
    )
