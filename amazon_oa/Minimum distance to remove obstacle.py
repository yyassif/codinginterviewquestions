'''Question Amazon | OA 2019 | Minimum distance to remove obstacle
You are in charge of preparing a recently purchased lot for Amazon’s building.
 The lot is covered with trenches and has a single obstacle that needs to be taken down
  before the foundation is prepared for the building. The demolition robot must remove
  the obstacle before the progress can be made on the building. Write an algorithm
  to determine the minimum distance required for the demolition robot to remove the obstacle
  1 is path and 9 is the obstacle set on its path.
  * I assume the path starts at lot[0][0]
'''
def remove_obstacle(lot):
    nr = len(lot)
    if nr==0:
        return -1
    nc = len(lot[0])
    if nc==0:
        return -1
    q=[]
    def valid(a,b):
        if 0<=a<nr and 0<=b<nc and lot[a][b]==1 or lot[a][b]==9:
            return True
        return False

    q.append((0,0,0))
    lot[0][0] = 2
    cnt=0

    while q:
        i,j,cnt = q.pop(0)
        print(i,j,cnt)
        if lot[i][j - 1] == 9:
            cnt += 1
            return cnt
        if valid(i,j-1):
            if lot[i][j-1]==9:
                cnt+=1
                return cnt
            lot[i][j-1]=2 #mark as visited
            q.append((i,j-1,cnt+1))
        if valid(i,j+1):
            if lot[i][j+1]==9:
                cnt+=1
                return cnt
            lot[i][j + 1] = 2
            q.append((i,j+1,cnt+1))
        if valid(i-1,j):
            if lot[i-1][j]==9:
                cnt+=1
                return cnt
            lot[i-1][j] = 2
            q.append((i-1,j,cnt+1))
        if valid(i+1,j):
            if lot[i+1][j]==9:
                cnt+=1
                return cnt
            lot[i + 1][j] = 2
            q.append((i+1,j,cnt+1))
    return -1
#Test Cases
lot = [
[1, 0, 0, 0],
[1, 0, 0, 0],
[1, 0, 0, 0],
[1, 9, 1, 1]
]
moves = remove_obstacle(lot)
print(lot)
print("min dist:",moves)

lot = [
[1, 0, 0, 0],
[1, 1, 0, 0],
[0, 1, 0, 0],
[0, 9, 1, 1]
]
moves = remove_obstacle(lot)
print(lot)
print("min dist:",moves)
