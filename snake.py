

from typing import List, Optional, Tuple
from grid import Grid,Direction



class Snake(object):
    grid:Grid
    length:Optional[int]
    segments:List[Tuple[int]]
    directions:List[Direction]

    def __init__(self,grid:Grid,length:Optional[int] = None):
        self.length = length
        self.grid = grid
        self.directions = list()

    def to_list(self)->List[Tuple[int,int]]:
        return self.segments
    
    def create_interactive(self,length:int, head:Tuple[int,int]):
        if self.length is not None:
            raise ValueError("Snake already initialised")
        self.length = length
        self.segments = list()
        self.segments.append(head)

    def int_add_seg(self,segment:Tuple[int,int]):
        raise NotImplementedError("NOt working yet! ")
        if segment not in self.int_options():
            raise ValueError("You are trying to add an invalid segment.")
        if len(self.segments) >= self.length:
            raise ValueError("You are trying to add to a finished snake.")
        self.segments.append(segment)

    def int_mv_seg(self,direction:Direction):
        if len(self.segments) >= self.length:
            raise ValueError("You are trying to add to a finished snake.")
        tail = self.segments[-1]
        segment = self.grid.getNext(tail,direction)
        if self.grid.is_occupied(segment):
            raise ValueError(f"You are trying to move occupied segment: {segment}")
        self.segments.append(segment)
        self.directions.append(direction)
        self.grid.register(segment)

    def int_options(self)->List[Tuple[Tuple[int,int],Direction]]:
        if len(self.segments) >= self.length:
            return []
        tail = self.segments[-1]
        neighbours = self.grid.neighbours(tail)
        return neighbours
        
    
