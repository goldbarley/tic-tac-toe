from grid import initialize_grid, print_grid, GRID, GRID_SIZE
from math import floor
from sys import exit

def main():
    # Print the main menu
    print_menu()

    inpt = input("Enter command: ")

    if inpt[0] != ".":
        print("Not a command. All commands must begin with a dot '.'")
        print("Proper usage: .play_pvp or .play_pvc")
        exit(0)

    if ".play_pvp" == inpt.lower():
        play_pvp()

    elif ".play_pvc" == inpt.lower():
        # Coming soon... *probably*
        print("\nComing soon... *probably*")

    elif ".quit" == inpt.lower():
        exit(0)

    else:
        print("Invalid input. Program terminated.")
        exit(1)

def print_menu():

    """ Prints the main menu. """

    print("MAIN MENU:")
    print("1. Play vs Computer (coming soon... *probably*) [cmd: .play_pvc]")
    print("2. Play Player_1 vs Player_2 [cmd: .play_pvp]")
    print("3. Quit [cmd: .quit]\n")

def play_pvp():
    
    """ Includes some basic playing mechanics for a Tic-Tac-Toe game. """

    initialize_grid()

    print("\nStarting game...")
    print("\nPlayer 1: X\nPlayer 2: O\n")

    print()
    print_grid()
    print()

    # Generate instructions
    print("INSTRUCTIONS (How to play?):\n")
    print("For each player's turn, the players should mention the coordinates of the square, inside the grid, they want to play in.")
    print("For example, if it's X's turn, they should write \"2,2\" to play in the centre square or \"1,3\" to play in the top-right square.")
    print("You can quit anytime, just type the command [.quit]\n`")
    print("That's all!, enjoy the game!\n")

    iterations = 0

    while grid_has_whitespace():
        #Alternating turns for X and O
        if iterations % 2 == 0:
            coords = input("X's turn: ")

            print()

            if coords.lower() == ".quit":
                exit(0)

            if "," in coords:
                comma_present = True
            
            while len(coords) != 3 or not comma_present:
                coords = input("Invalid format. Proper usage: x,y (without any spaces)\nEnter again: ")

                if coords.lower() == ".quit":
                    exit(0)

                print()

                if "," in coords:
                    comma_present = True
            
            update_grid(coords, "X", 0)
            
            print_grid()

            if winner()[0] != "I":
                print(winner())
                exit(0)
            
            print("\n")
        
        else:
            coords = input("O's turn: ")
            print()

            if coords.lower() == ".quit":
                exit(0)
            
            if "," in coords:
                comma_present = True
            else: 
                comma_present = False

            while len(coords) != 3 or not comma_present:
                coords = input("Invalid format. Proper usage: x,y (without any spaces)\nEnter again: ")

                if coords.lower() == ".quit":
                    exit(0)

                print()

                if "," in coords:
                    comma_present = True

            update_grid(coords, "O", 0)

            print_grid()

            if winner()[0] != "I":
                print(winner())
                exit(0)
            
            print()
        
        iterations += 1


def winner():
    """
    Determines whether the result of the game and returns the player <number> who won the game.
	If no one wins, the game results in a draw.
    """

    #Checks for a win, horizontally
    for i in range(0, GRID_SIZE, 2):
        counter1 = 0
        counter2 = 0

        for j in range(0, GRID_SIZE, 2):
            if GRID[i][j] == "X":

                counter1 += 1
            elif GRID[i][j] == "O":
                counter2 += 1

            if counter1 == 3:
                return "\nPlayer 1 wins!"
            
            elif counter2 == 3:
                return "\nPlayer 2 wins!"
    
    # Checks for a win, vertically
    for i in range (0, GRID_SIZE, 2):
        counter1 = 0
        counter2 = 0

        for j in range(0, GRID_SIZE, 2):
            if GRID[j][i] == "X":
                counter1 += 1

            elif GRID[j][i] == "O":
                counter2 += 1

            if counter1 == 3:
                return "\nPlayer 1 wins!"
            
            elif counter2 == 3:
                return "\nPlayer 2 wins!"
            
    counter1 = 0
    counter2 = 0

    # Checks for a win in the left diagonal
    for i in range(0, GRID_SIZE, 2):
        if GRID[i][i] == "X":
            counter1 += 1

        elif GRID[i][i] == "O":
            counter2 += 1
    
    if counter1 == 3:
        return "\nPlayer 1 wins!"
    
    elif counter2 == 3:
        return "\nPlayer 2 wins!"
    
    # Checks for a win in the right diagonal
    if GRID[0][4] == GRID[2][2] and GRID[2][2] == GRID[4][0]:

        if GRID[2][2] == 'X':
            return "\nPlayer 1 wins!"
            
        elif GRID[2][2] == "O":
            return "\nPlayer 2 wins!"
    
    if not grid_has_whitespace():
        # Returns a draw if neither players win
        return "\nIt's a Draw!"
    
    else:
        #Returns I because of the checking mechanism I included in the previous function
        return "I"
    

def grid_has_whitespace():

    """ Checks if the Grid has any whitespaces left."""

    for row in GRID:
        if " " in row:
            return True
    return False


def update_grid(coords, player, rec):

    """
    A recursive function that updates the grid according the the "coords" provided by the player
	The parameter "rec" keeps track of the number of recursive calls
    """

    # If the recursive calls are more than 0 that means that the coordinates provided, although correct, are already occupied by another (or the same) player
    if rec > 0:
        coords = input("Enter again: ")

        if coords.lower() == ".quit":
            exit(0)
        print();
    
    x = int(coords[0])
    y = int(coords[2])

    while (x > 3 or x < 1) or (y > 3 or y < 0):
        coords = input("Invalid coordinates. Coordinates should be in the limit of the grid.\nEnter again: ")
        
        if coords.lower() == ".quit":
            exit(0)
            
        print()

        x = int(coords[0])
        y = int(coords[2])
    
    median = floor(GRID_SIZE / 2)

    # Converts the user's given coordinates into the actual coordinates of the grid
    if x < median and x % 2 != 0:
        x -= 1
    elif x > median and x % 2 != 0:
        x += 1
    
    if y < median and y % 2 != 0:
        y -= 1
    elif y > median and y % 2 != 0:
        y += 1

    if GRID[x][y] != " ":
        print("Square is already occupied.")

        # The function recursively calls itself while updating it's recursion count if coordinates for the square are already occupied
        update_grid(coords, player, rec + 1)
    else:
        GRID[x][y] = player

main()