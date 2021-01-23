'''
This module will serve to generate various 'layer 1' in order to better check
our algorithm for the creation of layer 2
'''

from itertools import repeat
import random
def generate_try(m,n):
    #rows -m
    #cols-n
    layer1=[]
    values=[]
    for i in range(1,30000):
        values.append(i)

    for i in range(0,m):
        zero_row=list(repeat(0,n))
        layer1.append(zero_row)
    #we first create layer 1 to be mxn matrix of zeros

    index_list=[] # we will create a list of the indexes of the matrix layer1
    for i in range(0,m):
        for j in range(0,n):
            index_list.append((i,j))

    print('')

    for index in index_list:
        i=index[0]
        j=index[1]
       #basically we go through each index of the matrix layer1 and put horizontal ot vertical brick there, while following some rules.

        if j<=n-2 and i<=m-2 and layer1[i][j]==0:
            choice=random.choice(['vertical','horizontal'])

            while True:

             if choice=='horizontal' and layer1[i][j+1]==0:
                layer1[i][j]=values[0]
                layer1[i][j+1]=values[0]
                values.pop(0)
                break
             elif choice =='vertical' and layer1[i+1][j]==0:
                  layer1[i][j] = values[0]
                  layer1[i+1][j] = values[0]
                  values.pop(0)
                  break
             else:
                arr = ['vertical', 'horizontal']
                arr.remove(choice)
                choice = arr[0]


        elif i==m-1 and j<=n-2 and layer1[i][j]==0:

            if layer1[i][j+1]!=0:
                return 'again'
            else:
             layer1[i][j] = values[0]
             layer1[i][j + 1] = values[0]
             values.pop(0)

        elif j==n-1 and i<m-1 and layer1[i][j]==0:

            layer1[i][j] = values[0]
            layer1[i + 1][j] = values[0]
            values.pop(0)


    return layer1



def check(matrix):
    #we check if the generated matrix is correct.
    all=[]
    for item in matrix:
        all.extend(item)
    if len(set(all))!=(len(matrix)*len(matrix[0]))/2:
        print('False')
        return False
    else:
        print('True')
        return True


def disp(l1):
  for item in l1:
     print(item)

#we generate a matrix, we check if it is correct, if not, generate again. And so on, until correct.
#so correct_generate gives us a correctly generated layer1.
def correct_generate(function,m,n):
    while True:
        layer1 = function(m,n)
        if layer1 != 'again':
            break
    return(layer1)


