#!/usr/bin/env python
# coding: utf-8

# In[181]:


import math as Math


# In[182]:



def evaluate(b,player,opponent):  
   
    # Checking for Rows for X or O victory.  
    for row in range(0, 3):  
       
        if b[row][0] == b[row][1] and b[row][1] == b[row][2]:  
           
            if b[row][0] == player: 
                return 10 
            elif b[row][0] == opponent:  
                return -10 
  
    # Checking for Columns for X or O victory.  
    for col in range(0, 3):  
       
        if b[0][col] == b[1][col] and b[1][col] == b[2][col]:  
           
            if b[0][col]==player: 
                return 10 
            elif b[0][col] == opponent:  
                return -10 
  
    # Checking for Diagonals for X or O victory.  
    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:  
       
        if b[0][0] == player:  
            return 10 
        elif b[0][0] == opponent:  
            return -10 
       
    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:  
       
        if b[0][2] == player:  
            return 10 
        elif b[0][2] == opponent:  
            return -10 
       
    # Else if none of them have won then return 0  
    return 0 
   


# In[183]:


def isFullBoard(board):
    for x in board:
        for y in x:
            if y=='':
                return False
    return True


# In[184]:


def createNewNode(currentBoard,nChar,oChar):
    newNode=currentBoard[:]
    c=0
    for x in currentBoard:
        col=0
        for y in x:
            if y==oChar:
                newNode[c][col]=nChar
                return newNode
            col-=-1
        c-=-1
    return newNode    


# In[197]:


def minimax(board,depth,isMax,player,opponent):
    
    score=evaluate(board,player,opponent)
    print("Score : ",score,"\nDepth : ",depth,"\nMovement : ",isMax)
    
    if score==10:
        return score
    if score==-10:
        return score
    
    if isFullBoard(board):
        return 0

    if isMax:
        best=-999
        temp=createNewNode(board,player,'')
        print(temp)
        best=max(best,minimax(temp,depth+1,not isMax,player,opponent))
        print('Max :',score)
        return best
    else:
        best=999
        temp=createNewNode(board,opponent,'')
        print(temp)
        best=min(best,minimax(temp,depth+1,not isMax,player,opponent))
        print('Min :',score)
        return best


# In[195]:


def findBestMove(board,player,opponent):
    bestMove=None
    bestVal=-999
    row=0
    nboard=board[:]
    for x in board:
        col=0
        for y in x:
            if y=='':
                nboard[row][col]=player
                print("Input :",nboard)
                movVal=minimax(nboard,0,False,player,opponent)
#                 print(row,col,movVal,bestVal)
                if movVal >= bestVal:
                    bestMove=row,col,bestVal
                    bestVal=movVal
                    print("-"*10,"BestVal :",bestVal,"-"*10)
            col-=-1
        row-=-1
    return bestMove


# In[199]:



if __name__ == "__main__":
   
    board = [['o', 'x', 'o'],  
             ['x', 'x', 'o'],  
             ['', '', '']]  
    bestMove=findBestMove(board,'x','o')
    print("Best Move is", bestMove)  
  
# This code is contributed by Parth Roy 


# In[ ]:




