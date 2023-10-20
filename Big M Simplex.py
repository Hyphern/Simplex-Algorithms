rows = []
M = int(10000000000)
A_num = int(input("How many artificial variables?"))
EQ_num = int(input("How many equations?:"))
Var_num = int(input("How many variables?:"))
A_rows = []
kc =2*Var_num+A_num+1

for a in range (0,EQ_num+1):
    appendable = []
    print("row ",a )

    for b in range (0,Var_num+1):
        x = int(input(":"))
        appendable.append(x)
    rows.append(appendable)

for c in range (0,EQ_num):
    for d in range (0,EQ_num-1):
        rows[c].insert(-1,0)

for e in range (0,EQ_num):
    rows[e].insert(Var_num+e,1)

for f in range (0,EQ_num):
    rows[-1].insert(-1,0)

for g in range(0,EQ_num):
    for h in range(0,A_num-1):
        rows[g][h].insert(-1,0)

for l in range(0,A_num):
    tvar = int(input("Artificial variable rows:"))
    A_rows.append(tvar)

for num in A_rows:
    for a in range(0,len(A_rows)):
        rows[num].insert(-2+a,1)

not_solved = True

while not_solved:

    for k in range(0,EQ_num+1):
        print(rows[k])
    print("")



    P_row = []
    for i in range(0,len(rows[-1])-1):
        P_row.append(rows[-1][i])

    most_negative = min(filter(lambda x: x < 0, P_row), default=0)

    if most_negative >= 0:
        not_solved=False
    pivot_column = rows[-1].index(most_negative)
    theta_values = []



    for h in range(0,EQ_num):

        if rows[h][pivot_column] ==0:
            theta_values.append(100000)
        else:
            theta_values.append(rows[h][-1]/rows[h][pivot_column])
    theta_value = min([i for i in theta_values if i > 0])

    pivot_row = theta_values.index(theta_value)
    EQC = rows[pivot_row]
    pivot = EQC[pivot_column]
    EQCRO = [] # possible simplification

    for q in range(0,kc):
        if EQC[q] == 0:
            EQCRO.append(EQC[q])
        else:
            EQCRO.append(EQC[q] / pivot)
            
    rows[pivot_row] = EQCRO

    for i in range (0,len(rows)):
        if i == pivot_row:
            continue
        else:     
            pivot_multiple1 = rows[i][pivot_column] / EQCRO[pivot_column] 
            for j in range (0,kc):               
                rows[i][j] -= (pivot_multiple1 * EQCRO[j])



NP_row = []
for i in range(0,len(rows[-1])):
    if abs(rows[-1][i]) > 10000:
        result = round(rows[-1][i] / M, 2)
        remainder = rows[-1][i] - M*result
        NP_row.append(str(result) + "M + " + str(remainder))
    else:
        NP_row.append(rows[-1][i])

for k in range(0,EQ_num):
    print(rows[k])
print(NP_row)
