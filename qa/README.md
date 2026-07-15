QA test problem summary
=======================

This table is transcribed from the current `qa/hvy_qa_test/test*_in.py` input
files. The `Order` column follows `qa/test_problems.csv`.

| Test | Scheme | Comparison | Left boundary | Right boundary | Initial condition | Domain | Order | Source |
| ---- | ------ | ---------- | ------------- | -------------- | ----------------- | ------ | ----- | ------ |
| test1 | Explicit | Analytic | dirichlet 0.0 | dirichlet 0.0 | sin(pi*x/L) | Finite | 1 | |
| test2 | Laasonen | Analytic | dirichlet 0.0 | dirichlet 0.0 | sin(pi*x/L) | Finite | 2 | |
| test3 | Crank-Nicolson | Analytic | dirichlet 0.0 | dirichlet 0.0 | constant 1.0 | Finite | 5 | |
| test4 | Explicit | Analytic | dirichlet 0.0 | dirichlet 0.0 | chevron | Finite | 7 | |
| test5 | Explicit | Alt. implementation | dirichlet 100.0 | neumann 0.0 | zero | Finite | 15 | [1] |
| test6 | Crank-Nicolson | Analytic | dirichlet 100.0 | dirichlet 0.0 (infinity) | zero | Semi-infinite | 17 | |
| test7 | Explicit | Analytic | dirichlet 0.0 (infinity) | dirichlet 0.0 (infinity) | gaussian | Infinite | 19 | RHB p. 579 |
| test8 | Explicit | Analytic | dirichlet 1.0 | dirichlet 0.0 | zero | Finite | 9 | |
| test9 | Crank-Nicolson | Analytic | dirichlet 1.0 | dirichlet 0.0 | zero | Finite | 8 | |
| test10 | Explicit | Analytic | dirichlet 100.0 | dirichlet 0.0 (infinity) | zero | Semi-infinite | 18 | RHB p. 577 |
| test11 | Crank-Nicolson | Analytic | dirichlet 0.0 | dirichlet 1.0 | zero | Finite | 10 | |
| test12 | Explicit | Analytic | dirichlet 0.0 | dirichlet 1.0 | zero | Finite | 11 | |
| test13 | Explicit | Analytic | dirichlet 0.0 | neumann 1.0 | zero | Finite | 12 | RHB p. 550 |
| test14 | Crank-Nicolson | Analytic | dirichlet 0.0 | neumann 1.0 | zero | Finite | 13 | RHB p. 550 |
| test15 | Crank-Nicolson | Analytic | dirichlet 0.0 | neumann 0.0 | sin(pi*x/2L) | Finite | 3 | |
| test16 | Explicit | Alt. implementation | neumann 0.0 | dirichlet 100.0 | zero | Finite | 16 | [1] |
| test17 | Crank-Nicolson | Analytic | neumann 0.0 | dirichlet 0.0 | cos(pi*x/2L) | Finite | 4 | |
| test18 | Crank-Nicolson | Analytic | dirichlet 0.0 | dirichlet 0.0 | chevron | Finite | 6 | |

RHB = Riley, Hobson, and Bence, *Mathematical Methods for Physics and
Engineering*.

[1]: http://excelcalculations.blogspot.co.uk/2011/04/solving-1d-heat-equation-using-finite.html
    (reference data in `qa/hvy_qa_test/1DHeatEquation/solution.txt`)
