def displayBoard(board):
    print('     |   |')
    print('   '+board[0]+' | '+board[1]+' |  '+board[2]+'  ')
    print('     |   |')
    print(' ______________')
    print('     |   |')
    print('   '+board[3]+' | '+board[4]+' |  '+board[5]+'  ')
    print('     |   |')
    print(' ______________')
    print('     |   |')
    print('   '+board[6]+' | '+board[7]+' |  '+board[8]+'  ')
    print('     |   |\n')

def checkWin(board,playerMark):
    return(
        (board[0]==board[1]==board[2]==playerMark)or
        (board[3]==board[4]==board[5]==playerMark)or
        (board[6]==board[7]==board[8]==playerMark)or
        (board[0]==board[3]==board[6]==playerMark)or
        (board[1]==board[4]==board[7]==playerMark)or
        (board[2]==board[5]==board[8]==playerMark)or
        (board[0]==board[4]==board[8]==playerMark)or
        (board[2]==board[4]==board[6]==playerMark)
    )

def checkDraw(board):
    return(' ' not in board)

def copyBoard(board):
    dupBoard=[]
    for i in board:
        dupBoard.append(i)
    return dupBoard

def testWinMove(board,playerMark,move):
    boardCopy=copyBoard(board)
    boardCopy[move]=playerMark
    return checkWin(board,playerMark)

def winStrategy(board):
    for i in [0,2,6,8]:
        if board[i]==' ':
            return i
    
    if board[4]==' ':
        return 4
    
    for i in [1,3,5,7]:
        if board[i]==' ':
            return i

def forkMove(board,playerMark,move):
    boardCopy=copyBoard(board)
    boardCopy[move]=playerMark
    winningMoves=0
    for i in range(0,9):
        if testWinMove(board,playerMark,i) and boardCopy[i]==' ':
            winningMoves+=1
    return winningMoves>=2

def getAgentMove(board):    
    for i in range(0,9):
        if board[i]==' ' and testWinMove(board,'X',i):
            return i

    for i in range(0,9):
        if board[i]==' ' and testWinMove(board,'O',i):
            return i
    
    for i in range(0,9):
        if board[i]==' ' and forkMove(board,'X',i):
            return i
    
    for i in range(0,9):
        if board[i]==' ' and forkMove(board,'O',i):
            return i

    return winStrategy(board)


def tictactoe():
    playing=True
    while playing:
        inGame=True
        board=[' ']*9
        playerNext=False
        agentNext=False
        print("Would you like to go first or second?:(1/2)")
        if input()=='1':
            playerMark='O'
            playerNext=True
            agentMark='X'
        else :
            playerMark='X'
            agentNext=True
            agentMark='O'

        displayBoard(board)
        

        while inGame:
            # if playerMark=='O':
            if playerNext:
                print("Enter the board position:(0-8)")
                move=int(input())
                if board[move]!=' ':
                    print("Invalid move")
                else:
                    board[move]=playerMark
            
            else:
                move=getAgentMove(board)
                board[move]=agentMark
            
            
            

            if checkWin(board,playerMark):
                inGame=False
                displayBoard(board)
                print("Player won!")
                continue

            if checkWin(board,agentMark):
                inGame=False
                displayBoard(board)
                print("Agent won!")
                continue

            if checkDraw(board):
                inGame=False
                displayBoard(board)
                print("Its a draw!")
                continue
            
            displayBoard(board)
            
            if playerNext:
                playerNext=False
                agentNext=True
            else:
                agentNext=False
                playerNext=True
            
        print("Type y to continue playing")
        inp=input()
        if inp!='y' and inp!='Y':
            playing=False


tictactoe()
