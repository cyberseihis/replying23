from enum import Enum
from typing import Dict, List, Set, Tuple
import numpy as np

class Direction(Enum,str):
    U=1
    D=2
    L=3
    R=4

class Grid:
    grid_weigths:np.ndarray
    grid_snakes:np.ndarray
    wormholes:Set[Tuple(int,int)]
    def __init__(self,parsed_grid:List[List[int]]) -> None:
        wormholes = set()
        for i in range(len(parsed_grid)):
            for j in range(len(parsed_grid[i])):
                if parsed_grid[i][j] == '*':
                    #set wormholes
                    wormholes.add((i,j))
                    parsed_grid[i][j] = 0
        self.grid_weigths = np.array(parsed_grid)
        self.grid_snakes = np.zeros(self.grid_weigths.shape)
    def neighbours(self,origin: Tuple[int,int])->List(Tuple(Tuple[int,int],Direction)):
        possible_whole = [
            self.getNext(origin,Direction.U),
            self.getNext(origin,Direction.D),
            self.getNext(origin,Direction.L),
            self.getNext(origin,Direction.R),
            ]
        n_list = list()
        w_stack = set()
        while not possible_whole:
            n = possible_whole.pop()
            if self.is_occupied(n):
                continue
            if n in self.wormholes and n not in w_stack:
                #get neighbours from all wholes
                w_stack.add(n)
                for w in (self.wormholes ^ {n}):
                    tmp = [self.getNext(w,Direction.U),
                    self.getNext(w,Direction.D),
                    self.getNext(w,Direction.L),
                    self.getNext(w,Direction.R)]
                    possible_whole + tmp
            else:
                n_list.append(n)

    def register(self,origin: Tuple[int,int]):
        x,y = origin
        self.grid_snakes[x,y]

    def is_occupied(self,origin: Tuple[int,int]):
        x,y = origin
        return  self.grid_snakes[x,y] == 1
                
    def getNext(self,origin: Tuple[int,int],direction:Direction):
        x,y = origin
        match(direction):
            case Direction.U:
                r_ =  (x,y+1)
            case Direction.D:
                r_ =  (x,y-1)
            case Direction.L:
                r_ =  (x-1,y)
            case Direction.R:
                r_ =  (x+1,y)
            case _:
                raise ValueError("match error")