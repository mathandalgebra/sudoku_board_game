
import copy


def nondestructiveRemoveRowAndCol(lst, row, col):
    usableList = copy.deepcopy(lst)
    newList = []
    for i in range(len(usableList)):
        if(i != row):
            currentRow = []
            for j in range(len(usableList[0])):
                if(j != col):
                    currentRow = currentRow + [usableList[i][j]]
            newList = newList + [currentRow]
    return newList

def destructiveRemoveRowAndCol(lst, row, col):
    if(len(lst) == 1):
        lst = []
    for i in range(len(lst)-1):
        if(i == row):
            lst.pop(i)
        for j in range(len(lst[i])):
            if(j == col):
                lst[i].pop(j)
                break
    return None
                
        

def wordSearchWithWildcards(board, word):
    (rows, cols) = (len(board), len(board[0]))
    for row in range(rows):
        for col in range(cols):
            result = wordSearchFromCell(board, word, row, col)
            if (result != False):
                return True
    return False

def wordSearchFromCell(board, word, startRow, startCol):
    for drow in [-1, 0, +1]:
        for dcol in [-1, 0, +1]:
            if ((drow != 0) or (dcol != 0)):
                result = wordSearchFromCellInDirection(board, word,
                                                       startRow, startCol,
                                                       drow, dcol)
                if (result != False):
                    return result
    return False

def wordSearchFromCellInDirection(board, word, startRow, startCol, drow, dcol):
    (rows, cols) = (len(board), len(board[0]))
    dirNames = [ ["up-left"  ,   "up", "up-right"],
                 ["left"     ,   ""  , "right"   ],
                 ["down-left", "down", "down-right" ] ]
    i = 0
    iWord = 0
    
    while(iWord < len(word)):
        
        row = startRow + i*drow
        col = startCol + i*dcol
        if ((row < 0) or (row >= rows) or
            (col < 0) or (col >= cols)):
            return False
        
            
        if(str(board[row][col]).isdigit() == True):
            number = int(str(board[row][col]))
            if(number == len(word)):
                return True
            iWord = iWord + number
            if(iWord == len(word)):
                return True
            i = i + 1
            if ((row + drow < 0) or (row + drow >= rows) or
            (col + dcol < 0) or (col + dcol >= cols)):
                return False
            if(iWord >= len(word)):
                return False
            if(board[row + drow][col + dcol] != word[iWord]):
                return False 

        if(str(board[row][col]).islower() == True):
            if(board[row][col] != word[iWord]):
                return False 
            iWord = iWord + 1
            i = i + 1
        
    return (word, (startRow, startCol), dirNames[drow+1][dcol+1])
    
def testWordSearch():
    board = [[ 'p', 'i', 'g' ],
              [ 's',  2, 'c' ],
              [ 'r',  7, 'd' ]]
    assert(wordSearchWithWildcards(board, "cows") == True)
    assert(wordSearchWithWildcards(board,"coowws") == False)
    assert(wordSearchWithWildcards(board,"dogs") == False)
    assert(wordSearchWithWildcards(board,"roads") == False)
    assert(wordSearchWithWildcards(board,"cow") == True)
    board1 = [['d', 'o', 1], 
              [3, 'a', 'c'], 
              ['o', 'q', 't']]
    assert(wordSearchWithWildcards(board1,"dog") == True)
    assert(wordSearchWithWildcards(board1,"z") == True)
    print("pass")
    

def perfectSquare(num):
    root = num ** (1/2)
    if(int(root + 0.5) ** 2) == num:
        return True
    else: 
        return False
        
def areLegalValues(list):
    if(len(list)==0):
        return False
    for index in range(len(list)):
        if(str(list[index]).isdigit() == False):
            return False
        if(perfectSquare(len(list)) == False):
            return False 
        if(list[index] < 0 or list[index] > ((len(list)))):
            return False
        if(list[index] == 0):
            continue
        if(list.count(list[index]) > 1):
            return False
    return True

