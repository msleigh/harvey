## @brief Comparison with analytic solution, sinusoidal initial condition
##
## Comparison with analytic solution for sinusoidal initial condition,
## u(x,0) = sin(pi.x/L), and boundary conditions u(0,t) = u(L,t) = 0. Planar geometry,
## explicit solution, dx = 1cm, dt = dx^2/6D, D = 1, t_max = 0.25. Compare
## at every time-step, plot at t = t_max.
##
## Compare implicit solution, theta = 0.5


import matplotlib.pyplot as plt
import numpy as np
import qa_utils


def test15():

    testname = "test15"

    # Clear the figure
    plt.clf()

    # Get numerical solution
    (f, nnodes, x) = qa_utils.run_harvey(testname)

    print("\nAllocating arrays...")
    un = np.zeros(nnodes, dtype=np.float64)
    uc = np.zeros(nnodes, dtype=np.float64)

    # Set up the problem parameters for the analytic solution
    # These need to match the parameters in the input file for
    # the numerical solution
    print("\nSetting up analytic solution...")
    dcon = 1.0
    invlength = 1.0
    tol = 0.25e-01

    a = 1.0
    const = -np.pi * np.pi * dcon * invlength * invlength

    # Initial condition
    ic = a * np.sin(np.pi * x * invlength)
    ic[0] = 0.0
    # ic[-1] = 0.
    # print 'Is this 0',np.sin(np.pi*x[-1]*invlength)
    # print 'Is this 1',x[-1]*invlength
    # plt.plot(x,ic,'k-', lw=2.)

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

        tmpstr = f.readline()

    print("\nPlotting...")
    plt.plot(x, uc, "b-", lw=2.0)
    plt.plot(x, un, "r--", lw=2.0)
    # plt.plot(x,diff,'g-',lw=2.)
    # plt.show()
    plt.savefig(testname + ".png", format="png", bbox_inches="tight")

    assert failed == False

    return True
