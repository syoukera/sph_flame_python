import numpy as np
import time

def calc_tdam(phi, calc_coef, num_grid):
    P = np.zeros(num_grid)
    Q = np.zeros(num_grid)
    
    start_time = time.time()

    # step 1: calculate P[0] and Q[0]
    a_0, b_0, c_0, d_0 = calc_coef(0, num_grid)
    P[0] = b_0/a_0
    Q[0] = d_0/a_0

    # step 2: calculate P[i] and Q[i]
    for i in range(1,num_grid):
        # call coefficent calculation
        a_i, b_i, c_i, d_i = calc_coef(i, num_grid)
    
        P[i] = b_i/(a_i - c_i*P[i-1])
        Q[i] = (d_i + c_i*Q[i-1])/(a_i - c_i*P[i-1])

    # step 3: substitute Q[N] to phi[N]
    phi[num_grid-1] = Q[num_grid-1]

    # step 4: calcrate phi[i]
    for i in reversed(range(num_grid-1)):
        phi[i] = P[i]*phi[i+1] + Q[i]
        
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Elapsed time is {elapsed_time} s')