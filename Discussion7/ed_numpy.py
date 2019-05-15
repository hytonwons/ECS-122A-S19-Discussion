import numpy as np

# A DP program to solve edit distance problem
def editDistDP(x, y):
    m = len(x);
    n = len(y);
    # Create an e-table to store results of subproblems
    e = np.zeros((m+1, n+1), dtype=int)

    # Fill in e[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):
            # Initialization
            if i == 0:
                e[i][j] = j
            elif j == 0:
                e[i][j] = i
            elif x[i-1] == y[j-1]:
                e[i][j] = min(1 + e[i-1][j], 1 + e[i][j-1], e[i-1][j-1])
            else:
                e[i][j] = 1 + min(e[i-1][j], e[i][j-1], e[i-1][j-1])

    return e[m][n]
    # return e

# Test case 1
# x = "snowy"
# y = "sunny"

# Test case 2
x = "heroically"
y = "scholarly"

print(editDistDP(x, y))
