"""Physical constants."""

# import numpy as np
#
## Physical constants
## ------------------
#
#
## Speed of light
#
# C = 3.e+10                     ## cm.s^-1
#
## Planck constant
#
# H = 4.1356675e-18               # KeV.s
#
#
## Derived constants
## -----------------
#
# INV_C = 1. / c
#
# INV_H = 1. / h
#
# INV_H3 = 1. / h**3
#
# H3_C3 = h**3 * c**3              # keV^3.cm^3
#
# X15_PI4 = 15. / np.pi**4
#
## Stefan-Boltzmann constant
## (with the k^4 missing since this is folded into the temp variable)
#
# SB = 2. * pi**5 / (15. * h**3*c**2)   # keV^-3.cm^-2.s^-1 (flux-like)
#
## Radiation constant
#
# A = 4. * sb / c                     # keV^-3.cm^-3      (density-like)
#
# D04_A_C = a * c / 4. # ac/4 - used to calculate energy radiated from surface
