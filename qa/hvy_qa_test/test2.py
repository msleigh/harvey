## @brief Comparison with analytic solution, sinusoidal initial condition
##
## Comparison with analytic solution for sinusoidal initial condition,
## u(x,0) = sin(pi.x/L), and boundary conditions u(0,t) = u(L,t) = 0. Planar geometry,
## implicit solution, dx = 1cm, dt = dx^2/6D, D = 1, t_max = 0.25. Compare
## at every time-step, plot at t = t_max.
##
## Compare implicit solution, theta = 1.


import numpy as np
import qa_utils as qu


def analytic_solution(x, t):
    dcon = 1.0  # Diffusion coefficient
    a = 1.0  # Central position of sinusoidal initial condition
    length = x[-1] - x[0]
    const = -np.pi * np.pi * dcon / (length * length)
    ic = a * np.sin(np.pi * x / length)
    uc = ic * np.exp(const * t)
    return uc


def test2():
    testname = "test2"
    tol = 5.0e-04
    plot_times = [3000, 15000]
    qu.run_test(testname, analytic_solution, plot_times, tol)
    return True
