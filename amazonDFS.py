def amazonDFS(B, n, e, row, placed):
    # B is a vector such that B[i] = the col number in which the amazon is placed in row i
    # n is the dimension of the board for which a solution is sought
    # pre-condition: B is a valid partial solution
    e += 1
    if count(B) == n:   # solved
        print(B, e-1)
        return True

    for j in range(n): #cols
        # looking for a candidate for B[k] which will be an integer from 0 to n-1
        if not(attack(B, n, j, row)):
            #B.append(j)
            if not placed[row]:#we dont want to change/remove preplaced amazons so we skip
              B[row] = j

            if amazonDFS(B, n, e, row + 1, placed):
                return True
            else:
              #B.remove(j)
              if not placed[row]:#we dont want to change/remove preplaced amazons so we skip
                B[row] = -1
    #print(B, e)
    return False
    

def attack(B, n, j, row):
    #checks if the cell B[k+1, j] is under attack by the amazons in the first k rows of B
    rowNum = row+1
    for k in range(n): # column attack
        if B[k] == j and B[k] != -1:
            return True
    for i in range(rowNum):#diagonal attack
      if (B[row - i] != -1) and (B[row - i] == j - i or B[row - i] == j + i):
        return True
    for i in range(n-row):
      if (B[row + i] != -1) and (B[row + i] == j - i or B[row + i] == j + i):
        return True


#adds knights movement
    index = rowNum - 1
    if (index > 0): #out of bounce fix
      #checks row-1 col-2/+2
      if (B[index - 1] != -1) and ( B[index - 1] == j - 2 or B[index - 1] == j + 2 ):
        return True

    if (index > 1):#out of bounce fix
      #checks row-2 col-1/+1
      if (B[index - 2] != -1) and ( B[index - 2] == j - 1 or B[index - 2] == j + 1 ):
        return True

      #checks row+1 col-2/+2
    if (index < n-1):
      if (B[index + 1] != -1) and ( B[index + 1] == j - 2 or B[index + 1] == j + 2 ):
        return True
      #checks row+2 col-1/+1
    if (index < n-2):
      if (B[index + 2] != -1) and ( B[index + 2] == j - 1 or B[index + 2] == j + 1 ):
        return True
    
    return False

def count(B):#count how many amazons on placed
    amazons = 0
    for i in B:
      if i != -1:
        amazons += 1
    return amazons
        
def preplacedAmazons(B):#save the index of preplaced amazons
    pa = []
    for i in B:
      if i != -1:
        pa.append(True)
      else:
        pa.append(False)
    return pa

def main():
#It returns a board by adding as many additional amazons as possible, 
#return True (False) if it could find a solution with additional n − k amazons, 
#the number of nodes expanded by DFS.
    B = input("Enter a board as a vector B in f:")
    B = B.strip("[]").split(",")
    for i in range(len(B)):
        B[i] = int(B[i])

    N = len(B)
    placed = preplacedAmazons(B)
#first 0 tracks expanded nodes, 
#second 0 tracks index of B
#placed tracks pre-placed amazons

    amazonDFS(B, N, 0, 0, placed) 

if __name__ == "__main__":
    main()

    
