from datastructures.array2d import Array2D
from datastructures.iarray import IArray
import random
from time import sleep
from projects.gameoflife.kbhit import KBHit



class World():
    def __init__(self, rows: int = 10, cols: int = 10, max_evo: int = 75, speed: int = 2, file_name: str = None):
        self._max_evolutions = max_evo
        self._time = speed

        if file_name != None:
            with open(file_name, "r") as file:
                data = file.read()
                print(data)
                number = 0
                for line in file:
                    print(line)
                    if len(line) != 0:
                        if line[0] != "#":
                            if number == 0:
                                self._rows = int(line)
                                print(line)
                            elif number == 1:
                                self._cols = int(line)
                                print(line)
                                self._current_grid: IArray[IArray[bool]] = Array2D.empty(self._rows, self._cols, bool)
                            else:
                                for j in range(self._cols):
                                    self._current_grid[number-2][j] = True if line[j] == "X" else False
                            number += 1
                        
                
        else:
            self._rows = rows
            self._cols = cols
            self._current_grid: IArray[IArray[bool]] = Array2D.empty(rows,cols,bool)
            self._grid_history = []
            for i in range(len(self._current_grid)): #making the grid
                for j in range(len(self._current_grid[i])):
                    chance = random.randint(0,2)
                    if chance == 2:
                        self._current_grid[i][j] = True

    def evolve(self):
        new_grid = Array2D.empty(self._rows,self._cols,bool)
        for i in range(len(self._current_grid)):
            for j in range(len(self._current_grid[i])):
                neighbors = 0 #starting and zero and going through all possible locations to find out how many neighbors each cell has
                if i - 1 > -1:
                    neighbors += 1 if self._current_grid[i-1][j] else + 0
                    if j - 1 > -1:
                        neighbors += 1 if self._current_grid[i-1][j-1] else + 0
                    if j + 1 < self._cols:
                        neighbors += 1 if self._current_grid[i-1][j+1] else + 0
                if i + 1 < self._rows:
                    neighbors += 1 if self._current_grid[i+1][j] else + 0
                    if j - 1 > -1:
                        neighbors += 1 if self._current_grid[i+1][j-1] else + 0
                    if j + 1 < self._cols:
                        neighbors += 1 if self._current_grid[i+1][j+1] else + 0
                if j - 1 > -1:
                    neighbors += 1 if self._current_grid[i][j-1] else + 0
                if j + 1 < self._cols:
                    neighbors += 1 if self._current_grid[i][j+1] else + 0

                if neighbors == 2: #checking if it needs to make the bacteria alive next generation
                    new_grid[i][j] = self._current_grid[i][j]
                elif neighbors == 3:
                    new_grid[i][j] = True
        if self._current_grid == new_grid:
            print("No evolution occuring")
            exit()
        self._current_grid = new_grid


    def print_current_grid(self) -> None:
        for row in self._current_grid:
            for item in row:
                print_value = "X" if item else "."
                print(print_value, end=" ")
            print("")
        print("")

    def run(self) -> None:
        kb = KBHit()
        evo = 0
        self.print_current_grid()
        if self._time > 0:
            while evo < self._max_evolutions:
                sleep(self._time)
                if kb.kbhit():
                    key = (kb.getch())
                    if key == 32:
                        print("Game of life simulation stopped.")
                        exit()
                self.evolve()
                self.print_current_grid()
                evo += 1
            print("Max evolutions reached.")
            exit()
        else:
            while evo < self._max_evolutions:
                if kb.kbhit():
                    key = (kb.getch())
                    if key == 32:
                        print("Game of life simulation stopped.")
                        exit()
                    if key == "c":
                        self.evolve()
                        self.print_current_grid()
                        evo += 1
                        sleep(0.1)
            print("Max evolutions reached")
            exit()


