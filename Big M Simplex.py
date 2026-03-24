M = 10000000000

def create_tableau(eq_num, var_num, a_num):
    tableau = []
    for a in range(0, eq_num + 1):
        appendable = []
        print("row ", a)

        for _ in range(0, var_num + 1):
            x = int(input(":"))
            appendable.append(x)
        tableau.append(appendable)

    # Insert slack variables (identity matrix for <= constraints)
    for c in range(0, eq_num):
        for _ in range(0, eq_num - 1):
            tableau[c].insert(-1, 0)

    for e in range(0, eq_num):
        tableau[e].insert(var_num + e, 1)

    # Insert 0s in objective row for slack columns
    for _ in range(0, eq_num):
        tableau[-1].insert(-1, 0)

    # Insert columns for artificial variables
    for row_idx in range(0, eq_num):
        for _ in range(0, a_num - 1):
            tableau[row_idx].insert(-1, 0)

    # Mark which rows have artificial variables
    A_rows = []
    for _ in range(0, a_num):
        tvar = int(input("Artificial variable row: "))
        A_rows.append(tvar)

    # Add artificial variables to tableau (columns with 1s in specific rows)
    for num in A_rows:
        for a in range(0, len(A_rows)):
            tableau[num].insert(-2 + a, 1)

    global basic_variables, slack_variables, artificial_variables
    basic_variables = ["x" + str(i + 1) for i in range(var_num)]
    slack_variables = ["s" + str(i + 1) for i in range(eq_num)]
    artificial_variables = ["a" + str(i + 1) for i in range(a_num)]

    return tableau


def change_basic_variable(initial_index, new_index):
    basic_variables[initial_index], basic_variables[new_index] = (
        basic_variables[new_index],
        basic_variables[initial_index],
    )


def solve(tableau):
    eq_num = len(tableau) - 1
    var_num = len(basic_variables)
    a_num = len(artificial_variables)
    kc = 2 * var_num + a_num + 1
    unsolved = True

    while unsolved:
        for k in range(0, eq_num + 1):
            print(tableau[k])
        print("")

        P_row = []
        for i in range(0, len(tableau[-1]) - 1):
            P_row.append(tableau[-1][i])

        most_negative = min(filter(lambda x: x < 0, P_row), default=0)

        if most_negative >= 0:
            unsolved = False
            print("Solved!")
            continue

        pivot_column = tableau[-1].index(most_negative)
        theta_values = []

        for h in range(0, eq_num):
            if tableau[h][pivot_column] == 0:
                theta_values.append(100000)
            else:
                theta_values.append(tableau[h][-1] / tableau[h][pivot_column])

        theta_value = min([i for i in theta_values if i > 0])
        pivot_row = theta_values.index(theta_value)
        EQC = tableau[pivot_row]
        pivot = EQC[pivot_column]
        EQCRO = []

        for q in range(0, kc):
            if EQC[q] == 0:
                EQCRO.append(EQC[q])
            else:
                EQCRO.append(EQC[q] / pivot)

        tableau[pivot_row] = EQCRO

        for i in range(0, len(tableau)):
            if i == pivot_row:
                continue
            else:
                pivot_multiple1 = tableau[i][pivot_column] / EQCRO[pivot_column]
                for j in range(0, kc):
                    tableau[i][j] -= pivot_multiple1 * EQCRO[j]


def extract_big_m_row(tableau, M):
    NP_row = []
    for i in range(0, len(tableau[-1])):
        if abs(tableau[-1][i]) > 10000:
            result = round(tableau[-1][i] / M, 2)
            remainder = tableau[-1][i] - M * result
            NP_row.append(str(result) + "M + " + str(remainder))
        else:
            NP_row.append(tableau[-1][i])
    return NP_row


def print_solution(tableau):
    eq_num = len(tableau) - 1
    print("\nFinal Tableau:")
    for k in range(0, eq_num + 1):
        print(tableau[k])

    NP_row = extract_big_m_row(tableau, M)
    print("\nObjective function (Big-M form):")
    print(NP_row)

    print("\nBasic Variables:")
    for i in range(0, eq_num):
        print(basic_variables[i], "=", tableau[i][-1])


if __name__ == "__main__":
    eq_num = int(input("Enter the number of equations: "))
    var_num = int(input("Enter the number of variables: "))
    a_num = int(input("Enter the number of artificial variables: "))

    tableau = create_tableau(eq_num, var_num, a_num)
    solve(tableau)
    print_solution(tableau)
