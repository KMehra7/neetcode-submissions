class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):

                #Check for '.'
                if board[i][j] == '.':
                    continue
                if (board[i][j] in rows[i]
                    or board[i][j] in cols[j]
                    or board[i][j] in squares[ (i//3, j//3) ]
                ):
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i//3,j//3)].add(board[i][j])
        # print(rows)
        ''' {0: {'2', '1', '3'}, 
            1: {'4', '5'}, 
            2: {'3', '8', '9'}, 
            3: {'4', '5', '6'}, 
            4: {'5', '3', '8'}, 
            5: {'2', '6', '7'}, 
            6: {'2'}, 
            7: {'4', '1', '8', '9'}, 
            8: {'7', '8', '9'}}) '''
        # print(cols)
        ''' {0: {'4', '1', '7', '5'}, 
            1: {'2', '9'}, 
            4: {'6', '1', '2', '3', '8'}, 
            3: {'4', '5', '8'}, 
            2: {'8'}, 
            8: {'5', '4', '6', '9', '3', '8'}, 
            5: {'3', '9'}, 
            6: {'2'}, 
            7: {'7'}})'''
        # print(squares)
        '''{(0, 0): {'4', '1', '9', '2', '8'}, 
            (0, 1): {'5', '3'}, 
            (0, 2): {'3'}, 
            (1, 0): {'5', '7'}, 
            (1, 1): {'2', '6', '3', '8'}, 
            (1, 2): {'4', '5', '6'}, 
            (2, 2): {'2', '7', '8', '9'}, 
            (2, 1): {'4', '1', '8', '9'}})'''

        return True

        # Cant work cause it doesnt check all rows for one column
        #It only checks the adjacent rows
        # col=[]
        # for i in range(len(board)):
        #     for j in range(9):
        #         if board[i][j] == board[i][j-1] and board[i][j] != '.':
        #             return False

        #         print(j,i)
        #         print(j-1,i)
        #         print(board[j][i],board[j-1][i] )
        #         print('***')
        #         if board[j][i] == board[j-1][i] and board[j][i] != '.':
        #             return False
        # for i in range(0,len(board)-3,3):
        #     for j in range(0,len(board[i])-3,3):

        #         # if board[i][j] == board[i][j+1] and board[i][j] != '.':
        #         #     return False

        #         # print(board[j][i],board[j+1][i] )
        #         # if board[j][i] == board[j+1][i] and board[j][i] != '.':
        #         #     return False

        #         # print('###')
        #         # print(i,j)
        #         # print(board[i][j],board[i][j+1],board[i][j+2])
        #         # print(board[i+1][j],board[i+1][j+1],board[i+1][j+2])
        #         # print(board[i+2][j],board[i+2][j+1],board[i+2][j+2])
        #         # print('###')
        #         if ( board[i][j] == board[i][j+1] or board[i][j] == board[i][j+2]
        #             or board[i][j] == board[i+1][j] or board[i][j] == board[i+2][j]
        #             or board[i][j] == board[i+1][j+1] or board[i][j] == board[i+2][j+2]
        #             or board[i][j] == board[i+1][j+2] or board[i][j] == board[i+2][j+1]
        #         ):
                    
        #             if ( board[i][j] != '.' 
        #                 # and board[j][i] != '.'
        #                 # and board[i+1][j] != '.' and board[j+1][i] != '.'
        #                 # and board[i+2][j] != '.' and board[j+2][i] != '.'
        #                 # and board[i][j+1] != '.' and board[i][j+2] != '.'
        #                 # and board[j][i+1] != '.' and board[j][i+2] != '.'
        #                 # and board[i+1][j+1] != '.' and board[i+2][j+2] != '.'
        #             ):
        #                     return False

        # return True
                