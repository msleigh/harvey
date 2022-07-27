-------|---------------|----------------||-------------|-------------||---------|------------||----------|--------
TEST   | COMPARISON    | DIFFERENCING   ||       LEFT BOUNDARY       ||    RIGHT BOUNDARY    || INITIAL  | SOURCE
       |               |                ||   u(0,t)    | du/dx(0,t)  || u(L,t)  | du/dx(L,t) ||  u(x,0)  |
-------|---------------|----------------||-------------|-------------||---------|------------||----------|--------
                                        ||             |             ||
EXPLICIT DIR/DIR                        ||             |             ||
                                        ||             |             ||
test3  | Analytic sol. | Explicit       || 0 (Inf)     |      -      || 0 (Inf) |     -      || Gaussian | RHB p.579
test5  | Analytic sol. | Explicit       || 0           |      -      || 0       |     -      || Sinusoid |
test6  | Analytic sol. | Explicit       || 0           |      -      || 0       |     -      || Chevron  |
test7  | Analytic sol. | Explicit       || 0           |      -      || 0       |     -      || Constant |
test2  | Analytic sol. | Explicit       || 100         |      -      || 0 (Inf) |     -      || 0        | RHB p.577
test8  | Analytic sol. | Explicit       || 1           |      -      || 0       |     -      || 0        |
test12 | Analytic sol. | Explicit       || 0           |      -      || 1       |     -      || 0        |
                                        ||             |             ||
IMPLICIT DIR/DIR                        ||             |             ||
                                        ||             |             ||
test10 | Analytic sol. | Implicit (1.0) || 0           |      -      || 0       |     -      || Sinusoid |
test4  | Analytic sol. | Implicit (0.5) || 100         |      -      || 0 (Inf) |     -      || 0        |
test9  | Analytic sol. | Implicit (0.5) || 1           |      -      || 0       |     -      || 0        |
test11 | Analytic sol. | Implicit (0.5) || 0           |      -      || 1       |     -      || 0        |

EXPLICIT DIR/NEU

test1  | Alt. scheme   | Explicit       || 100         |      -      ||    -    | 0          || 0        | http://excelcalculations.blogspot.co.uk/2011/04/solving-1d-heat-equation-using-finite.html
test13 | Analytic sol. | Explicit       || 0           |      -      ||    -    | 1          || 0        | RHB p.550

IMPLICIT DIR/NEU

test14 | Analytic sol. | Implicit (0.5) || 0           |      -      ||    -    | 1          || 0        | RHB p.550
test15 | Analytic sol. | Implicit (0.5) || 0           |      -      ||    -    | 0          || Sinusoid |

EXPLICIT NEU/DIR

test16 | Alt. scheme   | Explicit       ||      -      | 0           || 100     |     -      || 0        | http://excelcalculations.blogspot.co.uk/2011/04/solving-1d-heat-equation-using-finite.html
NEEDS SETTING UP:                                        1

IMPLICIT NEU/DIR

test17 | Analytic sol. | Implicit (0.5) ||      -      | 0           || 0       |     -      || Sinusoid |
NEEDS SETTING UP:                                        1


RHB = Riley, Hobson and Bence
