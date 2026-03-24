def create_tableau(eq_num, var_num):
    tableau = []
    for a in range (0,eq_num+1):
        appendable = []
        print("row ",a )

        for _ in range (0,var_num+1):
            x = int(input(":"))
            appendable.append(x)
        tableau.append(appendable)

    for c in range (0,eq_num):
        for _ in range (0,eq_num-1):
            tableau[c].insert(-1,0)

    for e in range (0,eq_num):
        tableau[e].insert(var_num+e,1)

    for _ in range (0,eq_num):
        tableau[-1].insert(-1,0)
    

    global basic_variables, slack_variables
    basic_variables = ["x" + str(i+1) for i in range(var_num)]
    slack_variables = ["s" + str(i+1) for i in range(eq_num)]

    return tableau


def change_basic_variable(initial_index,new_index):
    basic_variables[initial_index], basic_variables[new_index] = basic_variables[new_index], basic_variables[initial_index]

def solve(tableau):

    EQ_num = len(tableau) - 1
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

def print_solution(tableau):
    Eq_num = len(tableau) - 1
    for i in range(0,Eq_num):
        print(basic_variables[i], "=", tableau[i][-1])

if __name__ == "__main__":
    eq_num = int(input("Enter the number of equations: "))
    var_num = int(input("Enter the number of variables: "))
    tableau = create_tableau(eq_num, var_num)
    solve(tableau)
    print_solution(tableau)
