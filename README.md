# amazonDFS
This project attempts to fill a chess board with as many "amazons" (queens that can also move like knights) without any of them attacking eachother as possible by exploring each combination of placements with a DFS. It returns true if it could find a solution that has N - K amazons placed. N being the column and width dimensions of the board and K being the amazons that are already placed on the board. Or in other words, 8 amazons for an 8x8 board would return true. 7 amazons for an 8x8 board would return false. Always returns the maximum amount of amazons able to be placed regardless of true or false result.

When entering a board, type comma separated numbers to give information on ROW at a time. The information is where an amazon is in that row with -1 indicating there is no amazon in this row. For example a 5x5 board with one amazon located at (1,3) would be entered like so:

 Enter a board as a vector B, 'q' to quit:-1,-1,1,-1,-1
 
 5 [4, -1, 1, -1, -1] False
                                 
And the program finds that, at most, one more amazon can be placed on this board. One example being at (4,1).

