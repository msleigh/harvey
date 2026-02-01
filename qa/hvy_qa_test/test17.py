## @brief Comparison with analytic solution, cosinusoidal initial condition
##
## Comparison with analytic solution for cosinusoidal initial condition,
## u(x,0) = cos(pi.x/(2L)), and boundary conditions du/dx(0,t) = 0 (Neumann),
## u(L,t) = 0 (Dirichlet). Planar geometry, Crank-Nicolson scheme (theta=0.5),
## L = 0.5, dx = 0.01, dt = dx^2/6D, D = 1, t_max = 1000*dt. Compare
## at every time-step, plot at t = t_max.
##
## The eigenfunction for Neumann-Dirichlet BCs is cos((2n-1)*pi*x/(2L)),
## with eigenvalue ((2n-1)*pi/(2L))^2. For n=1: cos(pi*x/(2L)), eigenvalue (pi/(2L))^2.


import matplotlib.pyplot as plt
import numpy as np
import qa_utils


def test17():

    testname = "test17"

    # Clear the figure
    plt.clf()

    # Get the numerical solution
    (f, nnodes, x) = qa_utils.run_harvey(testname)

    print("\nAllocating arrays...")
    un = np.zeros(nnodes, dtype=np.float64)
    uc = np.zeros(nnodes, dtype=np.float64)

    # Set up the problem parameters for the analytic solution
    # These need to match the parameters in the input file for
    # the numerical solution
    print("\nSetting up analytic solution...")
    dcon = 1.0
    length = x[-1] - x[0]
    invlength = 1.0 / length
    tol = 0.25e-01

    a = 1.0
    # For Neumann-Dirichlet BCs, eigenvalue is (pi/(2L))^2
    const = -0.25 * np.pi * np.pi * dcon * invlength * invlength

    # Initial condition: cos(pi*x/(2L))
    ic = a * np.cos(0.5 * np.pi * x * invlength)
    ic[-1] = 0.0  # Enforce Dirichlet BC at x=L

    # Read the first line for t = 0
    tmpstr = f.readline()

    failed = False

    # Read to the very end - last time-step
    while tmpstr != "":
        tmpfld = tmpstr.split(None)
        t = float(tmpfld[0])

        uc = ic * np.exp(const * t)

        if t == 0.0:
            assert all(uc == ic)

        un = np.array(tmpfld[1:], dtype=np.float64)

        diff = 100.0 * abs(un - uc)

        if np.all(np.less_equal(diff, uc * tol)):
            pass
        else:
            failed = True
            for j in range(nnodes):
                print(j, x[j], uc[j], un[j], diff[j], uc[j] * tol, np.less_equal(diff[j], uc[j] * tol))
            break

        tmpstr = f.readline()

    print("\nPlotting...")
    plt.plot(x, uc, "b-", lw=2.0)
    plt.plot(x, un, "r--", lw=2.0)
    # plt.plot(x,diff,'g-',lw=2.)
    # plt.show()
    plt.savefig(testname + ".png", format="png", bbox_inches="tight")

    assert failed == False

    return True
