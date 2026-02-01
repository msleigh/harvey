## @brief
##
## Compare implicit solution, theta = 0.5


import matplotlib.pyplot as plt
import numpy as np
import qa_utils


def test14():
    testname = "test14"

    # Clear the figure
    plt.clf()

    # Get the numerical solution
    (f, nnodes, x) = qa_utils.run_harvey(testname)

    # Plot the initial condition
    # --------------------------

    H = 1.0  # The incoming flux
    L = np.pi  # The length of the bar
    D = 1.0  # Diffusion coefficient

    dx = x[1] - x[0]
    ncells = int(round(L / dx))

    w = H * x / D
    plt.plot(x, w, "k--")

    assert ncells == 50, "Wrong number of cells: " + str(ncells)

    print("Number of nodes = ", nnodes)

    # Plot the solution at later times
    # --------------------------------

    # Pick a set of times to plot the results (number of time-steps)
    ttimes = [0, 1000, 2000, 4000, 8000, 9999, 24999]

    # Read the header line in the numerical solution output file
    tmpstr = f.readline()

    tn = -1.0
    failed = False
    tol = 1.0e-00

    pix2l = 0.5 * x  # Assumes L = pi
    phiFS0 = H * x / D
    cnst = -8.0 * H / (D * np.pi)  # Assumes L = pi

    # Cycle throught the times at which to plot the solution
    for tfac in ttimes:
        # Convert to an actual time by multiplying by time-step length
        t = tfac * dx * dx / (6.0 * D)

        # Read through the output file (from where we left off last time) until the
        # first data line with time >= the chosen time is found
        while tn < t:
            if tmpstr == "":
                break
            tmpfld = tmpstr.split(None)
            tn = float(tmpfld[0])
            tmpstr = f.readline()

        print(tfac, tn)

        # Extract the numerical solution at this time from the data file
        un = np.array(tmpfld[1:], dtype=np.float64)

        # Calculate the analytic solution at this time
        uc = np.zeros(nnodes)

        # Calculate the sum in the analytic solution
        for iterm in range(1, 5000):
            # Odd terms only
            if iterm % 2 != 0:
                it2 = iterm * iterm
                k = float((-1) ** ((iterm - 1) / 2)) / it2
                uc = uc + k * np.sin(iterm * pix2l) * np.exp(
                    -0.25 * it2 * D * tn
                )  # Assumes L = pi

        # Multiply the sum by the appropriate constant
        uc = cnst * uc
        # uc[-1] = 0.

        # Add on the initial term (the solution at t = \infty)
        uc = phiFS0 + uc

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
    plt.ylim(-0.1, H * L / D)
    plt.savefig(testname + ".png", format="png", bbox_inches="tight")

    assert not failed

    return True
