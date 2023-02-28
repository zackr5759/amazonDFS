import copy

def printboard(B):
    length = len(B)
    for i in range(length):
      for j in range(length):
        if B[i] == j:
          print("|",B[i], end="", sep='')
        else:
          print("|_",end="")
        if j == length - 1:
          print("|")

def amazons(list):
  return len(list) - list.count(-1)

def amazonDFS(B):
    # B is a vector such that B[i] = the col number in which the amazon is placed in row i
    # n is the dimension of the board for which a solution is sought
    # pre-condition: B is a valid partial solution
    if amazons(B) == len(B): #solved
      return 1, B
    count = 0
    best = copy.deepcopy(B)

    for c in range(len(B)):#rows
      for j in range(len(B)): #cols
        if B[c] == -1: #no amazons
          # looking for a candidate for B[k] which will be an integer from 0 to n-1
          if not(attack(B, len(B), j, c)):
              B[c] = j
              tempCount, tempB = amazonDFS(B)
              count += tempCount
              if amazons(tempB) > amazons(best):
                best = copy.deepcopy(tempB)
              B[c] = -1
    return count+1, best

def attack(B, n, j, row):
    #checks if the cell B[k+1, j] is under attack by the amazons in the first k rows of B
    rowNum = row+1
    for k in range(n): # column attack
        if B[k] == j and B[k] != -1:
            return True
    for i in range(rowNum):#diagonal attack
      #print(row)
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

def main():
#It returns a board by adding as many additional amazons as possible, 
#return True (False) if it could find a solution with additional n − k amazons, 
#the number of nodes expanded by DFS.
    print("N-Amazons program by Hector Romero and Zachary Robinson")

    while(True):
      B = input("Enter a board as a vector B, 'q' to quit:")
      if B == "q":
        print("****N-Amazons program terminated****")
        return 

      B = B.strip("[]").split(",")
      for i in range(len(B)):
          B[i] = int(B[i])

      count, best = amazonDFS(B)

      if amazons(best) == len(B):
        print(count, best, "True") # Has N (additional N-K) amazons 
      else:
        print(count, best, "False") # Doesn't have N amazons

    #prints a 2d matrix representing the board 
    #printboard(best) 

if __name__ == "__main__":
    main()
