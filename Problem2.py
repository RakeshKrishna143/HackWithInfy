row = int(input())
maze = []
for i in range(row):
    maze.append(input())
k = int(input())
col = len(maze[0])

def isSafe(maze,x,y):
    if 0<=x<row and 0<=y<col and maze[x][y]=='.':
        return True
    return False

def solmaze(maze,x,y):
    if x==row-1 and y==col-1:
        return True
    if isSafe(maze,x,y):
        if solmaze(maze, x+1, y):
            return True
        if solmaze(maze, x, y+1):
            return True
        return False

def solution(maze,row,col,k):
    if not(solmaze(maze,0,0)):
        return 'Better luck next time'
    if k>=row+col-2:
        return 'Fahad wins'
    return 'Better luck next time'



print(solution(maze,row,col,k))

'''
Fahad is taking part in a maze competition .
Initially, Fahad will stand in the top-left corner of the maze, the maze is a 2-D grid consisting of some blocked (represented as " # " ) and unblocked (represent represented as " . ") cell. 
It is guaranteed that is standing in an unblock cell. 
It is also guarantee that the bottom right corner is unblocked.
Each cell of is connected with its left, right, bottom and top cells if those cells exist. 
It takes 1 second to move from a cell to its adjacent cell. 
If he can reach the bottom right corner of the maze within 'k' seconds he can win
if he can return the string 'Fahad wins' otherwise return the string "better luck next time".
'''
