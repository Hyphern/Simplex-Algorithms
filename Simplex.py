tableau = []
EQ_num = int(input("How many equations?:"))
Var_num = int(input("How many variables?:"))

for a in range (0,EQ_num+1):
    appendable = []
    print("row ",a )

    for b in range (0,Var_num+1):
        x = int(input(":"))
        appendable.append(x)
    tableau.append(appendable)

for c in range (0,EQ_num):
    for d in range (0,EQ_num-1):
        tableau[c].insert(-1,0)

for e in range (0,EQ_num):
    tableau[e].insert(Var_num+e,1)

for f in range (0,EQ_num):
    tableau[-1].insert(-1,0)

unsolved = True

while unsolved:

    for k in range(0,EQ_num+1):
        print(tableau[k])
    print("")

    most_negative = min(filter(lambda x: x < 0, tableau[-1]), default=0)

    if most_negative >= 0:
        unsolved = False
        print("Solved!")
    pivot_column = tableau[-1].index(most_negative)
    theta_values = []

    for h in range(0,EQ_num):

        if tableau[h][pivot_column] ==0:
            theta_values.append(100000)
        else:
            theta_values.append(tableau[h][-1]/tableau[h][pivot_column])
    theta_value = min([i for i in theta_values if i > 0])

    pivot_row = theta_values.index(theta_value)
    EQC = tableau[pivot_row]
    pivot = EQC[pivot_column]
    EQCRO = []

    for q in range(0,len(tableau[-1])):
        if EQC[q] == 0:
            EQCRO.append(EQC[q])
        else:
            EQCRO.append(EQC[q] / pivot)
            
    tableau[pivot_row] = EQCRO

    for i in range (0,len(tableau)):
        if i == pivot_row:
            continue
        else:     
            pivot_multiple1 = tableau[i][pivot_column] / EQCRO[pivot_column] 
            test = len(tableau[-1])
            for j in range (0,len(tableau[-1])):                    
                tableau[i][j] -= (pivot_multiple1 * EQCRO[j])