# myString = 'Sanny'
# for letter in myString:
#     if letter == 'a':
#         break
#     print(letter)



# player1 = input("Please pick a marker 'X' or 'O'")
#print(player1)
board = ('#','x','o','x','o','x','o','x','o','x')
def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
print(display_board(board))

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player: choose X or O: ').upper()
    if marker == 'X' or marker == 'O':
        return('X','O')
    else:
        return None
    marker = player_input()
player_input()


