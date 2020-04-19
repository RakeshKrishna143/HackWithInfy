row = int(input())
maze = []
for i in range(row):
    maze.append(input())
k = int(input())
col = len(maze[0])

def printsol(sol):
    count = 0
    for i in sol:
        for j in i:
            if j==1:
                count+=1
            print(str(j)+" ",end="")
        print()
    return count
def issafe(maze,x,y):
    if 0<=x<row and 0<=y<col and maze[x][y]=='.':
        return True
    return False
def solmaze(maze,x,y,sol,d):
    if x==row-1 and y==col-1 :
        sol[x][y]=1 
        return True
    if issafe(maze,x,y):
        sol[x][y]=1 
        if d!='up' and solmaze(maze,x+1,y,sol,'down'):#down
            return True
        if d!='left' and solmaze(maze,x,y+1,sol,'right'):#right
            return True  
        if d!='down' and solmaze(maze,x-1,y,sol,'up'):#up
            return True
        if d!='right' and solmaze(maze,x,y-1,sol,'left'):#left
            return True  
        
        sol[x][y]=0
        return False
def solution(maze,row,col,k):
    sol=[[0 for j in range(col)]for i in range(row)]
    if not(solmaze(maze,0,0,sol,'down')):
        return 'Better luck next time'
    res = printsol(sol)
    if k>=res-1:
        return 'Fahad wins'
    return 'Better luck next time'

print(solution(maze,row,col,k))

'''
.....
#.##.
.....
..###
.....
'''
