print('Tic Tac Toe')


def switch_players(player):
    if player==Player1:
        player=Player2
    else:
        player=Player1
    return player
def make_move(position,player):
    if position[0]=='t':
        if position[1]=='1':
            moves[0][0]=player
        elif position[1]=='2':
            moves[0][1]=player
        else:
            moves[0][2]=player
    elif position[0]=='m':
        if position[1]=='1':
            moves[1][0]=player
        elif position[1]=='2':
            moves[1][1]=player
        else:
            moves[1][2]=player
    else:
        if position[1]=='1':
            moves[2][0]=player
        elif position[1]=='2':
            moves[2][1]=player
        else:
            moves[2][2]=player

def position_to_coordinates(position):
    if position=='t1':
        return moves[0][0]
    if position=='t2':
        return moves[0][1]
    if position=='t3':
        return moves[0][2]
    if position=='m1':
        return moves[1][0]
    if position=='m2':
        return moves[1][1]
    if position=='m3':
        return moves[1][2]
    if position=='b1':
        return moves[2][0]
    if position=='b2':
        return moves[2][1]
    if position=='b3':
        return moves[2][2]

def check_cordinates(x):
    if x!='  ':
        return False

def moves_available(x):
    for n in range(3):
        for m in range(3):
            if x[n][m]=='  ':
                return True

def is_winner(t):
    i=0
    while i<3:
        if t[0][i]==t[1][i] and t[1][i]==t[2][i] and t[1][i]!='  ':
            return True
        if t[i][0]==t[i][1] and t[i][1]==t[i][2] and t[i][1]!='  ':
            return True
        if t[0][0]==t[1][1] and t[1][1]==t[2][2] and t[0][0]!='  ' or t[0][2]==t[1][1] and t[1][1]==t[2][0] and t[1][1]!='  ':
            return True
        i+=1
    return False


NewGame=str(input("New Game? Y for Yes N for No:"))

while NewGame=='Y' or NewGame=='y':
    moves=[['  ','  ','  '],['  ','  ','  '],['  ','  ','  ']]
    valid_moves=['t1','t2','t3','m1','m2','m3','b1','b2','b3']
    print("""
    t1  | t2 |  t3
    --------------
    m1  | m2 |  m3
    --------------
    b1  | b2 |  b3""")

    Player1=str(input("Player1, X or O?"))
    if Player1=='O' or Player1=='o':
        Player1='O'
        Player2='X'
    else:
        Player1='X'
        Player2='O'

    player=Player1

    def player_move(player):
        if not is_winner(moves):
            if moves_available(moves)==True:
                print("%s's move:" %(player))
                position=str(input(""))
                while check_cordinates(position_to_coordinates(position))==False:
                    print("Already taken. Choose new position")
                    position=str(input(""))
                while position not in valid_moves:
                    print("Invalid move")
                    position=str(input(""))
                make_move(position,player)
                print("""
                %s  | %s | %s
                --------------
                %s  | %s | %s
                --------------
                %s  | %s | %s""" %(moves[0][0],moves[0][1],moves[0][2],moves[1][0],moves[1][1],moves[1][2],moves[2][0],moves[2][1],moves[2][2]))
                player_move(switch_players(player))




    player_move(player)
    if is_winner(moves):
        print("%s Wins!"%(player))
    else:
        print("It's a tie")
    NewGame=str(input("New Game? Y for Yes N for No:"))
