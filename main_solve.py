import numpy as np
import math
import matplotlib.pyplot as plt

from lib/calc_coef import calc_coef_steady
from lib/calc_coef import calc_coef_implicit
from lib/calc_tdam import calc_tdam

def main():
    print("hello world!")

    # define schalar
    D_mass      = 1.00e+0
    rho         = 1.00e+0
    u           = 1.00e+0
    
    # define grid scale
    total_length = 1.00e+0
    num_grid     = 101
    dx           = total_length/(num_grid-1)
    
    # define time scale
    start_time      = 0.00e+0
    end_time        = 1.00e+0
    dt              = 1.00e-3
    
    # define boundary value
    phi_0 = 1.00e+0
    phi_L = 0.00e+0

    # set grid posisions
    x = np.linspace(0, total_length, num=num_grid)
    # set inital phi
    phi_sim = np.zeros(num_grid)
    phi_sim[0:int(0.2*num_grid)] = 1.00e0

    calc_tdam(phi_sim, calc_coef_steady, num_grid)

    plt.plot(x, phi_ana, label='ana')
    plt.plot(x, phi_sim,  label='sim')
    plt.legend()
    plt.show()
    

if __name__ == "__main__":
    main()