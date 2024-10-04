import time


# game table as a coordinate system
table = {
    '1': {'1': ' ', '2': ' ', '3': ' ','4': ' ','5': ' ','6': ' ','7': ' '},
    '2': {'1': ' ', '2': ' ', '3': ' ','4': ' ','5': ' ','6': ' ','7': ' '},
    '3': {'1': ' ', '2': ' ', '3': ' ','4': ' ','5': ' ','6': ' ','7': ' '},
    '4': {'1': ' ', '2': ' ', '3': ' ','4': ' ','5': ' ','6': ' ','7': ' '},
    '5': {'1': ' ', '2': ' ', '3': ' ','4': ' ','5': ' ','6': ' ','7': ' '},
    '6': {'1': ' ', '2': ' ', '3': ' ','4': ' ','5': ' ','6': ' ','7': ' '},
}
possibleInputValues=['1','2','3','4','5','6','7','x','X']
rows=6

# all possible diagonal path (that contains minimum 4 diagonal positions of the table) coordinates
diagonalStartCoordinates=[[4,1],[5,1],[6,1],[6,2],[6,3],[6,4],[3,1],[2,1],[1,1],[1,2],[1,3],[1,4]]
diagonalEndCoordinates=[[1,4],[1,5],[1,6],[1,7],[2,7],[3,7],[6,4],[6,5],[6,6],[6,7],[5,7],[4,7]]
noOfCoordinates=len(diagonalStartCoordinates)

player='RED' # RED player starts the game
steps=0

# colors
RED = "\033[1;91m"
GREEN= "\033[1;32;40m"
BACKG="\33[1;31;41m"
RESET = "\033[0m"

# player forms
PLAYER1='\033[1;91m\u25CF\033[0m'
PLAYER2='\u25CF'


def printTable():
    print('    1 2 3 4 5 6 7 ')
    print('   ---------------')
    for row in table:
        print(row,'|', end=" ")
        for column in table[row]:
            if (table[row][column]=='R'):
                 print(f"{RED}{table[row][column]}{RESET}", end=" ")
            else:
                print(table[row][column], end=" ")
        print('|')
    print('   ---------------')


## check free place in column 
def checkColumn(col,player):
    for row in range(rows,0,-1):
        rowStr=str(row)
        if (table[rowStr][col]==' '):
            if (player)=='RED':
                table[rowStr][col]=PLAYER1
            else:
                table[rowStr][col]=PLAYER2
            break

def checkWinner():
    redWin=PLAYER1+PLAYER1+PLAYER1+PLAYER1
    whiteWin=PLAYER2+PLAYER2+PLAYER2+PLAYER2

    ## check horizontal match
    for row in table:
        for column in range(1,3):
            rowMask=table[row][str(column)]+table[row][str(column+1)]+table[row][str(column+2)]+table[row][str(column+3)]
            if (rowMask==redWin or rowMask==whiteWin):
                return True
    
    ## check vertical match 
    for column in table['1']:
        columnValues=''
        for row in table:
            columnValues=columnValues+table[row][column]
        if (redWin in columnValues or whiteWin in columnValues):
                return True
 

    ## check diagonal match
    index=0
    while index<noOfCoordinates: # every diagonal path is examined
        xStart=diagonalStartCoordinates[index][0]
        yStart=diagonalStartCoordinates[index][1]
        x=xStart
        y=yStart
        xEnd=diagonalEndCoordinates[index][0]
        index+=1
        diagonalValues='' # to store the value of the specified table coordinates
        while True:
            if (table[str(x)][str(y)])!=' ':
                diagonalValues=diagonalValues+table[str(x)][str(y)]
                if (redWin in diagonalValues or whiteWin in diagonalValues):
                    return True
            if (xStart>xEnd): 
                x-=1
                y+=1
            else:
                x+=1
                y+=1
            if (xStart>xEnd and x<xEnd) or (xStart<xEnd and x>xEnd):
                break
    return False

print(f'{BACKG}---- Connect 4 game for two players ----{RESET}')
print()
printTable()

def gameOver():
    print()
    print(f'{BACKG}---- GAME OVER ----{RESET}')
    if selectedValue!='x':
        if (steps<20):
            print(f'Congratulation! You have finished the game after {steps} steps.')
        else:
            print(f'Not bad at all, but you need to practice more!')
        print('-- I hope you enjoyed it. See you next time!')
    else:
        print('-- You exited from the game! See you next time!')

# main code
while (True):
    while (True):
        text=f"{GREEN}{player} player turn. {RESET}Please enter the column number or press {GREEN}'x'{RESET} to exit:"
        if (player=='RED'):
            text=f"{GREEN}{player} player turn. {RESET}Please enter the column number or press {GREEN}'x'{RESET} to exit:  "
        selectedValue=input(text)
        
        if selectedValue in possibleInputValues:
            break
        else:
            print("\033[A", end="")
            print('Please enter a valid column number!                                                                                    ')
            print("\033[A", end="")
            time.sleep(1)
            continue
   
    steps+=1

    if (selectedValue in ['x','X']):
        gameOver()
        break

    if (table['1'][selectedValue]==' '):
        checkColumn(selectedValue,player)

        # players change - next player
        if (player=='RED'):
            player='WHITE'
        else:
            player='RED'
        if selectedValue==' ':
            break
    else:
        print("\033[A", end="")
        print('You cannot place more in this column!                                                   ')
        time.sleep(1)
    
    # cursor back to the original position
    for back in range(1,11): 
        print("\033[A", end="")
       
    printTable()
    isWinner=checkWinner()
    if (isWinner):
        if(player=='RED'):
            print('WHITE player won the game!')
        else:
            print('RED player won the game!')
        gameOver()
        break
