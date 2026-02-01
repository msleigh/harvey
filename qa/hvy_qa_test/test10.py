## @brief Analytic solution of a semi-infinite bar - explicit
##
## Analytic solution for a semi-infinite bar/slab (plane geometry)
## with the left boundary held constant at 100 (u(0,t) = 100), and
## initial value of zero everywhere (u(x,0) = 0). Because the anal-
## ytic solution is applicable to an infinite bar, the error in the
## finite numerical solution increases with x. Compare for every
## cell at the final time-step only.
##
## Compare explicit solution, theta = 0.


import matplotlib.pyplot as plt
import numpy as np
import qa_utils as qu
from scipy import special  # For error function, erf


def test10():

    testname = "test10"

    # Get numerical solution
    (x, ntim, nval) = qu.get_harvey(testname)

    plt.clf()
    plot_times = [100, -1]  # Times to plot (number of time-steps)

    # Let D = 1
    dcon = 1.0

    # Define the two tolerances for x < 10 and x < 5
    tol1 = 1.0
    tol2 = 0.3

    nnodes = len(x)

    for tp in plot_times:

        t = ntim[tp]
        lab = 't\'={:.6f} (step {:d})'.format(t, tp)

        # Analytic solution
        c1 = 1.0 / np.sqrt(4.0 * dcon * t)
        uc = 100.0 * (1.0 - special.erf(x * c1))

        # Numerical solution
        un = nval[tp,:]

        if tp in plot_times:
            plt.plot(x, uc, "b-", lw=2, label=lab+' (ref)')
            plt.plot(x, un, "r--", lw=2, label=lab)

        diff1 = qu.diff(un, uc, 0.75)
        diff2 = qu.diff(un[0:48], uc[0:48])

        try:
            assert(qu.passed(un, uc, diff1, tol1))
        except AssertionError:
            qu.dump(nnodes, x, uc, un, diff1, tol1)
            raise

        failed = qu.has_failed(uc[0:48], diff2, tol2)
        if failed:
            qu.dump(nnodes, x, uc, un, diff2, tol2)
        assert not failed

    #plt.plot(x, diff, "g-", lw=2.0)
    #plt.plot(x,diff1,'y--',lw=2.)
    #plt.xlim((0.0, 0.4))
    #plt.yscale('log')
    #plt.ylim((1.0e-04, 1.0e02))
    plt.xlabel('$x$ (cm)')
    plt.ylabel('$\phi(x,t\')$')
    plt.legend(bbox_to_anchor=(1,1), loc="upper left")
    plt.savefig(testname + ".png", format="png", bbox_inches="tight")

    return True
