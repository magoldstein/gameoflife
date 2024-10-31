from projects.gameoflife.world import World



def main():
    print("Welcome to the game of life")
    print("Press spacebar to stop the game, and press c to evolve when on manual mode")
    file: int = int(input("Enter 0 to select file, or enter 1 to select dimensions: "))
    if file == 0:
        file_name: str = input("Please enter the file name that you would like to read: ")
        rows = 10
        cols = 10
    else: 
        rows: int = int(input("Please enter rows dimension: "))
        cols: int = int(input("Please enter column dimension: "))
        file_name = None
    max_evo: int = int(input("Please give a maximum number of evolutions: "))
    time: int = int(input("Please enter the time in seconds you would like between generations, or enter 0 for manual evolution: "))
    world = World(rows, cols, max_evo, time, file_name)
    world.run()
    pass










if __name__ =='__main__':
    main()