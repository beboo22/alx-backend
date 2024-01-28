import csv
import math
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
        0-simple_helper_function
        """
        nPage = page * page_size
        return nPage - page_size, nPage

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        1-simple_pagination
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        Sindx, Eindx = self.index_range(page, page_size)
        return self.dataset()[Sindx:Eindx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        1-simple_pagination
        """
        data = self.get_page(page, page_size)
        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None
        Nrow = len(self.dataset())

        next_page = page + 1
        if self.index_range(page, page_size)[1] >= Nrow:
            next_page = None

        total_pages = Nrow / page_size
        return {'page_size': len(data), 'page': page,
                'data': data, 'next_page': next_page,
                'prev_page': prev_page, 'total_pages': int(total_pages)}
