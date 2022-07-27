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
import qa_utils


def test16():

    testname = "test16"

    # Clear the figure
    plt.clf()

    # Get the numerical solution
    (fn, nnodes, x) = qa_utils.run_harvey(testname)

    fc = open("./1DHeatEquation/solution.txt")
    (nnodes2, x2) = qa_utils.read_nodes(fc)

    assert nnodes == nnodes2, "Number of nodes from two data files are not the same"
    assert any(x - x2 < 1.0e-15 * x), "X-values from two data files are not the same"

    # Pick a set of times to plot the results (number of time-steps)
    ttimes = [333, 666, 999]

    tmpstrn = "0"
    tmpstrc = "0"
    tn = -1.0
    tc = -1.0
    dt = 0.001

    # Cycle throught the times at which to plot the solution
    for tfac in ttimes:

        t = tfac * dt

        # Read through the output file (from where we left off last time)
        # until the first data line with time >= the chosen time is found
        while tn < t:
            if tmpstrn == "":
                break
            tmpfldn = tmpstrn.split(None)
            tn = float(tmpfldn[0])
            tmpstrn = fn.readline()

        # Extract the numerical solution at this time from the data file
        un = np.array(tmpfldn[1:], dtype=np.float64)

        while tc < t:
            if tmpstrc == "":
                break
            tmpfldc = tmpstrc.split(None)
            tc = float(tmpfldc[0])
            tmpstrc = fc.readline()

        # Extract the reference solution at this time from the data file
        # Reverse the vector because this is the solution for a problem with the boundary
        # conditons the other way round...
        uc = np.array(tmpfldc[1:][::-1], dtype=np.float64)

        print("Plotting...", tfac, t, tn, tc)
        plt.plot(x, uc, "b-", lw=2.0)
        plt.plot(x, un, "r--", lw=2.0)

        diff = 100.0 * abs(un - uc)

        # Perform checks
        print()
        print("Performing checks...")

        # Define the two tolerances for x < 10 and x < 5
        tol = 1.0e-12

        failed = qa_utils.has_failed(uc, diff, tol)
        if failed:
            qa_utils.dump(nnodes, x, uc, un, diff, tol)
        assert failed == False

    plt.savefig(testname + ".png", format="png", bbox_inches="tight")

    return True
