"""
name: Joe Le 
"""

import sys, os 
sys.path.append(os.path.dirname(__file__))

from SearchStructures import Stack, Queue
from Maze import Maze

class MazeSolver:

    def __init__(self, maze, searchStructure):
        self.maze = maze             # The maze to solve
        self.ss = searchStructure()  # Initialize a searchStructure object (Stack or Queue)

    def tileIsVisitable(self, row, col):
       if row < 0 or row >= self.maze.num_rows or col < 0 or col >= self.maze.num_cols:
            return False
       else:
            return not (self.maze.contents[row][col].getIsWall() or self.maze.contents[row][col].isVisited())

    def solve(self):
        self.ss.add(self.maze.start)
        while not self.ss.isEmpty():
            current = self.ss.remove()
            current.visit()
            if current is self.maze.goal:
                return current
            else:
                for rd, cd in [(-1,0),(1,0),(0,-1),(0,1)]:
                    if self.tileIsVisitable(current.getRow()+rd,current.getCol()+cd):
                        self.maze.contents[current.getRow()+rd][current.getCol()+cd].setPrevious(current)
                        self.ss.add(self.maze.contents[current.getRow()+rd][current.getCol()+cd])
        return None



     # Add any other helper functions you might want here

    def getPath(self):
        current = self.maze.goal
        if current.getPrevious() is None:
            return None

        path = []
        while current is not self.maze.start:
            path.append(current.getPrevious())
            current = current.getPrevious()
        path.reverse()
        return path
    

    # Print the maze with the path of the found solution
    # from Start to Goal. If there is no solution, just
    # print the original maze.
    def printSolution(self):
        # Get the solution for the maze from the maze itself
        solution = self.getPath()
        # A list of strings representing the maze
        output_string = self.maze.makeMazeBase()
        # For all of the tiles that are part of the path, 
        # mark it with a *
        for tile in solution:
            output_string[tile.getRow()][tile.getCol()] = '*'
        # Mark the start and goal tiles
        output_string[self.maze.start.getRow()][self.maze.start.getCol()] = 'S'
        output_string[self.maze.goal.getRow()][self.maze.goal.getCol()] = 'G'

        # Print the output string
        for row in output_string:
            print(row)

   

if __name__ == "__main__":
    # The maze to solve
    maze = Maze(["____",
                 "S##G",
                 "__#_",
                 "____"])
    # Initialize the MazeSolver to be solved with a Stack
    solver = MazeSolver(maze, Stack)
    # Solve the maze
    solver.solve()
    # Print the solution found
    solver.printSolution()

