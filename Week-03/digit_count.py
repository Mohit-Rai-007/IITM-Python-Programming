import sympy as sp

# Define the matrices
T_std = sp.Matrix([[4, 7],
                   [5, 8]])

P_gamma = sp.Matrix([[2, 3],
                     [1, 1]])

P_beta = sp.Matrix([[1, 1],
                    [0, 1]])

# Compute the inverses
P_gamma_inv = P_gamma.inv()
P_beta_inv = P_beta.inv()
print(P_beta_inv)