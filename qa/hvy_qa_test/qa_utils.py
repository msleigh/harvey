import matplotlib.pyplot as plt
import numpy as np

import harvey


def run_test(testname, analytic_solution, plot_times, tol):

    # Get numerical solution
    (x, ntim, nval) = get_harvey(testname)

    # Initial condition
    ic = analytic_solution(x, 0)
    plt.clf()
    plt.plot(x, ic, "k--", label="Initial condition")

    for tp, t in enumerate(ntim):

        uc = analytic_solution(x, t)

        un = nval[tp,:]

        if tp in plot_times:
            lab = 't\'={:.6f} (step {:d})'.format(t, tp)
            plt.plot(x, uc, "b-", lw=2, label=lab+' (ref)')
            plt.plot(x, un, "r--", lw=2, label=lab)
            #plt.plot(x, 100.0*diff, "g-", lw=2, label="% error")

        df = diff(un, uc)

        try:
            assert passed(un, uc, df, tol)
        except AssertionError as error:
            dump(len(x), x, uc, un, df, tol)
            raise

    plt.xlabel('$x$ (cm)')
    plt.ylabel('$\phi(x,t\')$')
    plt.legend(bbox_to_anchor=(1,1), loc="upper left")
    plt.annotate('tolerance\n= {:.1e}'.format(tol), xy=(0.8, np.max(nval)),
            horizontalalignment='left', verticalalignment='bottom',
            )
    plt.savefig(testname + ".png", format="png", bbox_inches="tight")

    return


def run_harvey(testname):
    """Get numerical solution."""
    print("\nRunning code...")
    harvey.main(testname + "_in", testname + ".out", False)

    # Open output file
    fff = open(testname + ".out", "r")

    # Get nodes in the numerical solution from the output data file
    print("\nReading number of nodes...")
    (nnodes, xvals) = read_nodes(fff)

    return (fff, nnodes, xvals)


def get_harvey(testname):
    """Get numerical solution."""
    print("\nGetting numerical solution...")

    _, _, x = run_harvey(testname)

    # Open the output file
    harveydat = np.genfromtxt(testname + ".out")
    time = harveydat[:, 0]
    soln = harveydat[:, 1:]

    return (x, time, soln)


def read_nodes(fff):
    """Get nodes from data file."""
    # First line is a comment/header line listing the x values of the nodes
    tokens = fff.readline().split(None)

    # Ignore first two tokens which are "#", "x"
    nnodes = len(tokens) - 2

    # Set up array of nodal x-values
    xvals = np.zeros(nnodes)

    # Read node x-values
    for inode in range(nnodes):
        xvals[inode] = float(tokens[inode + 2])

    return (nnodes, xvals)


def diff(un, uc, minval=0):
    d = np.zeros_like(uc)
    np.divide(un - uc, uc, out=d, where=uc > minval)
    return d

def has_failed(reference, difference, tolerance):
    """Abstract the definition of failure."""
    # Return True if failed
    return np.all(np.greater(difference, reference * tolerance))


def passed(un, uc, diff, tolerance):
    """Abstract the definition of failure."""
    # Return True if passed
    # Test diff explicitly against tol rather than using e.g. allclose to
    # compare un and uc directly, to give more control over diff (elsewhere)
    return np.less_equal(diff, tolerance).all()


def dump(nnodes, xvals, uc, un, diff, tol):
    """Dump the data out to screen for debugging."""
    assert len(xvals) == nnodes
    assert len(uc) == nnodes
    assert len(un) == nnodes
    assert len(diff) == nnodes

    print(
        "{0:2s} {1:23s} {2:23s} {3:23s} {4:23s} {5:23s} {6:23s}".format(
            "j",
            "xvals[j]",
            "uc[j]",
            "un[j]",
            "diff[j]",
            "*tol",
            "np.less_equal(diff[j], tol)",
        )
    )
    for j in range(nnodes):
        print(
            "{0:2d} {1:23.16e} {2:23.16e} {3:23.16e} {4:23.16e} {5:23.16e} {6}".format(
                j,
                xvals[j],
                uc[j],
                un[j],
                abs(diff[j]),
                tol,
                np.less_equal(abs(diff[j]), tol),
            )
        )
