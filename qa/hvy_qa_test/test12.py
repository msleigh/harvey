## @brief Comparison with the output of a difference implementation of the same
## numerical scheme
##
## Compare explicit solution, theta = 0.


import matplotlib.pyplot as plt
import numpy as np
import qa_utils


def test12():

    testname = "test12"

    # Clear the figure
    plt.clf()

    # Get the numerical solution
    (x, ntim, nval) = qa_utils.get_harvey(testname)
    nnodes = len(x)
    if nval.size == 0:
        raise AssertionError(
            f"{testname} numerical solution output is empty. Check {testname}.log for solver output."
        )

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

    failed = False
    tol = 1.0e-00

    for tfac in ttimes:

        t = tfac * dx * dx / D

        tp = np.searchsorted(ntim, t, side="left")
        if tp >= len(ntim):
            raise AssertionError(
                f"{testname} expected time {t:.6f} exceeds available solution times "
                f"(last time {ntim[-1]:.6f})."
            )
        tn = ntim[tp]
        un = nval[tp, :]

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

        diff = np.abs(un - uc)

        failed = qa_utils.has_failed(uc, diff, tol)
        if failed:
            qa_utils.dump(nnodes, x, uc, un, diff, tol)
            break

    plt.xlim(0.0, np.pi)
    plt.savefig(testname + ".png", format="png", bbox_inches="tight")

    assert not failed

    return True
