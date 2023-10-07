# Made by Onyrew
def evaluate_board(_board, _token):
    # x, y
    for i in range(3):
        counter_x = 0
        counter_y = 0
        for j in range(3):
            if _board[i][j] == _token:
                counter_x += 1
            if _board[j][i] == _token:
                counter_y += 1
        if counter_x == 3 or counter_y == 3:
            return True
    # \/
    counter_l = 0
    counter_r = 0
    for i in range(3):
        if _board[i][i] == _token:
            counter_l += 1
        if _board[i][2 - i] == _token:
            counter_r += 1
    # Check
    return counter_l == 3 or counter_r == 3

# Init
board = [
    [ 0, 0, 0 ],
    [ 0, 0, 0 ],
    [ 0, 0, 0 ]
]
won = False
current_player = 1

while not won:
    # Draw
    for i in range(3):
        print(board[i])
    # Input
    print("Step:")
    x, y = map(int, input().split())
    if not (0 <= x <= 2) or not (0 <= y <= 2):
        print("Must be a valid point!")
        continue
    # Add
    if board[x][y] != 0:
        print("Must be an empty slot!")
        continue
    board[x][y] = current_player
    # Eval
    won = evaluate_board(board, current_player)
    if won:
        print(f"Player{current_player} Won")
    if str(board).count('0') == 0:
        print("Tie")
        break
    # Switch
    current_player = (current_player & 1) + 1
