class Player():
    def __init__(self, player_name, move_name):
        self.player = player_name
        self.move_name = move_name
        self.score = 0
class Game():
    def __init__(self):
        self.is_game = True
        self.game_list = [["_","_","_",],["_","_","_",],["_","_","_",]]


game = Game()


def get_move(name, player_name):
    print()
    move = int(input(f"Player '{player_name}'. Enter your move 1-9: > "))
    player_move(move, name,player_name)
    
def game_board(game_list):    
    print()
    for game in game_list:
        print(f"{' '.join(game)}")


def player_move(move, player, player_name):
    if move == 1 and game.game_list[0][0]=='_':
        game.game_list[0][0] = player
    elif move == 2 and game.game_list[0][1]=='_':
        game.game_list[0][1] = player
    elif move == 3 and game.game_list[0][2]=='_':
        game.game_list [0][2] = player
    elif move == 4 and game.game_list[1][0]=='_':
        game.game_list[1][0] = player
    elif move == 5 and game.game_list[1][1]=='_':
        game.game_list[1][1] = player
    elif move == 6 and game.game_list[1][2]=='_':
        game.game_list[1][2]= player
    elif move == 7 and game.game_list[2][0]=='_':
        game.game_list[2][0] = player
    elif move == 8 and game.game_list[2][1]=='_':
        game.game_list[2][1] = player
    elif move == 9 and game.game_list[2][2]=='_':
        game.game_list[2][2] = player
    else:
        print()
        print('Space already occupied')
        get_move(player, player_name)
        
def get_winner(name, player_name):
    if game.game_list[0][0]==name and game.game_list[0][1]==name and game.game_list[0][2]==name or \
        game.game_list[1][0]==name and game.game_list[1][1]==name and game.game_list[1][2]==name or \
        game.game_list[2][0]==name and game.game_list[2][1]==name and game.game_list[2][2]==name or \
        game.game_list[0][0]==name and game.game_list[1][1] and game.game_list[2][2]==name or \
        game.game_list[0][2]== name and game.game_list[1][1]== name and game.game_list[2][0] or \
        game.game_list[0][0]== name and game.game_list[1][0]== name and game.game_list[2][0]== name or \
        game.game_list[0][1]== name and game.game_list[1][1]== name and game.game_list[2][1]== name or \
        game.game_list[0][2]== name and game.game_list[1][2]== name and game.game_list[2][2]== name:
        is_winner = True
        print()
        print(f'The winner is {player_name} ') 
        return is_winner
    else:
        is_winner = False

def play_again():
    print()
    i = input("Wanna play again? (yes/no): > ")
    if i.lower() == "yes":
        main()
    if i.lower() == "no":
        return False

def main():
    print()
    p_1 = input('Please enter Player 1 name: ')
    p_2 = input('Please enter Player 2 name: ')
    player_1 = Player(p_1,'X')
    player_2 = Player(p_2,'O')
    
    while game.is_game:

        get_move(player_1.move_name, player_1.player)
        game_board(game.game_list)
        if get_winner(player_1.move_name, player_1.player) == True:
            if play_again() == False:
                break
            
        get_move(player_2.move_name, player_2.player)
        game_board(game.game_list)
        if get_winner(player_1.move_name, player_2.player)   == True:
            if play_again() == False:
                break

        
if __name__ == "__main__":
    main()
    
    