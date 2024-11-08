import numpy as np

def multiple_disk_clutch_brake(x):
    """
    Multiple disk clutch brake optimization problem
    """
    # Problem constants
    rho = 7.85e-6  # Density of the material (kg/mm³)
    Mh = 1000      # Maximum torque (Nm)
    prz = 1        # Maximum pressure (MPa)
    Vsr = 10       # Maximum sliding velocity (m/s)
    mu = 0.5       # Coefficient of friction
    s = 1.5        # Safety factor
    N = 250        # RPM
    pi = np.pi

    # Extract design variables
    ri, ro, t, F, n = x
    n = round(n)
    
    # Objective function (minimize clutch brake mass)
    fx = pi * (ro**2 - ri**2) * t * n * rho
    
    # Constraints
    g1 = (ro - ri) - 20 
    g2 = prz - (F / (pi * (ro**2 - ri**2))) 
    g3 = Vsr - (2 * pi * ro * N / 60) 
    g4 = 2.5 * (ro + ri) - (ro - ri)  
    g5 = F - s * Mh / (mu * n * (ro + ri) / 2)  
    g6 = t - 3  
    g7 = 0.25 - t 
    
    # Penalty function
    penalty = 0
    constraints = [g1, g2, g3, g4, g5, g6, g7]
    penalty_factor = 1e6
    
    for g in constraints:
        if g > 0:  # Constraint violation
            penalty += penalty_factor * g**2
    
    return fx + penalty

benchmark_functions = {
    "Multiple Disk Clutch Brake": {
        "function": multiple_disk_clutch_brake,
        "DIMENSION": 5,
        "LOWER_BOUND": [60, 75, 0.25, 1000, 2],
        "UPPER_BOUND": [80, 95, 3, 3000, 9],
        "GLOBAL_OPTIMUM": 0,
        "is_constrained": True,
        "can_plot_3d": False
    },
}