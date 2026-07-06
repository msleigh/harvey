QA test problem summary
=======================

This table is transcribed from the current `qa/hvy_qa_test/test*_in.py` input
files. The `Order` column follows `qa/test_problems.csv`.

| Test | Scheme | Left boundary | Right boundary | Initial condition | Order |
| ---- | ------ | ------------- | -------------- | ----------------- | ----- |
| test1 | Explicit | dirichlet 0.0 | dirichlet 0.0 | sin pi / mesh.xsize | 1 |
| test2 | Laasonen | dirichlet 0.0 | dirichlet 0.0 | sin pi / mesh.xsize | 2 |
| test3 | Crank-Nicolson | dirichlet 0.0 | dirichlet 0.0 | constant 1.0 | 5 |
| test4 | Explicit | dirichlet 0.0 | dirichlet 0.0 | chevron C | 7 |
| test5 | Explicit | dirichlet 100.0 | neumann 0.0 | zero | 15 |
| test6 | Crank-Nicolson | dirichlet 100.0 | dirichlet 0.0 | zero | 17 |
| test7 | Explicit | dirichlet 0.0 | dirichlet 0.0 | gaussian | 19 |
| test8 | Explicit | dirichlet 1.0 | dirichlet 0.0 | zero | 9 |
| test9 | Crank-Nicolson | dirichlet 1.0 | dirichlet 0.0 | zero | 8 |
| test10 | Explicit | dirichlet 100.0 | dirichlet 0.0 | zero | 18 |
| test11 | Crank-Nicolson | dirichlet 0.0 | dirichlet 1.0 | zero | 10 |
| test12 | Explicit | dirichlet 0.0 | dirichlet 1.0 | zero | 11 |
| test13 | Explicit | dirichlet 0.0 | neumann 1.0 | zero | 12 |
| test14 | Crank-Nicolson | dirichlet 0.0 | neumann 1.0 | zero | 13 |
| test15 | Crank-Nicolson | dirichlet 0.0 | neumann 0.0 | sin pi / (2.0 * mesh.xsize) | 3 |
| test16 | Explicit | neumann 0.0 | dirichlet 100.0 | zero | 16 |
| test17 | Crank-Nicolson | neumann 0.0 | dirichlet 0.0 | cos pi / (2.0 * mesh.xsize) | 4 |
| test18 | Crank-Nicolson | dirichlet 0.0 | dirichlet 0.0 | chevron C | 6 |

RHB = Riley, Hobson and Bence
