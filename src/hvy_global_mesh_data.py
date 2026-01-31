"""Global data related to mesh."""

# Execution statements - only executed the first time this module is imported

geom = None
ncells = None
xsize = None
dx = None
theta = None
xmin = 0.0

# Cell arrays

cellpos = None
# sigma_p = -1.0
# temp = -1.0
# temp0 = -1.0
# beta = -1.0
# nrgdep = -1.0

# Nodal arrays

nodepos = None


# Reset state for re-entrant runs.
def reset():
    """Reset global mesh data to defaults."""
    global geom, ncells, xsize, dx, theta, xmin, cellpos, nodepos
    geom = None
    ncells = None
    xsize = None
    dx = None
    theta = None
    xmin = 0.0
    cellpos = None
    nodepos = None
