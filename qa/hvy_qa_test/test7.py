##  @brief Analytic solution for a delta function in an infinite bar
##
##  Analytic solution for a delta function at x = 0 in an infinite bar/slab.
##  For a delta function at time zero, the solution at t > 0 is a Gaussian,
##  u(x,t) = (1/sqrt(4pi.Dt)) * exp[-x^2/4Dt].


import matplotlib.pyplot as plt
import numpy as np
import qa_utils


def test7():

    testname = "test7"

    # Get numerical solution
    (x, ntim, nval) = qa_utils.get_harvey(testname)
    nonfinite_mask = ~np.isfinite(nval)
    if np.any(nonfinite_mask):
        bad_steps = np.where(np.any(nonfinite_mask, axis=1))[0]
        sample_steps = bad_steps[:5]
        raise AssertionError(
            f"{testname} numerical solution contains non-finite values at steps "
            f"{sample_steps.tolist()} (showing up to 5). Check {testname}.log for solver output."
        )

    print("\nPlotting...")
    plt.clf()
    plot_times = [63, 250, 1000]
    rel_l2_tol = 0.15
    # Let D = 1, a = 0 (where x = a is location of the delta function)
    dcon = 1.0

    for tp in plot_times:

        t = ntim[tp]
        lab = 't\'={:.6f}'.format(t)

        # Analytic solution
        c1 = 1.0 / np.sqrt(4.0 * np.pi * dcon * t)
        uc = c1 * np.exp(-0.25 * x * x / t)

        un = nval[tp,:]

        if not np.all(np.isfinite(un)):
            raise AssertionError(
                f"{testname} numerical solution has non-finite values at step {tp} (t={t:.6f})."
            )
        if not np.all(np.isfinite(uc)):
            raise AssertionError(
                f"{testname} analytic solution has non-finite values at step {tp} (t={t:.6f})."
            )

        rel_l2_error = np.linalg.norm(un - uc) / np.linalg.norm(uc)
        assert rel_l2_error < rel_l2_tol, (
            f"{testname} relative L2 error {rel_l2_error:.3e} exceeds tolerance {rel_l2_tol:.2f} "
            f"at step {tp} (t={t:.6f})."
        )

        plt.plot(x, uc, "b-", lw=2.0, label=lab+' (ref)')
        plt.plot(x, un, "r--", lw=2.0, label=lab)

    plt.xlim((-5, 5))
    plt.xlabel('$x$ (cm)')
    plt.ylabel('$\phi(x,t\')$')
    plt.legend()
    plt.savefig(testname + ".png", format="png", bbox_inches="tight")

    return True
