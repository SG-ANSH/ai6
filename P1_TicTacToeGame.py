board = {
    'T1': '','T2': '','T3':'',
    'M1': '','M2': '','M3':'',
    'D1': '','D2': '','D3':''
}
Player = 1
TotalMoves = 0
EndCheck = 0

def check():
    #Horizontal Check
    if board['T1'] == 'X' and board['T2'] == 'X' and board['T3'] == 'X':
        print("Player 1 Won!")
        return 1
    if board['M1'] == 'X' and board['M2'] == 'X' and board['M3'] == 'X':
        print("Player 1 Won!")
        return 1
    if board['D1'] == 'X' and board['D2'] == 'X' and board['D3'] == 'X':
        print("Player 1 Won!")
        return 1

    #Vertical Check
    if board['T1'] == 'X' and board['M1'] == 'X' and board['D1'] == 'X':
        print("Player 1 Won!")
        return 1
    if board['T2'] == 'X' and board['M2'] == 'X' and board['D2'] == 'X':
        print("Player 1 Won!")
        return 1
    if board['T3'] == 'X' and board['M3'] == 'X' and board['D3'] == 'X':
        print("Player 1 Won!")
        return 1
    
    #Diagonal Check
    if board['T1'] == 'X' and board['M2'] == 'X' and board['D3'] == 'X':
        print("Player 1 Won!")
        return 1
    if board['T3'] == 'X' and board['D2'] == 'X' and board['M1'] == 'X':
        print("Player 1 Won!")
        return 1
    

#Player 2 Check
#Horizontal Check
    if board['T1'] == 'O' and board['T2'] == 'O' and board['T3'] == 'O':
        print("Player 2 Won!")
        return 1
    if board['M1'] == 'O' and board['M2'] == 'O' and board['M3'] == 'O':
        print("Player 2 Won!")
        return 1
    if board['D1'] == 'O' and board['D2'] == 'O' and board['D3'] == 'O':
        print("Player 2 Won!")
        return 1

    #Vertical Check
    if board['T1'] == 'O' and board['M1'] == 'O' and board['D1'] == 'O':
        print("Player 2 Won!")
        return 1
    if board['T2'] == 'O' and board['D2'] == 'O' and board['M2'] == 'O':
        print("Player 2 Won!")
        return 1
    if board['T3'] == 'O' and board['M3'] == 'O' and board['D3'] == 'O':
        print("Player 2 Won!")
        return 1
    
    #Diagonal Check
    if board['T1'] == 'O' and board['M2'] == 'O' and board['D3'] == 'O':
        print("Player 2 Won!")
        return 1
    if board['T3'] == 'O' and board['D2'] == 'O' and board['M1'] == 'O':
        print("Player 2 Won!")
        return 1
    return 0

print('T1 | T2 | T3 \n')
print('-+-+- \n')
print('T1 | T2 | T3 \n')
print('-+-+- \n')
print('T1 | T2 | T3 \n')

while True:
    print(board['T1']+ '|' +board['T2']+ '|' +board['T3'])
    print('-+-+- \n')
    print(board['M1']+ '|' +board['M2']+ '|' +board['M3'])
    print('-+-+- \n')
    print(board['D1']+ '|' +board['D2']+ '|' +board['D3'])

    EndCheck = check()
    if TotalMoves == 9 or EndCheck == 1:
        break
    while True:
        if Player == 1:
            p1_input = input("Enter your value: ")
            print(p1_input)
            #p1_input =  input('Player 1')
            if p1_input.upper() in board and board[p1_input.upper()] == '':
                board[p1_input.upper()] = 'X'
                player = 2
                break
            else:
                print("Wrong Input. Try Again")
                continue
        
        if Player == 2:
            p2_input =  input('Player 2 Chance')
            if p2_input.upper() in board and board[p2_input.upper()] == '':
                board[p2_input.upper()] = 'O'
                player = 1
                break
            else:
                print("Wrong Input. Try Again")
                continue

                TotalMoves += 1
            print('*************************')
            print()