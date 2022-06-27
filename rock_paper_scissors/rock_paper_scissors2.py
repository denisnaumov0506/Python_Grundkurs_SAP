# Actual bonus assignment

player1, player2 = [], []
win_player_1, win_player_2, draw = 0, 0, 0
wins = {'R' : 'S',
        'S' : 'P',
        'P' : 'R'}

with open("player1.txt", 'r') as f:
    for line in f:
        player1.append(line.strip())

with open("player2.txt", 'r') as f:
    for line in f:
        player2.append(line.strip())

for x in range(0, 100):
    if player1[x] == player2[x]:
        draw += 1
    elif wins[player1[x]] == player2[x]:
        win_player_1 += 1
    else:
        win_player_2 += 1

with open("result.txt", 'w') as f:
    f.write(f"Player1 wins: {win_player_1}\n"
            f"Player2 wins: {win_player_2}\n"
            f"Draws: {draw}\n")
