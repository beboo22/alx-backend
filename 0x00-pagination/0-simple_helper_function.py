#!/usr/bin/env python3
"""
0-simple_helper_function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    0-simple_helper_function
    """
    nPage = page * page_size
    return nPage - page_size, nPage