def isLegalRow(board, row):
    if(areLegalValues(board[row]) == False):
            return False
    return True

def isLegalCol(board, col):
    newList = []
    for i in range(len(board)):
        newList = newList + [board[i][col]]
    if(areLegalValues(newList) == False):
        return False
    return True

def isLegalBlock(board, block):
    bRowNum = int(len(board)**(1/2))
    bColNum = int(len(board)**(1/2))
    rowAdvancement = block // bRowNum
    colAdvancement = block % bColNum
    bList = []
    for i in range(bRowNum *rowAdvancement, bRowNum * (rowAdvancement + 1)):
        for j in range(bColNum * colAdvancement, bColNum * (colAdvancement + 1)):
            bList = bList + [board[i][j]]
    if(areLegalValues(bList) == False):
        return False
    return True
            

def isLegalSudoku(board):
    for row in range(len(board)):
        if(isLegalRow(board,row) == False):
            return False
    for col in range(len(board[0])):
        if(isLegalCol(board,col) == False):
            return False
    for block in range(len(board)):
        if(isLegalBlock(board,block) == False):
            return False
    return True
            



from tkinter import *



def init(data):
    data.board = [
  [ 1, 2, 3, 4, 5, 6, 7, 8, 9],
  [ 5, 0, 8, 1, 3, 9, 6, 2, 4],
  [ 4, 9, 6, 8, 7, 2, 1, 5, 3],
  [ 9, 5, 2, 3, 8, 1, 4, 6, 7],
  [ 6, 4, 1, 2, 9, 7, 8, 3, 5],
  [ 3, 8, 7, 5, 6, 4, 0, 9, 1],
  [ 7, 1, 9, 6, 2, 3, 5, 4, 8],
  [ 8, 6, 4, 9, 1, 5, 3, 7, 2],
  [ 2, 3, 5, 7, 4, 8, 9, 1, 6]
]
    cellWidth = data.width//len(data.board[0])
    cellHeight = data.height//len(data.board)
    data.cellSize = min(cellWidth,cellHeight)

    data.currentRow = 0
    data.currentCol = 0
    data.currentNum = ""

def drawBoard(canvas, data):
    for row in range(len(data.board)):
        for col in range(len(data.board[row])):
            left = col * data.cellSize
            top = row * data.cellSize
            canvas.create_rectangle(left,top,left + data.cellSize,top + data.cellSize)
    
    thickLineIncrement = int(len(data.board) ** (1/2))
    
    for row in range(0,len(data.board) + 1,thickLineIncrement):
        left = col * data.cellSize
        top = row * data.cellSize
        canvas.create_line(0,top,data.width,top,width = 5)
    
    for col in range(0,len(data.board) + 1, thickLineIncrement):
        left = col * data.cellSize
        top = row * data.cellSize
        canvas.create_line(left,0,left,data.height,width = 5)
    
    canvas.create_rectangle(data.currentCol * data.cellSize,data.currentRow * data.cellSize,data.currentCol * data.cellSize + data.cellSize,data.currentRow * data.cellSize + data.cellSize,fill = "yellow")
        
    for row in range(len(data.board)):
        for col in range(len(data.board)):
            left = col * data.cellSize
            top = row * data.cellSize
            if(data.board[row][col] != 0):
                canvas.create_text(left + data.cellSize / 2, top + data.cellSize / 2,
                                   text = str(data.board[row][col]),font = "Times 28 bold italic")
                        
    if(success(data.board) == True):
        canvas.create_text(data.width/2,data.height/2, text = "win", font = "Arial 40 bold")        
    
def mousePressed(event, data):
    pass

