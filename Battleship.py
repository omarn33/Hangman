#Omar N
#CIS 1400
#Battleship Game
#7/24/19
#This project is a one player Battleship game against the CPU.
#The user first sets up their ships and then alternates turns with the CPU
#in guessing the coordinates of the enemy's ships. The first to destroy the
#opponent's ships wins the game!

import random
name = ""

#User Global Variables
userAircraftCarrier = 5
userBattleship = 4
userSub = 3
userDestroyer = 2
userShipUnits = 14

#CPU Global Variables
cpuAircraftCarrier = 5
cpuBattleship = 4
cpuSub = 3
cpuDestroyer = 2
cpuShipUnits = 14

#Global GameBoard Selection
x = 0

def main():

    playAgain = 'y'
    while playAgain.lower() == 'y':
        generalGamePlay()
        cpuGameBoard = cpuGamePlay()
        userGameBoard = userGamePlay(cpuGameBoard)
        print()
        print()
        print("Would you like to play again?")
        print()
        playAgain = input("Enter 'y' for yes or any other key for no: ")
        print()
    end = input("Press 'Enter' to quit: ")
    
##----GENERAL GAME PLAY FUNCTIONS-----
def generalGamePlay():
    welcomeScreen()
    instructions()
    
    
def welcomeScreen():
    print("/////////////////////////////////////////////////////////////////////////")
    print("                         WELCOME TO BATTLESHIP")
    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
    print()
    print("Please make your screen FULL SCREEN in order to enhance gaming experience!")
    print()
    global name
    name = input("Enter your name: ")
    print("Welcome Chief Admiral " + name)
    print()

def instructions():
    print("HERE'S HOW TO PLAY: ")
    print()
    print("1. The object of the game is to sink the CPU's ships.")
    print()
    print("2. You and the CPU will each have 4 ships which include: an Aircraft Carrier, a Battleship, a Submarine, and a Destroyer.")
    print()
    print("3. You and the CPU will take turns guessing where the other's ships are located.")
    print()
    print("4. The first to sink the other's ships will win the game!")
    print()
    cont = input("Enter 'c' to continue: ")
    while cont.lower() != 'c':
        print()
        print("INVALID INPUT!")
        cont = input("Please enter 'c' to continue: ")
    
    print()
    print("GENERAL GAME PLAY RULES: ")
    print()
    print("1. You will first be prompted to enter your ships on your Game Board before starting the official game.")
    print()
    print("2. The Game Board will be a two-dimensional coordinate grid that will contain letters on the left and numbers on the top.")
    print()
    print("3. When choosing a coordinate, either for placing a ship or attacking an enemy ship, make sure to enter in the letter first before the corresponding number (ex: 'D3').")
    print()
    print("4. Make sure you are familiar with the following symbols that will show up on your Game Board before starting the game:")
    print("         . -- an open body of water ")
    print("         X -- a missed shot ")
    print("         H -- a successful HIT on a ship ")
    print("         # -- the total destruction of a ship ")
    print("         A -- Aircraft Carrier ")
    print("         B -- Battleship ")
    print("         S -- Submarine ")
    print("         D -- Destroyer ")
    print()
    print("5. Lastly, in case of an improper input, you will recieve the 'INVALID INPUT!' message. You will then be prompted to enter in a different response until deemed acceptable.")
    print()
    ready = input("Are you ready to play? Enter 'y' for yes: ")
    while ready.lower()!= 'y':
        print()
        print("INVALID INPUT!")
        ready = input("Please enter 'y' to start the game: ")
    return ready
    

##----USER GAME PLAY FUNCTIONS----  
def userGamePlay(cpuGameBoard):
    gameBoard = generateGameBoard()
    print()
    printGameBoard(gameBoard)

    userGameBoard = setUpShips(gameBoard)

    #Game Board to track user's guesses
    userGuessBoard = generateGameBoard()
    
    print()
    print("ITS TIME TO ATTACK THE CPU'S SHIPS!")

    #problems:
    #1. updating gameboard after miss or hit
    #2. showing congrats message
    #3. Can CPU ever win?
    
    global userShipUnits
    global cpuShipUnits
    
    while userShipUnits != 0 and cpuShipUnits != 0:
        #print("User ShipUnits Remaining: ", userShipUnits)
        #print("CPU ShipUnits Remaining: ", cpuShipUnits)

        userGuessBoard = userGuess(userGuessBoard, cpuGameBoard)
        if cpuShipUnits == 0:
            print("CONGRATULATIONS! Chief Admiral", name + ", you WON!")
            print()
            break
            
        cpuGuessBoard = cpuGuess(userGameBoard)
        if userShipUnits == 0:
            print("Oh no! Chief Admiral", name + ", you LOST!")
            print()
            break
        
    return gameBoard

