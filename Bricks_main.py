'''
A brick game is being created!
'''

from project_bricks import layer1_generator
from project_bricks.displaying import display

#Here, the user provides the number of rows and columns and checks whether they are even numbers.
def input_dimensions():
    '''
    Taking the dimensions rows and columns (N and M)
    '''

    while True:
        try:
            rows = int(input("Input the number of rows: "))
            if rows%2==0 and rows<=100 and rows>=2:
                break
            else:
                print('Your number must be even')
        except:
            print('You must type an integer!')

    while True:
        try:
            columns = int(input("Input the number of columns: "))
            if columns%2==0 and columns<=100 and columns>=0:
                break
            else:
                print('Your number must be even')
        except:
            print('You must type an integer!')

    return rows,columns

def make_layer1(rows):
    '''
    Here, we will create layer1
    '''

    layer1=[]
    for i in range(0,rows):
        row = input(f"input row{i+1}: ")
        row = row.split()
        for i in range(0, len(row)):
            row[i] = int(row[i])
        layer1.append(row)

    print('') # empty line
    return layer1

def validate_dimensions(layer1,rows,columns):
    '''
    Here we will validate the dimensions of the created layer whether they correspond to the input dimensions
    '''
    validate=True
    if len(layer1)!=rows:
        validate = False
    for item in layer1:
        if len(item)!=columns:
            validate=False

    return validate

def validate_for_3(layer1):
    '''
    We will see that there is no brick that has length or height of 3
    '''
    validate=True
    all_elements=[]
    for item in layer1:
        all_elements.extend(item)

    for item in all_elements:
        if all_elements.count(item)==3:
         validate=False
         break

    return validate

def make_values(layer1):
    '''
    Here we create a set of values, that will later on be used to create the bricks
    '''
    one_row_matrix = []
    for item in layer1:
        one_row_matrix.extend(item)

    values = list(set(one_row_matrix))
    return values


#this is the function for the creation of the second layer
def make_layer2(layer1,values):
    '''
    This function represent the main logic. Basically we move through the first layer with a step that is a 2x2 matrix
    and create the corresponding second layer.
    '''
    m = len(layer1) # number of rows
    n = len(layer1[0]) #number of columns (= to the number of rows of the first element)
    layer2=[]


    for i in range(0,m-1,2):
        up_row=[]
        down_row=[]
        for j in range(0,n-1,2):
            if layer1[i][j]==layer1[i][j+1] or layer1[i+1][j]==layer1[i+1][j+1]:
                #add two vertical bricks

                up_row.append(values[0])
                down_row.append(values[0])
                values.pop(0)
                up_row.append(values[0])
                down_row.append(values[0])
                values.pop(0)
            else:
                #add two horizontal bricks
                up_row.append(values[0])
                up_row.append(values[0])
                values.pop(0)

                down_row.append(values[0])
                down_row.append(values[0])
                values.pop(0)

        layer2.append(up_row)
        layer2.append(down_row)
    return layer2


def check(l1,l2):
    '''
    This function checks whether the created layer2 indeed follows the rule from the assignment
    '''
    N=len(l1) # rows of layer 1
    M=len(l1[0]) #columns of layer1
    for i in range(0,N):
        for j in range(0,M-1):
            if l1[i][j]==l1[i][j+1] and l2[i][j]==l2[i][j+1]:
                print('-1')  # printing the wanted output with respect to the assignment
                return 'Check: Wrong'

    print('Check: Correct')

def print_layer(layer):
    for item in layer:
        print(item)

while True:
    #First lets create the dimensions of layer 1
    dimensions=input_dimensions()
    N=dimensions[0] #N-rows
    M=dimensions[1] #M-columns

    #create layer 1 and validate if the dimensions are correct and validate if there is a brick that spans 3 rows or columns
    #if both validations are correct - break, else - go again

    layer1=make_layer1(N)
    if validate_dimensions(layer1,N,M)==False:
        print('The dimensions of your layer are incorrect')
    elif validate_for_3(layer1)==False:
        print('There is a brick that is spanning 3 rows/columns')
    else:
        break

print('')

#creating the values list
values=make_values(layer1)


#Now we create layer 2, print both layers and check whether our layer 2 follows the assignemnt's rules
layer2 = make_layer2(layer1,values)

#I have imported a display function, that visualizes the bricks. However, because the python's print line is restrained
# to 24 columns, if the number of columns that the user provides is more than 24, then we will simply print both layers, without
#visualization
if len(layer1[0]) <= 24:

    print('LAYER 2:')
    display(layer2)

    print('')

    print('LAYER 1:')
    display(layer1)
else:
    print('LAYER 2:')
    print_layer(layer2)

    print('')

    print('LAYER 1:')
    print_layer(layer1)

check(layer1, layer2)



###This is extra. Press yes if you want to generate a lot of inputs of layers1 and create the corresponding layer 2 of each.
print('')
while True:
 choice=input('The following will automatically generate various layers 1 and create their corresponding layers 2. Press "y" to continue or "n" to stop:')
 #for more information, read layer1_generator.py
 if choice =='y' or choice=='Y' or choice=='n' or choice=='N':
     break
 else:
     print('Invalid choice,try again!')

if choice.lower()=='y':

    print(5 * '\n')

    all_correct=True # we will need it to check if all layers 2 are correct

    for step in range(10):  #You can choose your step (number of layer 1 matrices)

     values=list(range(1,3000))
     layer1= layer1_generator.correct_generate(layer1_generator.generate_try, 10, 24)
     layer2=make_layer2(layer1,values)

     if len(layer1[0])<=24:

        print('LAYER 2:')
        display(layer2)

        print('\n')

        print('LAYER 1:')
        display(layer1)
     else:
        print('LAYER 2:')
        print_layer(layer2)

        print('')

        print('LAYER 1:')
        print_layer(layer1)


     check(layer1, layer2)
     print('')

     if check=='Check: Wrong':
        all_correct=False

    print('')
    print(f'All are correct? {all_correct}')


