"""Global data related to mesh."""

# Execution statements - only executed the first time this module is imported

geom = -1
ncells = -1
xsize = -1.0
dx = -1.0
theta = -1.0
xmin = 0.0

# Cell arrays

cellpos = -1.0
# sigma_p = -1.0
# temp = -1.0
# temp0 = -1.0
# beta = -1.0
# nrgdep = -1.0

# Nodal arrays

nodepos = -1.0


# Reset state for re-entrant runs.
def reset():
    """Reset global mesh data to defaults."""
    global geom, ncells, xsize, dx, theta, xmin, cellpos, nodepos
    geom = -1
    ncells = -1
    xsize = -1.0
    dx = -1.0
    theta = -1.0
    xmin = 0.0
    cellpos = -1.0
    nodepos = -1.0
