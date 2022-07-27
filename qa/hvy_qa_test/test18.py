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


import matplotlib.pyplot as plt
import numpy as np
import qa_utils


def test18():

    testname = "test18"

    # Clear the figure
    plt.clf()

    # Get the numerical solution
    (f, nnodes, x) = qa_utils.run_harvey(testname)

    # Plot the initial condition
    # --------------------------

    C = 1.0  # Define the gradient of the slope
    L = x[-1] - x[0]  # The length of the bar
    A = 0.5 * C * L  # The amplitude/maximum temperature
    D = 1.0  # Diffusion coefficient

    ncells = 20
    dx = x[1] - x[0]

    phi = np.zeros(nnodes)
    phiFS = np.zeros(nnodes)

    for inode in range(ncells // 2 + 1):
        print(inode, x[inode])
        phi[inode] = C * x[inode]

    for inode in range(ncells // 2 + 1, ncells + 1):
        print(inode, x[inode])
        phi[inode] = C * (L - x[inode])

    plt.plot(x, phi)

    # Plot the initial condition using its Fourier series representation
    # ------------------------------------------------------------------

    cnst = 4.0 * C / np.pi

    # Next 5 terms
    for iterm in range(1, 50):
        n = 2.0 * iterm - 1.0
        phiFS = phiFS + ((-1.0) ** (iterm - 1)) * (np.sin(n * x) / (n * n))

    plt.plot(x, cnst * phiFS, "r--")

    # Plot the solution at later times
    # --------------------------------

    ttimes = [0.0, 5.0, 10.0, 15.0, 20.0, 40.0]

    tmpstr = f.readline()

    tn = -1.0
    failed = False
    tol = 0.5e-00

    for tfac in ttimes:

        t = tfac * dx * dx / D

        uc = np.zeros(nnodes)
        for iterm in range(1, 50):
            n = 2.0 * iterm - 1.0
            uc = uc + ((-1.0) ** (iterm - 1)) * (np.sin(n * x) / (n * n)) * np.exp(
                -n * n * D * t
            )
        uc = cnst * uc
        uc[-1] = 0.0
        plt.plot(x, uc, "b-")

        if tmpstr == "":
            break

        while tn < t:
            tmpfld = tmpstr.split(None)
            tn = float(tmpfld[0])
            tmpstr = f.readline()
        print("t = ", t, tn)
        un = np.array(tmpfld[1:], dtype=np.float64)
        plt.plot(x, un, "r--")

        diff = 100.0 * (un - uc)

        failed = qa_utils.has_failed(uc, diff, tol)

        if failed:
            for j in range(nnodes):
                print(
                    j,
                    x[j],
                    uc[j],
                    un[j],
                    diff[j],
                    uc[j] * tol,
                    np.less_equal(diff[j], uc[j] * tol),
                )
            break

    plt.xlim(0.0, np.pi)
    plt.ylim(0.0, 0.5 * np.pi)
    plt.savefig(testname + ".png", format="png", bbox_inches="tight")

    assert failed == False

    return True
