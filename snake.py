

from typing import List, Optional, Tuple
from .grid import Grid,Direction



class Snake(object):
    length:Optional[int]
    segments:List[Tuple[int]]

    def __init__(self,length:Optional[int] = None):
        self.length = length

    def create_from_list(self,segments:List[Tuple[int,int]]):
        if self.length is not None:
            raise ValueError("Snake already initialised")
        self.segments = segments

    def to_list(self)->List[Tuple[int,int]]:
        return self.segments
    
    def create_interactive(self,length:int, head:Tuple[int,int]):
        if self.length is not None:
            raise ValueError("Snake already initialised")
        self.length = length
        self.segments = list()
        self.segments.append(head)

    def int_add_seg(self,segment:Tuple[int,int]):
        if segment not in self.int_options():
            raise ValueError("You are trying to add an invalid segment.")
        if len(self.segments) >= self.length:
            raise ValueError("You are trying to add to a finished snake.")
        self.segments.append(segment)

    def int_mv_seg(self,direction:Direction):
        if len(self.segments) >= self.length:
            raise ValueError("You are trying to add to a finished snake.")
        tail = self.segments[-1]
        segment = Grid.getNext(tail,direction)
        self.segments.append(segment)


    def int_options(self)->List(Tuple[int,int]):
        tail = self.segments[-1]
        neighbours = Grid.neighbours(tail)
        return neighbours
        
    
