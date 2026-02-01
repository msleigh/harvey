## @brief Comparison with analytic solution, chevron initial condition
##
## Comparison with analytic solution for chevron initial condition,
## u(x,0) = {Cx      x<=pi/2
##          {C(pi-x) x>=pi/2
## and boundary conditions u(0,t) = u(L,t) = 0, L=pi, C=1. Planar geometry,
## explicit solution, dx = pi/20, dt = 5dx^2/11D, t_max = 40dx^2/D, D = 1. Compare
## at every time-step.
##
## Compare explicit solution, theta = 0.


import numpy as np
import qa_utils as qu


def analytic_solution(x, t):
    dcon = 1.0  # Diffusion coefficient
    C = 1.0  # Define the gradient of the slope
    const = 4.0 * C / np.pi
    uc = np.zeros(len(x))
    for iterm in range(1, 50):
        n = 2.0 * iterm - 1.0
        uc = uc + ((-1.0) ** (iterm - 1)) * (np.sin(n * x) / (n * n)) * np.exp(
            -n * n * dcon * t
        )
    uc = const * uc
    return uc


def test4():
    testname = "test4"
    tol = 0.5e-00
    plot_times = [5, 15, 40]
    qu.run_test(testname, analytic_solution, plot_times, tol)
    return True
