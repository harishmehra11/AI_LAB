import math

floor=[[1,0,0,1,0],
       [0,0,0,1,1],
       [1,1,1,0,0],
       [0,0,0,1,1],
       [1,1,1,1,1]]

def printFloor(floor):
    row=len(floor)
    col=len(floor[0])
    for i in range(row):
        for j in range(col):
            print(floor[i][j],end=" ")
        print()

def cleanFloor(floor):
    row=len(floor)
    col=len(floor)
    for i in range(row):
        if i%2==0:
            for j in range(col):
                if(floor[i][j]==1):
                    print("dirty status!")
                    printFloor(floor) 
                    floor[i][j]=0
                else:
                    print("clean status!")
                    printFloor(floor)
                print()
        else:
            for j in range(col-1,-1,-1):
                if(floor[i][j]==1):
                    print("dirty status!")
                    printFloor(floor) 
                    floor[i][j]=0
                else:
                    print("clean status!")
                    printFloor(floor)
                print()

cleanFloor(floor)
printFloor(floor)