def generateGameBoard():
    
    gameBoard = [['0','1','2','3','4','5','6','7','8','9','10',' ', ' ', ' '],
                 ['A','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                 ['B','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                 ['C','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                 ['D','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                 ['E','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                 ['F','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                 ['G','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                 ['H','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                 ['I','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                 ['J','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                 [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ', ' '],
                 [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ', ' '],
                 [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ', ' ']]

    return gameBoard

def userGuess(userGuessBoard, cpuGameBoard):
    print()
    printGameBoard(userGuessBoard)
    print("Choose a coordinate to attack!")
    print()

    userTurn = True
    while userTurn:
        coordinate = chooseCoordinates()
        r = returnRowLetter(coordinate)
        c = returnColNumber(coordinate)

        while((userGuessBoard[r][c] in 'H') or (userGuessBoard[r][c] in '#') or (userGuessBoard[r][c] in 'X')):
            print()
            print("INVALID INPUT!")
            print("You already entered this coordinate before!")
            print()
            coordinate = chooseCoordinates()
            r = returnRowLetter(coordinate)
            c = returnColNumber(coordinate)

        while(cpuGameBoard[r][c] in 'ABDS'):

            global cpuShipUnits
            cpuShipUnits -= 1

            if cpuGameBoard[r][c] in 'A':
                global cpuAircraftCarrier
                cpuAircraftCarrier -= 1

                userGuessBoard[r][c] = 'H'
                printGameBoard(userGuessBoard)
                print("HIT!")
                print()

                if cpuAircraftCarrier == 0:
                    hitEnter = input("Press 'Enter' to continue: ")
                    print()
                    print("You destroyed the CPU's Aircraft Carrier!")
                    print()

                    if x == 1:
                        userGuessBoard = changeGameBoard(6, 1, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(7, 1, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(8, 1, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(9, 1, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(10, 1, "#", userGuessBoard)
                        printGameBoard(userGuessBoard)

                    if x == 2:
                        userGuessBoard = changeGameBoard(4, 3, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(4, 4, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(4, 5, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(4, 6, "#", userGuessBoard) 
                        userGuessBoard = changeGameBoard(4, 7, "#", userGuessBoard)
                        printGameBoard(userGuessBoard)

                    if x == 3:
                        userGuessBoard = changeGameBoard(1, 4, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(1, 5, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(1, 6, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(1, 7, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(1, 8, "#", userGuessBoard)   
                        printGameBoard(userGuessBoard)

                    if x == 4:
                        userGuessBoard = changeGameBoard(10, 4, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(10, 5, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(10, 6, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(10, 7, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(10, 8, "#", userGuessBoard)
                        printGameBoard(userGuessBoard)

                    if x == 5:
                        userGuessBoard = changeGameBoard(4, 5, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(5, 5, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(6, 5, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(7, 5, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(8, 5, "#", userGuessBoard)
                        printGameBoard(userGuessBoard)
    
            if cpuGameBoard[r][c] in 'B':
                global cpuBattleship
                cpuBattleship -= 1

                userGuessBoard[r][c] = 'H'
                printGameBoard(userGuessBoard)
                print("HIT!")
                print()

                if cpuBattleship == 0:
                    hitEnter = input("Press 'Enter' to continue: ")
                    print()
                    print("You destroyed the CPU's Battleship!")
                    print()

                    if x == 1:
                        userGuessBoard = changeGameBoard(7, 6, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(7, 7, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(7, 8, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(7, 9, "#", userGuessBoard)
                        printGameBoard(userGuessBoard)

                    if x == 2:
                        userGuessBoard = changeGameBoard(8, 3, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(8, 4, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(8, 5, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(8, 6, "#", userGuessBoard)
                        printGameBoard(userGuessBoard)

                    if x == 3:
                        userGuessBoard = changeGameBoard(7, 5, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(8, 5, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(9, 5, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(10, 5, "#", userGuessBoard) 
                        printGameBoard(userGuessBoard)

                    if x == 4:
                        userGuessBoard = changeGameBoard(1, 1, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(1, 2, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(1, 3, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(1, 4, "#", userGuessBoard)
                        printGameBoard(userGuessBoard)

                    if x == 5:
                        userGuessBoard = changeGameBoard(10, 7, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(10, 8, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(10, 9, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(10, 10, "#", userGuessBoard)
                        printGameBoard(userGuessBoard)
                
            if cpuGameBoard[r][c] in 'S':
                global cpuSub
                cpuSub -= 1

                userGuessBoard[r][c] = 'H'
                printGameBoard(userGuessBoard)
                print("HIT!")
                print()

                if cpuSub == 0:
                    hitEnter = input("Press 'Enter' to continue: ")
                    print()
                    print("You destroyed the CPU's Submarine!")
                    print()

                    if x == 1:
                        userGuessBoard = changeGameBoard(3, 3, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(3, 4, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(3, 5, "#", userGuessBoard)
                        printGameBoard(userGuessBoard)

                    if x == 2:
                        userGuessBoard = changeGameBoard(1, 10, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(2, 10, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(3, 10, "#", userGuessBoard)
                        printGameBoard(userGuessBoard)

                    if x == 3:
                        userGuessBoard = changeGameBoard(3, 1, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(3, 2, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(3, 3, "#", userGuessBoard)
                        printGameBoard(userGuessBoard)

                    if x == 4:
                        userGuessBoard = changeGameBoard(1, 5, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(1, 6, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(1, 7, "#", userGuessBoard)
                        printGameBoard(userGuessBoard)

                    if x == 5:
                        userGuessBoard = changeGameBoard(8, 2, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(9, 2, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(10, 2, "#", userGuessBoard)
                        printGameBoard(userGuessBoard)

            if cpuGameBoard[r][c] in 'D':
                global cpuDestroyer
                cpuDestroyer -= 1
                
                userGuessBoard[r][c] = 'H'
                printGameBoard(userGuessBoard)
                print("HIT!")
                print()

                if cpuDestroyer == 0:
                    hitEnter = input("Press 'Enter' to continue: ")
                    print()
                    print("You destroyed the CPU's Destroyer!")
                    print()

                    if x == 1:
                        userGuessBoard = changeGameBoard(2, 9, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(3, 9, "#", userGuessBoard)
                        printGameBoard(userGuessBoard)

                    if x == 2:
                        userGuessBoard = changeGameBoard(6, 3, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(7, 3, "#", userGuessBoard)
                        printGameBoard(userGuessBoard)

                    if x == 3:
                        userGuessBoard = changeGameBoard(9, 2, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(10, 2, "#", userGuessBoard)
                        printGameBoard(userGuessBoard)

                    if x == 4:
                        userGuessBoard = changeGameBoard(5, 1, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(6, 1, "#", userGuessBoard)
                        printGameBoard(userGuessBoard)

                    if x == 5:
                        userGuessBoard = changeGameBoard(1, 1, "#", userGuessBoard)
                        userGuessBoard = changeGameBoard(1, 2, "#", userGuessBoard)
                        printGameBoard(userGuessBoard)
                        
            if cpuShipUnits == 0:
                print("You destroyed all the CPU's ships!")
                userTurn = False
                print()

                return userGuessBoard

            hitEnter = input("Press 'Enter' to continue: ")
            print()
            print("Choose another coordinate to attack again!")
            
            coordinate = chooseCoordinates()
            r = returnRowLetter(coordinate)
            c = returnColNumber(coordinate)

            while((userGuessBoard[r][c] in 'H') or (userGuessBoard[r][c] in '#') or (userGuessBoard[r][c] in 'X')):
                print()
                print("INVALID INPUT!")
                print("You already entered this coordinate before!")
                print()
                coordinate = chooseCoordinates()
                r = returnRowLetter(coordinate)
                c = returnColNumber(coordinate)
                
        print()

        userGuessBoard[r][c] = 'X'
        printGameBoard(userGuessBoard)
        print("Miss")
        print()
        enter = input("Press 'Enter' to continue: ")
        print()

        print("                                 CPU's Turn")
        
        userTurn = False

        return userGuessBoard
        
def setUpShips(gameBoard):
    print("ITS TIME TO SET UP YOUR SHIPS!")
    print()
    gameBoardAfterACSetUp = setUpAircraftCarrier(gameBoard)
    print("The Aircraft Carrier has been successfully set up!")
    print()
    gameBoardAfterBSetUp = setUpBattleship(gameBoardAfterACSetUp)
    print("The Battleship has been successfully set up!")
    print()
    
    gameBoardAfterSSetUp = setUpSub(gameBoardAfterBSetUp)
    print("The Submarine has been successfully set up!")
    print()
    
    gameBoardAfterDSetUp = setUpDestroyer(gameBoardAfterSSetUp)
    print("The Destroyer has been successfully set up!")
    print()

    print("Ship set up complete! Chief Admiral " + name + ", you are now ready for battle!")
    
    print()
    hitEnter = input("Press 'Enter' to continue: ")
    print()

    return gameBoardAfterDSetUp    

def setUpAircraftCarrier(gameBoard):

    shipUnits = 5
    shipLabel = "A"
    print("First is the Aircraft Carrier, which covers 5 coordinate positions.")
    gameBoardAfterACSetUp = setUp_VerifyShips(shipUnits, shipLabel, gameBoard)

    return gameBoardAfterACSetUp

def setUpBattleship(gameBoard):

    shipUnits = 4
    shipLabel = "B"
    print("Next is the Battleship, which covers 4 coordinate positions.")
    gameBoardAfterBSetUp = setUp_VerifyShips(shipUnits, shipLabel, gameBoard)

    return gameBoardAfterBSetUp

def setUpSub(gameBoard):

    shipUnits = 3
    shipLabel = "S"
    print("Next is the Submarine, which covers 3 coordinate positions.")
    gameBoardAfterSSetUp = setUp_VerifyShips(shipUnits, shipLabel, gameBoard)

    return gameBoardAfterSSetUp

def setUpDestroyer(gameBoard):

    shipUnits = 2
    shipLabel = "D"
    print("Last is the Destroyer, which covers 2 coordinate positions.")
    gameBoardAfterDSetUp = setUp_VerifyShips(shipUnits, shipLabel, gameBoard)

    return gameBoardAfterDSetUp
    

def setUp_VerifyShips(shipUnits, shipLabel, gameBoard):
    shipDirection = direction()
    print()
    
    print("Coordinate #1")
    print("This coordinate must either be the left-most position (if ship is horizontal) or upper-most position (if ship is vertical) of the ship.")

    #Verify first coordinate entered using different functions
    firstCoordinate = chooseCoordinates()
    firstR = returnRowLetter(firstCoordinate)
    firstC = returnColNumber(firstCoordinate)
    r = firstR
    c = firstC
    
    prevR = firstR - 1
    prevC = firstC - 1

    otherCoordsEntered = False
    isValidFirstCoordinate = validateCoord(firstR, firstC, r, c, shipDirection, firstCoordinate, shipUnits, shipLabel, otherCoordsEntered, prevR, prevC, gameBoard)

    while isValidFirstCoordinate != True:
        print()
        firstCoordinate = chooseCoordinates()
        firstR = returnRowLetter(firstCoordinate)
        firstC = returnColNumber(firstCoordinate)
        r = firstR
        c = firstC
        
        prevR = firstR - 1
        prevC = firstC - 1
        
        isValidFirstCoordinate = validateCoord(firstR, firstC, r, c, shipDirection, firstCoordinate, shipUnits, shipLabel, otherCoordsEntered, prevR, prevC, gameBoard)
        
    changeGameBoard(firstR, firstC, shipLabel, gameBoard)
    printGameBoard(gameBoard)

    prevR = firstR
    prevC = firstC
    
    #Ask for other coordinates
    for counter in range(2, shipUnits + 1):
        print()
        print("Coordinate #" + str(counter))
        coordinate = chooseCoordinates()
        r = returnRowLetter(coordinate)
        c = returnColNumber(coordinate)

        #Verify other coordinates
        otherCoordsEntered = True
        isValidCoordinate = validateCoord(firstR, firstC, r, c, shipDirection, firstCoordinate, shipUnits, shipLabel, otherCoordsEntered, prevR, prevC, gameBoard)
        while isValidCoordinate != True:
            print()
            coordinate = chooseCoordinates()
            r = returnRowLetter(coordinate)
            c = returnColNumber(coordinate)

            isValidCoordinate = validateCoord(firstR, firstC, r, c, shipDirection, firstCoordinate, shipUnits, shipLabel, otherCoordsEntered, prevR, prevC, gameBoard)

        prevR = r
        prevC = c

        changeGameBoard(r, c, shipLabel, gameBoard)
        printGameBoard(gameBoard)

    return gameBoard
        

def validateCoord(firstR, firstC, r, c, shipDirection, firstCoordinate, shipUnits, shipLabel, otherCoordsEntered, prevR, prevC, gameBoard):
    #Problems this functions should resolve:
    #   make sure ship does not overlap other ship

    #Verifies if ship is horizontal, the coordinate entered is to the right of the coordinate entered before
    if shipDirection.lower() == 'h' and ((c - prevC) != 1):
        print()
        print("INVALID INPUT!")
        print("Make sure the coordinate is one position to the right of", str(chr(prevR + 64)) + str(prevC) )
        return False
    
    #Verifies if ship is vertical, the coordinate entered is one below the coordinate entered before
    if shipDirection.lower() == 'v' and ((r - prevR) != 1):
        print()
        print("INVALID INPUT!")
        print("Make sure the coordinate is one position below", str(chr(prevR + 64)) + str(prevC) )
        return False
    
    #Verifies if other coordinates entered are in line with the first one
    if shipDirection.lower() == 'h' and firstR != r:
        print()
        print("INVALID INPUT!")
        print("Make sure the coordinate is in line with", firstCoordinate)
        return False

    #Verifies if other coordinates entered are in line with the first one
    if shipDirection.lower() == 'v' and firstC != c:
        print()
        print("INVALID INPUT!")
        print("Make sure the coordinate is in line with", firstCoordinate)
        return False

    #Verifies if ship is horizontal, it can not be placed after a certain number
    if shipDirection.lower() == 'h' and firstC >= (10 - (shipUnits - 2)):
        print()
        print("INVALID INPUT!")
        print("The ship will not fit if you place its left most position here!")
        return False

    #Verifies if ship is vertical, it can not be placed after a certain letter
    if shipDirection.lower() == 'v' and ord(str(chr(firstR + 64))) >= ord(str(chr(74 - (shipUnits - 2)))):
        print()
        print("INVALID INPUT!")
        print("The ship will not fit if you place its highest position here!")
        return False

    #Verifies if Battleship is being set up and horizontal, it does not interfere with the placement of other ships
    try:
        if (shipLabel == "B") and (shipDirection.lower() == 'h') and ((gameBoard[firstR][firstC] in 'ADS') or (gameBoard[firstR][firstC + 1] in 'ADS') or
                                                                      (gameBoard[firstR][firstC + 2] in 'ADS') or (gameBoard[firstR][firstC + 3] in 'ADS')): #C:+1,+2,+3
            print()
            print("INVALID INPUT!")
            print("The Battleship will interfere with another ship's positioning if you place it here!")
            return False
    except IndexError:
        pass

    #Verifies if Battleship is being set up and vertical, it does not interfere with the placement of other ships
    try:
        if (shipLabel == "B") and (shipDirection.lower() == 'v') and ((gameBoard[firstR][firstC] in 'ADS') or (gameBoard[firstR + 1][firstC] in 'ADS') or
                                                                      (gameBoard[firstR + 2][firstC] in 'ADS') or (gameBoard[firstR + 3][firstC] in 'ADS')): #R:+1,+2,+3
            print()
            print("INVALID INPUT!")
            print("The Battleship will interfere with another ship's positioning if you place it here!")
            return False
    except IndexError:
        pass

    #Verifies if Submarine is being set up and horizontal, it does not interfere with the placement of other ships
    try:
        if (shipLabel == "S") and (shipDirection.lower() == 'h') and ((gameBoard[firstR][firstC] in 'ADB') or (gameBoard[firstR][firstC + 1] in 'ADB') or
                                                                      (gameBoard[firstR][firstC + 2] in 'ADB')): #C:+1,+2
            print()
            print("INVALID INPUT!")
            print("The Submarine will interfere with another ship's positioning if you place it here!")
            return False       
    except IndexError:
        pass

    #Verifies if Submarine is being set up and vertical, it does not interfere with the placement of other ships    
    try:
        if (shipLabel == "S") and (shipDirection.lower() == 'v') and ((gameBoard[firstR][firstC] in 'ADB') or (gameBoard[firstR + 1][firstC] in 'ADB') or
                                                                      (gameBoard[firstR + 2][firstC] in 'ADB')): #R:+1,+2
            print()
            print("INVALID INPUT!")
            print("The Submarine will interfere with another ship's positioning if you place it here!")
            return False       
    except IndexError:
        pass

    #Verifies if Destroyer is being set up and horizontal, it does not interfere with the placement of other ships
    try:
        if (shipLabel == "D") and (shipDirection.lower() == 'h') and ((gameBoard[firstR][firstC] in 'ABS') or (gameBoard[firstR][firstC + 1] in 'ABS')): #C:+1
            print()
            print("INVALID INPUT!")
            print("The Destroyer will interfere with another ship's positioning if you place it here!")
            return False       
    except IndexError:
        pass

    #Verifies if Destroyer is being set up and vertical, it does not interfere with the placement of other ships    
    try:
        if (shipLabel == "D") and (shipDirection.lower() == 'v') and ((gameBoard[firstR][firstC] in 'ABS') or (gameBoard[firstR + 1][firstC] in 'ABS')): #R:+1
            print()
            print("INVALID INPUT!")
            print("The Destroyer will interfere with another ship's positioning if you place it here!")
            return False       
    except IndexError:
        pass
    
    
    return True
        
def direction():
    
    direction = input("Enter 'v' to place the ship vertically (up-down) or 'h' to place the ship horizontally (left-right): ")

    while (direction.lower() != 'v' and direction.lower() != 'h'):
        print()
        print("INVALID INPUT!")
        direction = input("Please enter 'v' to place the ship vertically (up-down) or 'h' to place it horizontally (left-right): ")
    return direction

def chooseCoordinates():
    letter = input("Enter in the letter of the coordinate position you would like to choose (ex: enter in 'F' if coordinate position was 'F4'): ")
    letter = letter.upper()
    while(letter != 'A' and letter != 'B' and letter != 'C' and letter != 'D' and letter != 'E' and letter != 'F' and letter != 'G'
       and letter != 'H' and letter != 'I' and letter != 'J'):
        print()
        print("INVALID INPUT!")
        letter = input("Please enter in a letter between A-J: ")
        letter = letter.upper()
    
    number = input("Enter in the number of the coordinate position you would like to choose (ex: enter in '4' if coordinate position was 'F4'): ")
    while(number != '1' and number != '2' and number != '3' and number != '4' and number != '5' and number != '6' and number != '7'
       and number != '8' and number != '9' and number != '10'):
        print()
        print("INVALID INPUT!")
        number = input("Please enter in a whole number between 1-10: ")

    print("You entered:", letter + number)
    print()
    return letter + number

def returnRowLetter(coordinate):
    if ('A' in coordinate):
        r = 1
    elif ('B' in coordinate):
        r = 2
    elif ('C' in coordinate):
        r = 3
    elif ('D' in coordinate):
        r = 4
    elif ('E' in coordinate):
        r = 5
    elif ('F' in coordinate):
        r = 6
    elif ('G' in coordinate):
        r = 7
    elif ('H' in coordinate):
        r = 8
    elif ('I' in coordinate):
        r = 9
    elif ('J' in coordinate):
        r = 10
    else:
        print("INVALID LETTER INPUT!")
        r = 0
    return r
        
def returnColNumber(coordinate):
    if ('10' in coordinate):
        c = 10
    elif ('2' in coordinate):
        c = 2
    elif ('3' in coordinate):
        c = 3
    elif ('4' in coordinate):
        c = 4
    elif ('5' in coordinate):
        c = 5
    elif ('6' in coordinate):
        c = 6
    elif ('7' in coordinate):
        c = 7
    elif ('8' in coordinate):
        c = 8
    elif ('9' in coordinate):
        c = 9
    elif ('1' in coordinate):
        c = 1
    else:
        print("INVALID NUMBER INPUT!")
        c = 0
    return c

def changeGameBoard(r, c, label, gameBoard):

    gameBoard[r][c] = label    
    
    return gameBoard

def printGameBoard(gameBoard):
    for r in range(0,11):
        for c in range(0,11):
             print(gameBoard[r][c], end ="      ")
        print()
        print()
        print()

    #print()

#----CPU GAME PLAY FUNCTIONS----
def cpuGamePlay():
    #print()
    #print("                       CPU GameBoard")
    cpuGameBoard = generateCPUGameBoard()
    #printGameBoard(cpuGameBoard)

    return cpuGameBoard

def generateCPUGameBoard():
    #Generate random Pre-defined gameBoard for the CPU
    global x 
    x = random.randint(1, 5)
    #print("", x)

    #Choose Pre-defined gameBoards
    if x == 1:
    
        cpuGameBoard = [['0','1','2','3','4','5','6','7','8','9','10',' ', ' ', ' '],
                       ['A','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['B','.','.','.','.','.','.','.','.','D','.',' ', ' ', ' '],
                       ['C','.','.','S','S','S','.','.','.','D','.',' ', ' ', ' '],
                       ['D','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['E','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['F','A','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['G','A','.','.','.','.','B','B','B','B','.',' ', ' ', ' '],
                       ['H','A','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['I','A','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['J','A','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ', ' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ', ' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ', ' ']]
    elif x == 2:
    
        cpuGameBoard = [['0','1','2','3','4','5','6','7','8','9','10',' ', ' ', ' '],
                       ['A','.','.','.','.','.','.','.','.','.','S',' ', ' ', ' '],
                       ['B','.','.','.','.','.','.','.','.','.','S',' ', ' ', ' '],
                       ['C','.','.','.','.','.','.','.','.','.','S',' ', ' ', ' '],
                       ['D','.','.','A','A','A','A','A','.','.','.',' ', ' ', ' '],
                       ['E','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['F','.','.','D','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['G','.','.','D','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['H','.','.','B','B','B','B','.','.','.','.',' ', ' ', ' '],
                       ['I','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['J','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ', ' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ', ' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ', ' ']]
    if x == 3:
    
        cpuGameBoard = [['0','1','2','3','4','5','6','7','8','9','10',' ', ' ', ' '],
                       ['A','.','.','.','A','A','A','A','A','.','.',' ', ' ', ' '],
                       ['B','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['C','S','S','S','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['D','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['E','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['F','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['G','.','.','.','.','B','.','.','.','.','.',' ', ' ', ' '],
                       ['H','.','.','.','.','B','.','.','.','.','.',' ', ' ', ' '],
                       ['I','.','D','.','.','B','.','.','.','.','.',' ', ' ', ' '],
                       ['J','.','D','.','.','B','.','.','.','.','.',' ', ' ', ' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ', ' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ', ' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ', ' ']]
    elif x == 4:
    
        cpuGameBoard = [['0','1','2','3','4','5','6','7','8','9','10',' ', ' ', ' '],
                       ['A','B','B','B','B','S','S','S','.','.','.',' ', ' ', ' '],
                       ['B','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['C','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['D','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['E','D','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['F','D','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['G','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['H','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['I','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['J','.','.','.','A','A','A','A','A','.','.',' ', ' ', ' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ', ' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ', ' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ', ' ']]
    elif x == 5:
    
        cpuGameBoard = [['0','1','2','3','4','5','6','7','8','9','10',' ', ' ', ' '],
                       ['A','D','D','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['B','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['C','.','.','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['D','.','.','.','.','A','.','.','.','.','.',' ', ' ', ' '],
                       ['E','.','.','.','.','A','.','.','.','.','.',' ', ' ', ' '],
                       ['F','.','.','.','.','A','.','.','.','.','.',' ', ' ', ' '],
                       ['G','.','.','.','.','A','.','.','.','.','.',' ', ' ', ' '],
                       ['H','.','S','.','.','A','.','.','.','.','.',' ', ' ', ' '],
                       ['I','.','S','.','.','.','.','.','.','.','.',' ', ' ', ' '],
                       ['J','.','S','.','.','.','.','B','B','B','B',' ', ' ', ' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ', ' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ', ' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ', ' ']]

    return cpuGameBoard

def cpuGuess(userGameBoard):
    print()

    cpuTurn = True
    while cpuTurn:
        coordinate = chooseCPUCoordinates()
        r = returnRowLetter(coordinate)
        c = returnColNumber(coordinate)
        #print("The CPU guesses:", coordinate)
        #print()
    
        while((userGameBoard[r][c] in 'H') or (userGameBoard[r][c] in '#') or (userGameBoard[r][c] in 'X')):
            #print("The CPU already guessed this coordinate before!")
            #print("The CPU will guess again.")
            #print()
            coordinate = chooseCPUCoordinates()
            r = returnRowLetter(coordinate)
            c = returnColNumber(coordinate)

        print("The CPU guesses:", coordinate)
        print()
            
        while(userGameBoard[r][c] in 'ABDS'):

            global userShipUnits
            userShipUnits -= 1

            if userGameBoard[r][c] in 'A':
                global userAircraftCarrier
                userAircraftCarrier -= 1

                userGameBoard[r][c] = 'H'
                printGameBoard(userGameBoard)
                print("HIT!")
                print()
                

                if userAircraftCarrier == 0:
                    print("The CPU destroyed your Aircraft Carrier!")
                    print()
    
            if userGameBoard[r][c] in 'B':
                global userBattleship
                userBattleship -= 1

                userGameBoard[r][c] = 'H'
                printGameBoard(userGameBoard)
                print("HIT!")
                print()

                if userBattleship == 0:
                    print("The CPU destroyed your Battleship!")
                    print()
                
            if userGameBoard[r][c] in 'S':
                global userSub
                userSub -= 1

                userGameBoard[r][c] = 'H'
                printGameBoard(userGameBoard)
                print()
                print("HIT!")
                print()

                if userSub == 0:
                    print("The CPU destroyed your Submarine!")
                    print()

            if userGameBoard[r][c] in 'D':
                global userDestroyer
                userDestroyer -= 1
                
                userGameBoard[r][c] = 'H'
                printGameBoard(userGameBoard)
                print("HIT!")
                print()

                if userDestroyer == 0:
                    print("The CPU destroyed your Destroyer!")
                    print()
                        
            if userShipUnits == 0:
                print("The CPU destroyed all your ships!")
                userTurn = False
                print()

                return userGameBoard

            hitEnter = input("Press 'Enter' to continue: ")
            print()
            print("The CPU will choose another coordinate to attack again!")
            print()
            coordinate = chooseCPUCoordinates()
            r = returnRowLetter(coordinate)
            c = returnColNumber(coordinate)

            while((userGameBoard[r][c] in 'H') or (userGameBoard[r][c] in '#') or (userGameBoard[r][c] in 'X')):
                coordinate = chooseCPUCoordinates()
                r = returnRowLetter(coordinate)
                c = returnColNumber(coordinate)

            print("The CPU guesses:", coordinate)
            print()
            

        userGameBoard[r][c] = 'X'
        printGameBoard(userGameBoard)                
        print("Miss")
        print()
        enter = input("Press 'Enter' to continue: ")
        print()
        print("                                 Your Turn")

        cpuTurn = False

    return userGameBoard

def chooseCPUCoordinates():
        #CPU Generates Letter
        r = random.randint(1, 10)

        if r == 1:
            letter = 'A'
        elif r == 2:
            letter = 'B'
        elif r == 3:
            letter = 'C'
        elif r == 4:
            letter = 'D'
        elif r == 5:
            letter = 'E'
        elif r == 6:
            letter = 'F'
        elif r == 7:
            letter = 'G'
        elif r == 8:
            letter = 'H'
        elif r == 9:
            letter = 'I'
        elif r == 10:
            letter = 'J'
        else:
            print("INVALID CPU LETTER INPUT!")
            letter = 'O'

        #CPU Generates Number
        number = random.randint(1, 10)

        return letter + str(number)
        
main()


    


