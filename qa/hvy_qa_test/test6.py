##  @brief Analytic solution of a semi-infinite bar - Crank-Nicholson
##
## Analytic solution for a semi-infinite bar/slab (plane geometry)
## with the left boundary held constant at 100 (u(0,t) = 100), and
## initial value of zero everywhere (u(x,0) = 0). Because the anal-
## ytic solution is applicable to an infinite bar, the error in the
## finite numerical solution increases with x. Compare for every
## cell at the final time-step only.
##
## Compare implicit solution, theta = 0.5 (Crank-Nicolson).


import matplotlib.pyplot as plt
import numpy as np
import qa_utils as qu
from scipy import special  # For error function, erf

def test6():

    testname = "test6"

    # Get numerical solution
    (x, ntim, nval) = qu.get_harvey(testname)
    nnodes = len(x)

    # Clear the figure
    plt.clf()
    plot_times = [-1]

    dcon = 1.0

    for tp in plot_times:

        t = ntim[tp]

        c1 = 1.0 / np.sqrt(4.0 * dcon * t)
        uc = 100.0 * (1.0 - special.erf(x * c1))

        un = nval[tp,:]

        diff = 100.0 * abs(un - uc)
        diff1 = 100.0 * abs(un[0:99] - uc[0:99])

        plt.plot(x, uc, "b-", lw=2.0, label='$\phi(x,{:.6f})$'.format(t)+' (ref)')
        plt.plot(x, un, "r--", lw=2.0, label='$\phi(x,{:.6f})$'.format(t))
        plt.plot(x, 100.0*qu.diff(un, uc), "g-", lw=2.0, label='% error')

        # Define the two tolerances for x < 10 and x < 5
        tol1 = 1.5
        tol2 = 0.025

        failed = qu.has_failed(uc, diff, tol1)
        if failed:
            qu.dump(nnodes, x, uc, un, diff, tol1)
        assert failed == False

        failed = qu.has_failed(uc[0:99], diff1, tol2)
        if failed:
            qu.dump(nnodes, x, uc, un, diff1, tol2)
        assert failed == False

    plt.xlim((0.0, 0.4))
    # plt.yscale('log')
    plt.ylim((1.0e-04, 1.0e02))
    plt.xlabel('$x$ (cm)')
    plt.ylabel('Value')
    plt.legend()

    plt.savefig(testname + ".png", format="png", bbox_inches="tight")

    return True
