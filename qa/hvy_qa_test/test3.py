## @brief Comparison with analytic solution, constant initial condition
##
## Comparison with analytic solution for constant initial condition, u(x,0) = C,
## and boundary conditions u(0,t) = u(L,t) = 0, for C = 1, L = pi. Planar geometry,
## implicit solution, dx = pi/20, dt = 5dx^2/11D, t_max = 40dx^2/D, D = 1. Compare
## at every time-step.
##
## Compare implicit solution, theta = 0.5


import numpy as np
import qa_utils as qu


def analytic_solution(x, t):
    dcon = 1.0  # Diffusion coefficient
    T0 = 1.0  # The initial temperature (constant in x)
    const = 4.0 * T0 / np.pi
    problem_size = x[0] + x[-1]
    uc = np.zeros(len(x))
    for iterm in range(1, 500):
        n = 2.0 * iterm - 1.0
        wavenumber = n * np.pi / problem_size
        uc = uc + (np.sin(wavenumber * x) / n) * np.exp(
            -wavenumber * wavenumber * dcon * t
        )
    uc = const * uc
    return uc


def test3():
    testname = "test3"
    tol = 1.0e-01
    plot_times = [100, 500, 2000, 8000]
    qu.run_test(testname, analytic_solution, plot_times, tol)
    return True
