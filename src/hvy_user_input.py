"""User input functions."""

## @brief Process command-line arguments
##
## Process the command-line arguments

import sys

import hvy_global_bcon_data as bcon
import hvy_global_mesh_data as mesh
import hvy_global_mat_data as mat
import hvy_global_reg_data as reg
import hvy_global_time_data as time


def read(input_file):
    """
    @brief   Reads input deck (by importing).

    @details Reads input deck with user-specified problem-specific
             information.
    @param   None
    @return  None
    """
    # There is no default input file name (initialised to None in import)
    print()
    print("Processing user input file...")
    if input_file is None:
        print("    Error: no input file specified")
        sys.exit()

    bcon.reset()
    mesh.reset()
    mat.reset()
    reg.reset()
    time.reset()

    print(("    Specified input file name = ", input_file))
    print("    Importing...")
    harvin = __import__(input_file)
    print("    Running...")
    harvin.define()


def echo():
    """Echo user input back out."""
    print()
    print("Echoing user input...")

    print(("    mesh.geom      ", mesh.geom))
    print(("    mesh.theta     ", mesh.theta))
    print(("    mesh.ncells    ", mesh.ncells))
    print(("    mesh.xmin      ", mesh.xmin))
    print(("    mesh.xsize     ", mesh.xsize))
    print(("    mesh.dx        ", mesh.dx))

    print(("    time.dt        ", time.dt))
    print(("    time.end       ", time.end))

    mat.nmats = len(mat.materials)
    print(("    mat.nmats      ", mat.nmats))
    for matname in mat.materials.keys():
        print(("    mat.name    ", matname))
        print(("    mat.dcoeff  ", mat.materials[matname]["d"]))

    reg.nregs = len(reg.regions)
    print(("    reg.nregs      ", reg.nregs))
    for regname in reg.regions.keys():
        print(("    reg.name   ", regname))
        print(("    reg.mat    ", reg.regions[regname]["mat"]))
        print(("    reg.xbound ", reg.regions[regname]["xbound"]))
