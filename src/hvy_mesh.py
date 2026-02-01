"""Mesh processing."""

import sys

import numpy as np

import hvy_global_mesh_data as mesh

## @brief Sets up the mesh
##
## This function sets up the mesh, by determining the _x_-coordinates
## of the cell centres and nodes, from the cell size, number of cells
## and total mesh size.

# ------------------------------------------------------------------------------


def _validate_mesh_parameters():
    """Validate mesh parameters before building coordinate arrays."""
    errors = []

    if mesh.geom is None:
        errors.append("mesh.geom must be set to 0 (planar)")
    elif mesh.geom != 0:
        errors.append(
            "mesh.geom must be 0 (planar). Cylindrical and spherical geometries are not supported yet."
        )

    try:
        dx_value = float(mesh.dx)
    except (TypeError, ValueError):
        errors.append("mesh.dx must be a positive number")
    else:
        if dx_value <= 0.0:
            errors.append("mesh.dx must be greater than zero")
        else:
            mesh.dx = dx_value

    try:
        xsize_value = float(mesh.xsize)
    except (TypeError, ValueError):
        errors.append("mesh.xsize must be a positive number")
    else:
        if xsize_value <= 0.0:
            errors.append("mesh.xsize must be greater than zero")
        else:
            mesh.xsize = xsize_value

    try:
        theta_value = float(mesh.theta)
    except (TypeError, ValueError):
        errors.append("mesh.theta must be a number between 0 and 1")
    else:
        if not 0.0 <= theta_value <= 1.0:
            errors.append("mesh.theta must be between 0 and 1")
        else:
            mesh.theta = theta_value

    try:
        ncells_value = int(mesh.ncells)
    except (TypeError, ValueError):
        errors.append("mesh.ncells must be a positive integer")
    else:
        if ncells_value <= 0:
            errors.append("mesh.ncells must be a positive integer")
        elif ncells_value != mesh.ncells:
            errors.append("mesh.ncells must be an integer value")
        else:
            mesh.ncells = ncells_value

    if not errors and mesh.dx > 0.0:
        expected_cells = mesh.xsize / mesh.dx
        if not np.isclose(expected_cells, mesh.ncells, rtol=1.0e-6, atol=1.0e-12):
            errors.append("mesh.ncells must be consistent with mesh.xsize / mesh.dx")

    if errors:
        print("    Error: invalid mesh parameters")
        for message in errors:
            print(f"        - {message}")
        sys.exit(1)


def setup():
    """Set up initial mesh."""
    _validate_mesh_parameters()
    # Create cell data as a 2D array (with first dimension = 1)
    # to facilitate use of matplotlib.pyplot.pcolor
    # mesh.cells = np.zeros((1, mesh.ncells + 1))
    # mesh.cells[0, 0:mesh.ncells + 1] = np.linspace(0., mesh.xsize,
    #    mesh.ncells + 1)

    # mesh.dx = mesh.xsize / float(mesh.ncells)

    print(f"num cells/nodes {mesh.ncells}")

    mesh.cellpos = np.arange(0.5 * mesh.dx, mesh.xsize, mesh.dx)
    mesh.nodepos = np.linspace(0.0, mesh.xsize, mesh.ncells + 1)
    # for j in range(len(mesh.nodepos)):
    #    print j, mesh.nodepos[j]

    mesh.cellpos[:] = mesh.cellpos[:] + mesh.xmin
    mesh.nodepos[:] = mesh.nodepos[:] + mesh.xmin


## @brief Prints the mesh information
##
## This function prints out the mesh information.

# ------------------------------------------------------------------------------

# def printout():
#    """
#    @brief   This is a brief description.
#
#    @details Here is a longer description.
#             Which can go over several lines.
#    @param   None
#    @return  int Returns a 0 if successful
#
#    This is a header
#    ================
#
#    So is this
#    ----------
#    """
#    print
#    print "Mesh..."
#
#    print "    Number of cells    = ", mesh.ncells, len(mesh.cellpos)
#    print "    Number of nodes    = ", mesh.ncells+1, len(mesh.nodepos)
#    print "    Size of domain     = ", mesh.xsize
#    print "    Spatial resolution = ", mesh.dx
#    print "    Origin of mesh     = ", mesh.xmin
#    #print mesh.cellpos
#    for j in range(mesh.ncells-1):
#        print "    ", j, mesh.nodepos[j], mesh.cellpos[j]
#    print "    ", mesh.ncells, mesh.nodepos[mesh.ncells]
