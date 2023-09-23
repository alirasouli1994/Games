A = [[0]*3 for i in range(3)]

# fills the table with values 1 to 9
def init_table(A):
    khooneh = 1
    for i in range(3):
        for j in range(3):
            A[i][j] = khooneh
            khooneh +=1
        
# prints the table
def print_table(A):
    for i in range(3):
        for j in range(3):
            print(A[i][j] , end=' ')
        print()
    print()
def put(x,s):
    row = x // 3
    cloumn = x % 3
    if A[row][cloumn] == "X" or A[row][cloumn] == "O":
        print("jerzani shode")
        exit(0)
    A[row][cloumn] = s                

def check(s):
    for i in range(3):
        if A[i][0] == s and A[i][1] == s and A[i][2] == s:
            return True
        if A[0][i] == s and A[1][i] == s and A[2][i] == s:
            return True
    if A[0][0] == s and A[1][1] == s and A[2][2] == s:
        return True
    if A[0][2] == s and A[1][1] == s and A[2][0] == s:
        return True
        
    return False

print_table(A)
init_table(A)
print_table(A)

for move in range(9):
    if move % 2 == 0 :
        x = int(input('player 1: '))
        put(x-1, "X")
        if check('X'):
            print('player 1 wins!')
            break
    else :
        x = int(input('player 2: '))
        put(x-1, "O")
        if check('O'):
            print('player 2 wins!')
            break
    print()
    print_table(A)

