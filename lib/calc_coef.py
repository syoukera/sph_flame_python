# Calclate coefficient of discretized equation
def calc_coef_steady(i, num_grid):
    
    # center boundary
    if i == 0:
        a_i = 1.00e+0
        b_i = 0.00e+0
        c_i = 0.00e+0
        d_i = 1.00e+0
        
    # outer boundary
    elif i == num_grid-1:
        a_i = 1.00e+0
        b_i = 0.00e+0
        c_i = 0.00e+0
        d_i = 0.00e+0
    
    # internal grids
    else:
        dx_e = x[i+1] - x[i]
        dx_w = x[i] - x[i-1]
    
        F = rho*u
        D_e = D_mass/dx_e
        D_w = D_mass/dx_w
    
        a_E = D_e + max(-F, 0)
        a_W = D_w + max(F, 0)
        a_P = a_E + a_W
        b   = 0
    
        a_i = a_P
        b_i = a_E
        c_i = a_W
        d_i = b
    
    return a_i, b_i, c_i, d_i

# Calclate coefficient of discretized equation
def calc_coef_implicit(i, num_grid):
    
    # center boundary
    if i == 0:
        a_i = 1.00e+0
        b_i = 1.00e+0
        c_i = 0.00e+0
        d_i = 0.00e+0
        
    # outer boundary
    elif i == num_grid-1:
        a_i = 1.00e+0
        b_i = 0.00e+0
        c_i = 1.00e+0
        d_i = 0.00e+0
    
    # internal grids
    else:
        dx_e = x[i+1] - x[i]
        dx_w = x[i] - x[i-1]
    
        F = rho*u
        D_e = D_mass/dx_e
        D_w = D_mass/dx_w
    
        a_E   = D_e + max(-F, 0)
        a_W   = D_w + max(F, 0)
        a_P_0 = rho*dx/dt
        a_P   = a_E + a_W + a_P_0
        b     = a_P_0*phi_sim[i]
    
        a_i = a_P
        b_i = a_E
        c_i = a_W
        d_i = b
    
    return a_i, b_i, c_i, d_i