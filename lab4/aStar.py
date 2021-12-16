import math
def print_grid(src):#print the grid
    state = src.copy()
    state[state.index(-1)] = ' '
    print(
        f"""
{state[0]} {state[1]} {state[2]}
{state[3]} {state[4]} {state[5]}
{state[6]} {state[7]} {state[8]}
        """
    )

def manhattan(state,target):
    dist=0
    for i in state:
        d1,d2=state.index(-1),target.index(-1)
        x1,y1=d1%3,d1//3
        x2,y2=d2%3,d2//3
        dist+=abs(x2-x1)+abs(y2-y1)
    return dist

def astar(src, target):#a* algo
    states = [src]
    g = 0
    visited_states = set()
    while len(states):
        print(f"Level: {g}")
        moves = []
        for state in states:
            visited_states.add(tuple(state))
            print_grid(state)
            if state == target:
                print("Success")
                return
            moves += [move for move in possibleMoves(state, visited_states) if move not in moves]
        costs = [g + manhattan(move, target) for move in moves]#fn=gn+hn
        states = [moves[i] for i in range(len(moves)) if costs[i] == min(costs)]#min cost
        g += 1
    print("Fail")


def possibleMoves(state,visited):
    index=state.index(-1)
    moves=[]
    if index+3 in range(9):
        moves.append('d')
    if index-3 in range(9):
        moves.append('u')
    if index not in [0,3,6]:
        moves.append('l')
    if index not in [2,5,8]:
        moves.append('r')
    
    possMoves=[]
    for move in moves:
        possMoves.append(generate(move,state,index))
    
    return [move for move in possMoves if tuple(move) not in visited]


def generate(move,state,b):
    temp=state.copy()
    if move == 'u':
        temp[b-3], temp[b] = temp[b], temp[b-3]
    if move == 'd':
        temp[b+3], temp[b] = temp[b], temp[b+3]
    if move == 'r':
        temp[b+1], temp[b] = temp[b], temp[b+1]
    if move == 'l':
        temp[b-1], temp[b] = temp[b], temp[b-1]
    return temp
    
    


src=[1,2,3,-1,4,5,6,7,8]
target=[1,2,3,4,5,-1,6,7,8]
astar(src,target)

