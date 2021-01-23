def display(A):
     '''
     This function will be used to display the layers
     '''
     Print_Matrix=[] #here we will fill in with strings that will later on print in order to visualize the matrix
     for item in A:
        Print_Matrix.append(['','',''])


     i=0
     j=0

     h = "\u2501"  #upper horizontal dash
     lcd = "\u2517" #left down corner
     lcu = "\u250F" #left upper corner
     v = "\u2503" #vertical dash
     rcd = "\u251B" #right down corner
     rcu = "\u2513" #right upper corner
     hd = '\u2581' #lower horizontal dash

     all=[]
     for item in A:
         all.extend(item)
     all.sort()
     all=all[::-1]

     last_number_digits=len(str(all[0])) # this is the number of digits of the largest value of matrix A

     while i<=len(A)-1:

        while j <= len(A[0]) - 1:
            if j!=len(A[0])-1:
                if A[i][j] == A[i][j + 1]:
                    if last_number_digits<=2:
                     Print_Matrix[i][0] += lcu + 10*h + rcu
                     Print_Matrix[i][1] += v + f' {A[i][j]:<3}  {A[i][j]:>3} ' +2*(last_number_digits-2)*' ' + v
                     Print_Matrix[i][2] += v + 10*hd + v
                    else:
                     Print_Matrix[i][0] += lcu + 10*h +2*(last_number_digits-2)*h +rcu
                     Print_Matrix[i][1] += v + f' {A[i][j]:<3}  {A[i][j]:>{2*last_number_digits-1}} ' + v
                     Print_Matrix[i][2] += v + 10*hd +2*(last_number_digits-2)*hd+ v

                    j += 2

                elif i==0 :
                    if last_number_digits<=2:
                     Print_Matrix[i][0]+=lcu+4*h+rcu
                     Print_Matrix[i][1]+=v+f' {A[i][j]:<2} '+v
                     Print_Matrix[i][2]+=v+f'    '+v
                    else:
                     Print_Matrix[i][0] += lcu +4*h +(last_number_digits-2)*h+ rcu
                     Print_Matrix[i][1] += v + f' {A[i][j]:^{last_number_digits}} ' + v
                     Print_Matrix[i][2] += v + f'    ' +(last_number_digits-2)*' '+ v
                    j+=1
                elif A[i][j]==A[i-1][j]:

                  if last_number_digits<=2:
                    Print_Matrix[i][0] += v+f'    '+v
                    Print_Matrix[i][1] += v + f' {A[i][j]:<2} ' + v
                    Print_Matrix[i][2] += v+4*hd+v
                  else:
                    Print_Matrix[i][0] += v + f'    ' +(last_number_digits-2)*' '+ v
                    Print_Matrix[i][1] += v + f' {A[i][j]:^{last_number_digits}} ' + v
                    Print_Matrix[i][2] += v + 4*hd +(last_number_digits-2)*hd+ v
                  j += 1
                else:
                  if last_number_digits<=2:
                    Print_Matrix[i][0] += lcu+4*h+rcu
                    Print_Matrix[i][1] += v + f' {A[i][j]:<2} ' + v
                    Print_Matrix[i][2] += v + f'    ' + v
                  else:
                      Print_Matrix[i][0] += lcu + 4*h + (last_number_digits - 2) * h + rcu
                      Print_Matrix[i][1] += v + f' {A[i][j]:^{last_number_digits}} ' + v
                      Print_Matrix[i][2] += v + f'    ' + (last_number_digits - 2) * ' ' + v

                  j += 1

            else:
              if i==0 :
                if last_number_digits<=2:
                 Print_Matrix[i][0]+=lcu+4*h+rcu
                 Print_Matrix[i][1]+=v+f' {A[i][j]:<2} '+v
                 Print_Matrix[i][2]+=v+f'    '+v
                else:
                 Print_Matrix[i][0] += lcu + 4*h + (last_number_digits - 2) * h + rcu
                 Print_Matrix[i][1] += v + f' {A[i][j]:^{last_number_digits}} ' + v
                 Print_Matrix[i][2] += v + f'    ' + (last_number_digits - 2) * ' ' + v
                j+=1
              elif A[i][j] == A[i - 1][j]:
                  if last_number_digits <= 2:
                      Print_Matrix[i][0] += v + f'    ' + v
                      Print_Matrix[i][1] += v + f' {A[i][j]:<2} ' + v
                      Print_Matrix[i][2] += v + 4*hd + v
                  else:
                      Print_Matrix[i][0] += v + f'    ' + (last_number_digits - 2) * ' ' + v
                      Print_Matrix[i][1] += v + f' {A[i][j]:^{last_number_digits}} ' + v
                      Print_Matrix[i][2] += v +4*hd + (last_number_digits - 2) * hd + v
                  j += 1
              else:
                  if last_number_digits <= 2:
                      Print_Matrix[i][0] += lcu + 4*h + rcu
                      Print_Matrix[i][1] += v + f' {A[i][j]:<2} ' + v
                      Print_Matrix[i][2] += v + f'    ' + v
                  else:
                      Print_Matrix[i][0] += lcu + 4*h + (last_number_digits - 2) * h + rcu
                      Print_Matrix[i][1] += v + f' {A[i][j]:^{last_number_digits}} ' + v
                      Print_Matrix[i][2] += v + f'    ' + (last_number_digits - 2) * ' ' + v
                  j += 1
        i+=1
        j=0

     for i in range(0, len(Print_Matrix)):
         for j in range(0, len(Print_Matrix[0])):
             print(Print_Matrix[i][j])


