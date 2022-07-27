"""Mesh processing."""

import numpy as np

import hvy_global_mesh_data as mesh

## @brief Sets up the mesh
##
## This function sets up the mesh, by determining the _x_-coordinates
## of the cell centres and nodes, from the cell size, number of cells
## and total mesh size.

# ------------------------------------------------------------------------------


def setup():
    """Set up initial mesh."""
    # Create cell data as a 2D array (with first dimension = 1)
    # to facilitate use of matplotlib.pyplot.pcolor
    # mesh.cells = np.zeros((1, mesh.ncells + 1))
    # mesh.cells[0, 0:mesh.ncells + 1] = np.linspace(0., mesh.xsize,
    #    mesh.ncells + 1)

    # mesh.dx = mesh.xsize / float(mesh.ncells)

    print(("num cells/nodes ", mesh.ncells))

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
