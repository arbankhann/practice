import numpy as np

P_A = np.array(0.2)
P_B_given_A = np.array(0.85)
P_B = np.array(0.25)

P_A_given_B = (P_B_given_A * P_A) / P_B

print("P(A|B) =", P_A_given_B)