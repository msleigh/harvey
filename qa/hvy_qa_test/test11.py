## @brief Comparison with the output of a difference implementation of the same
## numerical scheme
##
## Compare implicit solution, theta = 1.


import matplotlib.pyplot as plt
import numpy as np
import qa_utils


def test11():

    testname = "test11"

    # Clear the figure
    plt.clf()

    # Get the numerical solution
    (f, nnodes, x) = qa_utils.run_harvey(testname)

    # Plot the initial condition
    # --------------------------

    T0 = 1.0  # The initial temperature (constant in x)
    L = np.pi  # The length of the bar
    D = 1.0  # Diffusion coefficient

    dx = x[1] - x[0]
    ncells = int(L / dx)
    assert ncells == 40

    phi = np.zeros(nnodes)
    phiFS = np.zeros(nnodes)

    phi[:] = 0.0
    phi[0] = T0
    phi[-1] = 0.0

    # plt.plot(x,phi,'b-',lw=2)
    # plt.show()

    # Plot the initial condition using its Fourier series representation
    # ------------------------------------------------------------------

    phiFS0 = T0 * (1 - x / L)

    cnst = -2.0 * T0 / np.pi

    # Next 5 terms
    for iterm in range(1, 500):
        n = iterm
        phiFS = phiFS + np.sin(n * np.pi * x / L) / n

    # plt.plot(x,phiFS0+cnst*phiFS,'r--',lw=2)
    # plt.show()

    # Plot the solution at later times
    # --------------------------------

    ttimes = [0.0, 5.0, 10.0, 15.0, 20.0, 40.0]
    # ttimes = [40.]
    ttimes = [0.0, 100.0, 160.0, 240.0, 320.0, 640.0]

    tmpstr = f.readline()

    tn = -1.0
    failed = False
    tol = 1.0e-00

    for tfac in ttimes:

        t = tfac * dx * dx / D

        while tn < t:
            if tmpstr == "":
                break
            tmpfld = tmpstr.split(None)
            tn = float(tmpfld[0])
            tmpstr = f.readline()
        un = np.array(tmpfld[1:], dtype=np.float64)

        uc = np.zeros(nnodes)
        for iterm in range(1, 5000):
            n = iterm
            uc = uc + (np.sin(n * np.pi * x / L) / n) * np.exp(-n * n * D * tn)
        uc = cnst * uc
        uc[-1] = 0.0
        uc = phiFS0 + uc
        uc = uc[::-1]

        plt.plot(x, uc, "b-", lw=2)
        plt.plot(x, un, "r--", lw=2)

        diff = np.zeros(nnodes)
        for i, uni in enumerate(un):
            if uni != 0.0:
                diff[i] = 100.0 * (uni - uc[i])

        if np.all(np.less_equal(abs(diff), abs(uc * tol))):
            pass
        else:
            failed = True
            print(
                "{0:2s} {1:23s} {2:23s} {3:23s} {4:23s} {5:23s} {6:23s}".format(
                    "j",
                    "x[j]",
                    "uc[j]",
                    "un[j]",
                    "diff[j]",
                    "uc[j]*tol",
                    "np.less_equal(diff[j], uc[j]*tol)",
                )
            )
            for j in range(nnodes):
                print(
                    "{0:2d} {1:23.16e} {2:23.16e} {3:23.16e} {4:23.16e} {5:23.16e} {6}".format(
                        j,
                        x[j],
                        uc[j],
                        un[j],
                        abs(diff[j]),
                        abs(uc[j] * tol),
                        np.less_equal(abs(diff[j]), abs(uc[j] * tol)),
                    )
                )
            break

    plt.xlim(0.0, np.pi)
    plt.savefig(testname + ".png", format="png", bbox_inches="tight")

    assert failed == False

    return True
