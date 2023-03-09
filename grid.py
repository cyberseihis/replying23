from enum import Enum
from typing import Tuple


class Direction(Enum):
    'U':1
    'D':2
    'L':3
    'R':4



class Grid:
    @staticmethod
    def neighbours(origin: Tuple[int,int]):
        raise NotImplementedError()
        ...
    @staticmethod
    def getNext(origin: Tuple[int,int],direction:Direction):
        raise NotImplementedError()
        ...