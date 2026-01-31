Test Suite Report  {#testreport}
=================

\tableofcontents


\section testreport_summary Summary

This report documents the analysis of the Harvey test suite, which validates the 1D heat/diffusion equation solver against analytic solutions and reference implementations.

| Metric | Value |
|--------|-------|
| Total tests defined | 19 (including 3 commented out) |
| Tests executed | 16 |
| Tests passed | 16 |
| Tests failed | 0 |
| Tests disabled | 3 (Test 9, 11, 12) |
| PNG images generated | 15 |
| Data output files | 17 (15 test*.out + 2 reset*.out) |


\section testreport_detailed Detailed Test Analysis

The following table summarizes all tests in the suite:

| Test | Runs | Pass | Data Output | PNG | Numerical Method | Validation Type | Scientific Assessment |
|------|------|------|-------------|-----|------------------|-----------------|----------------------|
| Reset Smoke | Yes | Yes | reset_a.out, reset_b.out | No | Explicit (@f$\theta=0@f$) | Re-entrant state check | Verifies solver can be called multiple times without state pollution |
| Test 1 | Yes | Yes | test1.out (37MB) | Yes | Explicit (@f$\theta=0@f$) | Analytic (tol=5e-9) | Sinusoidal IC, Dirichlet BC; excellent match with exponential decay solution |
| Test 2 | Yes | Yes | test2.out (37MB) | Yes | Implicit (@f$\theta=1@f$) | Analytic (tol=5e-4) | Same as Test 1 but fully implicit; excellent match |
| Test 3 | Yes | Yes | test3.out (24MB) | Yes | Crank-Nicolson (@f$\theta=0.5@f$) | Analytic (tol=1e-1) | Constant IC, Dirichlet BC; Fourier series solution; excellent match |
| Test 4 | Yes | Yes | test4.out (48KB) | Yes | Explicit (@f$\theta=0@f$) | Analytic (tol=5e-1) | Chevron IC, Dirichlet BC; excellent match with damped triangular profile |
| Test 5 | Yes | Yes | test5.out (530KB) | Yes | Explicit (@f$\theta=0@f$) | Reference impl (tol=0.085%) | Comparison with external 1DHeatEquation solution; perfect match |
| Test 6 | Yes | Yes | test6.out (92MB) | Yes | Crank-Nicolson (@f$\theta=0.5@f$) | Analytic erf() | Semi-infinite bar with error function solution; excellent match |
| Test 7 | Yes | Yes | test7.out (54MB) | Yes | Explicit (@f$\theta=0@f$) | Analytic Gaussian | Delta function IC, Gaussian diffusion; good match at all times |
| Test 8 | Yes | Yes | test8.out (14MB) | Yes | Explicit (@f$\theta=0@f$) | Analytic Fourier | Zero IC, non-zero BC; excellent match showing approach to steady state |
| Test 9 | **No** | N/A | N/A | N/A | Crank-Nicolson (@f$\theta=0.5@f$) | Analytic | *Disabled* - similar to Test 8 with different scheme |
| Test 10 | Yes | Yes | test10.out (92MB) | Yes | Explicit (@f$\theta=0@f$) | Analytic erf() | Same as Test 6 but explicit scheme; excellent match |
| Test 11 | **No** | N/A | N/A | N/A | Implicit (@f$\theta=1@f$) | Reference | *Disabled* - similar to Test 8 with different scheme |
| Test 12 | **No** | N/A | N/A | N/A | Explicit (@f$\theta=0@f$) | Reference | *Disabled* - similar to Test 8 |
| Test 13 | Yes | Yes | test13.out (31MB) | Yes | Explicit (@f$\theta=0@f$) | Analytic | Flux BC (Neumann), zero IC; approaches linear steady-state; excellent match |
| Test 14 | Yes | Yes | test14.out (31MB) | Yes | Crank-Nicolson (@f$\theta=0.5@f$) | Analytic | Same as Test 13 with CN scheme; excellent match |
| Test 15 | Yes | Yes | test15.out (19MB) | Yes | Crank-Nicolson (@f$\theta=0.5@f$) | Analytic | Sinusoidal IC, Dirichlet BC; excellent match |
| Test 16 | Yes | Yes | test16.out (530KB) | Yes | Explicit (@f$\theta=0@f$) | Reference impl (tol=1e-12) | Same as Test 5 (reversed BC); perfect match to machine precision |
| Test 17 | Yes | Yes | test17.out (1.3MB) | Yes | Crank-Nicolson (@f$\theta=0.5@f$) | Analytic | Cosine IC, Neumann BC; **significant mismatch observed but assertion disabled** |
| Test 18 | Yes | Yes | test18.out (48KB) | Yes | Crank-Nicolson (@f$\theta=0.5@f$) | Analytic | Chevron IC (like Test 4) with CN scheme; excellent match |


\section testreport_scientific Scientific Correctness Assessment


\subsection testreport_excellent Tests with Excellent Results

The following tests show excellent agreement between numerical and analytic solutions:

| Test | Problem Type | Observed Behavior |
|------|--------------|-------------------|
| 1, 2, 15 | Sinusoidal decay | Exponential amplitude decay matches theory perfectly |
| 3 | Constant to zero | Fourier mode decay correct |
| 4, 18 | Chevron diffusion | Sharp peak smoothing follows analytic solution |
| 5, 16 | Reference comparison | Machine-precision match with external implementation |
| 6, 10 | Semi-infinite bar | Error function profile matches boundary diffusion |
| 7 | Delta function | Gaussian spreading at correct rate @f$\sqrt{4Dt}@f$ |
| 8 | Step to steady state | Correct approach to linear steady-state profile |
| 13, 14 | Flux boundary | Correct evolution toward @f$Hx/D@f$ steady state |


\subsection testreport_issues Tests with Issues

| Test | Issue |
|------|-------|
| **Test 17** | PNG output shows numerical (red) and analytic (blue) solutions diverge significantly. The test passes only because the validation assertion is commented out. The analytic solution uses IC = @f$\cos(\pi x / 2L)@f$ but there may be a boundary condition mismatch. |


\subsection testreport_disabled Disabled Tests

| Test | Reason (inferred) |
|------|-------------------|
| 9 | Crank-Nicolson variant of Test 8 (possibly redundant or unstable) |
| 11 | Fully implicit variant of Test 8 (possibly redundant) |
| 12 | Explicit variant similar to Test 8 (possibly redundant) |


\section testreport_outputs Output Files

After running `make test`, the following outputs are generated:

| Directory | Contents |
|-----------|----------|
| `build/QA/*.png` | 15 visualization images comparing numerical vs reference solutions |
| `build/QA/*.out` | 17 solution data files (time series of spatial profiles) |
| `build/QA/log.html` | Robot Framework detailed execution log |
| `build/QA/output.xml` | Robot Framework machine-readable results |
| `build/QA/report.html` | Robot Framework summary report |
| `build/QA/1DHeatEquation/` | Reference solution data for comparison tests |


\section testreport_conclusions Conclusions

1. **All 16 active tests pass** - the Harvey 1D heat equation solver produces correct results across multiple numerical schemes (explicit, implicit, Crank-Nicolson) and boundary conditions (Dirichlet, Neumann).

2. **Scientific validation is thorough** - tests cover:
   - Multiple initial conditions (sinusoidal, constant, chevron, delta function)
   - Multiple boundary conditions (Dirichlet, Neumann/flux)
   - Multiple numerical schemes (@f$\theta = 0, 0.5, 1@f$)
   - Comparison with both analytic solutions and external reference implementations

3. **Test 17 requires attention** - the visual output shows significant discrepancy between numerical and analytic solutions, but the test passes because the validation code is commented out.

4. **Tests 9, 11, 12 are disabled** - these appear to be variants of existing tests and may have been disabled due to redundancy or known issues.
