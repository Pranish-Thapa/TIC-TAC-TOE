# Tic Tac Toe board
board_2=[" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]
def print_board_2():
    print(board_2[0] + " | " + board_2[1] + " | " + board_2[2])
    print("--|---|--")
    print(board_2[3] + " | " + board_2[4] + " | " + board_2[5])
    print("--|---|--")
    print(board_2[6] + " | " + board_2[7] + " | " + board_2[8])
for i in range(0,9):
    for j in range(i+1,10):
        board_2.insert(i,str(j))
        break
def welcome():
    print_board_2()
    print("---------------->Welcome to TIC TAC TOE<----------------")
    print("PLayer X's turn first")
def enter_x():
    while True:
        while True:
            try:
                x=int(input("Enter a position: "))
                break;
            except:
                print("Invalid input")
        if x < 1 or x>9:
            print("INVALID INPUT")
        else:
            break;
    for i in range(1,10):
        if x==i:
            board_2.pop(x-1)
            board_2.insert(x-1,'X')
        else:
            pass
    print_board_2()
def enter_o():
    while True:
        while True:
            try:
                o=int(input("Enter a position(Player O): "))
                break;
            except:
                print("Invalid input")
        if o < 1 or o>9:
            print("INVALID INPUT")
        else:
            break;
    for i in range(1,10):
        if o==i:
            board_2.pop(o-1)
            board_2.insert(o-1,'O')
        else:
            pass
    print_board_2()
def win_check():
    i=0
    winning_combinations = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,4,7],
    [2,5,8],
    [3,6,9],
    [1,5,9],
    [3,5,7]
]
    win_x=['X','X','X']
    win_o=['O','O','O']
    
    for arrs in winning_combinations:
        wc=board_2[arrs[0]-1], board_2[arrs[1]-1],board_2[arrs[2]-1]
        if list(wc)==win_x:
            print("Player X has won the game")
            
            while True:
                a=input("Press (R) to play again or (E) to exit....").lower()
                if a=='r':
                    play_game()
                elif a=='e':
                    exit()
                else:
                    print('INVALID INPUT')
            
            
        elif list(wc)==win_o:
            print('Player O has won the game')
            while True:
                a=input("Press (R) to play again or (E) to exit....").lower()
                if a=='r':
                    play_game()
                elif a=='e':
                    exit()
                else:
                    print('INVALID INPUT')
        else:
            pass
def play_game():
        welcome()
        while True:
            enter_x()
            win_check()
            enter_o()
            win_check()
play_game()
        



    

        