def keyPressed(event, data):
    if event.keysym == "Up":
        data.currentRow = (data.currentRow - 1) % len(data.board)
    elif event.keysym == "Down":
        data.currentRow = (data.currentRow + 1) % len(data.board)
    elif event.keysym == "Left":
        data.currentCol = (data.currentCol - 1) % len(data.board)
    elif event.keysym == "Right":
        data.currentCol = (data.currentCol + 1) % len(data.board)
    elif event.keysym == "BackSpace":
        data.board[data.currentRow][data.currentCol] = 0
        
    # data.currentNum = ""
    # data.keysymText = event.keysym
    
    if(event.keysym.isdigit() == True):
        data.currentNum = event.keysym
        data.currentNum = int(data.currentNum)
        if(data.board[data.currentRow][data.currentCol] == 0):
            data.board[data.currentRow][data.currentCol] = data.currentNum
        # if(isLegalSudoku(data.board) == False):
        #     data.board[data.currentRow][data.currentCol] = 0
    
   #  

def success(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j] == 0):
                return False
    if(isLegalSudoku(board) == True):
        return True
        
def redrawAll(canvas, data):
    drawBoard(canvas,data)
    pass

def runSudoku(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed


def testNondestructiveRemoveRowAndCol():
 
    
    print("Write your own tests for nondestructiveRemoveRowAndCol!")

def testDestructiveRemoveRowAndCol():

    
    print("Write your own tests for destructiveRemoveRowAndCol!")

def testWordSearchWithWildcards():
    board = [ [ 'p', 'i', 'g' ],
          [ 's',   2, 'c' ],
          [ 'r',   7, 'd' ] ]
    assert(wordSearchWithWildcards(board, "cows") == True)
    assert(wordSearchWithWildcards(board, "pig") == True)
    assert(wordSearchWithWildcards(board, "road") == False)
    assert(wordSearchWithWildcards(board, "class") == False)
    assert(wordSearchWithWildcards(board, "be") == True)
    print("Write your own tests for wordSearchWithWildcards!")

def testAreLegalValues():
    assert(areLegalValues([1,4,2,3])==True)
    assert(areLegalValues([1,5,2,3])==False)
    assert(areLegalValues([1,2,2,3])==False)
    print("pass")
    print("Write your own tests for areLegalValues!")

def testIsLegalRow():
    assert(isLegalRow([[ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 5, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]],1)==False)
    
    print("Write your own tests for isLegalRow!")
    assert(isLegalRow([[ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 5, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]],2)==True)
    print("pass")
def testIsLegalCol():
    assert(isLegalCol([[ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
    [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
    [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
    [ 8, 0, 11, 0, 6, 0, 0, 0, 3 ],
    [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
    [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
    [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
    [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
    [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]],2) == False)
    assert(isLegalCol([[ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
    [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
    [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
    [ 8, 0, 9, 0, 6, 0, 0, 0, 3 ],
    [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
    [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
    [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
    [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
    [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]],2) == True)
    print("pass")
    print("Write your own tests for isLegalCol!")

def testIsLegalBlock():
    assert(isLegalBlock([[ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
    [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
    [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
    [ 8, 0, 9, 0, 6, 0, 0, 0, 3 ],
    [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
    [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
    [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
    [ 0, 0, 0, 4, 1, 9, 0, 5, 5 ],
    [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]],8) == False)
    print("pass")
    print("Write your own tests for isLegalBlock!")

def testIsLegalSudoku():
    assert(isLegalSudoku([[ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 5, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]])==False)
    assert(isLegalSudoku([[ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 7, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]])==True)

    print("Write your own tests for isLegalSudoku!")

def testSudokuAnimation():
    print("Running Sudoku Animation...", end="")
    # Feel free to change the width and height!
    width = 500
    height = 500
    runSudoku(width, height)
    print("Done!")

def testSokobanAnimation():
    print("Running Sokoban Animation...", end="")
    # Feel free to change the width and height!
    width = 500
    height = 500
    runSokoban(width, height)
    print("Done!")


def testAll():
    testNondestructiveRemoveRowAndCol()
    testDestructiveRemoveRowAndCol()
    testWordSearchWithWildcards()
    testAreLegalValues()
    testIsLegalRow()
    testIsLegalCol()
    testIsLegalBlock()
    testIsLegalSudoku()
    testSudokuAnimation()
  

def main():
    testAll()

if __name__ == '__main__':
    main()