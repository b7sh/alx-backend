#!/usr/bin/env python3
"""
    Task - solving
"""
import csv
import math
from typing import List
index_range = __import__("0-simple_helper_function").index_range


class Server:
    """
        Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
            Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            takes two integer arguments page
            with default value 1 and page_size with default value 10.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        correct_indexes = index_range(page, page_size)
        first_index = correct_indexes[0]
        second_index = correct_indexes[1]
        try:
            return self.dataset()[first_index: second_index]
        except IndexError:
            return []
