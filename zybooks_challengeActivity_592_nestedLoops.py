num_rows = int(input())
num_cols = int(input())
#above is included in the books unchangable program

currentRow = 1
currentCol = 1
seatCol = '?'

while currentRow <= num_rows:
    seatCol = 'A'
    while currentCol <= num_cols:
        print(str(currentRow)+str(seatCol), end=' ')
        currentCol += 1
        seatCol = chr(ord(seatCol) + 1)
    currentRow += 1

#below is included in the books unchangeable program
print()
