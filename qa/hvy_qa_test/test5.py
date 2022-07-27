## @brief Comparison with the output of a different implementation of the same
## numerical scheme
##
## Solution from alternative implementation of explicit numerical scheme.
## 1000 time-steps, 10 cells. Finite bar/slab with left boundary held constant
## at 100 (u(0,t) = 100) and initial value of zero everywhere (u(x,0) = 0).
## Right-hand boundary is Neuman condition du/dx = 0. Compare for every
## cell and every time-step.
##
## Compare explicit solution, theta = 0.


import matplotlib.pyplot as plt
import numpy as np
import qa_utils as qu


def test5():

    testname = "test5"

    # Get numerical solution
    (x, ntim, nval) = qu.get_harvey(testname)

    tol = 0.085  # %

    # Get reference solution
    refdat = np.genfromtxt("./1DHeatEquation/solution.txt")
    rtim = refdat[:, 0]
    rval = refdat[:, 1:]

    plt.clf()
    plot_times = [333, 666, 999]  # Times to plot (number of time-steps)

    # Cycle through times at which to plot solution
    for tp in plot_times:

        t = ntim[tp]
        lab = 't\'={:.6f} (step {:d})'.format(t, tp)

        uc = rval[tp,:]

        un = nval[tp,:]

        if tp in plot_times:
            plt.plot(x, uc, "b-", lw=2, label=lab+' (ref)')
            plt.plot(x, un, "r--", lw=2, label=lab)

        diff = qu.diff(un, uc)

        try:
            assert(qu.passed(un, uc, diff, tol) == True)
        except AssertionError as error:
            qu.dump(len(x), x, uc, un, diff, tol)
            raise

    plt.xlabel('$x$ (cm)')
    plt.ylabel('$\phi(x,t\')$')
    plt.legend(bbox_to_anchor=(1,1), loc="upper left")
    plt.savefig(testname + ".png", format="png", bbox_inches="tight")

    return True
