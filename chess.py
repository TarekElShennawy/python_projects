#Initialising the input of the user to col and row variables
start_col = int(input())
start_row = int(input())
end_col = int(input())
end_row = int(input())

#Logic that states if the horizontal or vertical values equate or the absolute of their difference (for the diagonals), returning yes if true or no otherwise
if start_col == end_col or start_row == end_row or abs(start_col - end_col) == abs(start_row - end_row):
  print ("YES")
  print (abs(start_col - end_col), abs(start_row - end_row))
else:
  print ("NO")
