#!/usr/bin/env python3
"""Main program."""

import argparse
import time as pytime

import harfort
import hvy_bcons
import hvy_mats
import hvy_mesh
import hvy_regs
import hvy_user_input
import hvy_global_bcon_data as bcon
import hvy_global_mat_data as mat
import hvy_global_mesh_data as mesh
import hvy_global_reg_data as reg
import hvy_global_time_data as time

## @brief The main run function
#
# This is the main run function that is called when the code is executed.
# It reads the user input, echoes it to the output, sets up the materials
# and the mesh, and then calls the main Fortran routine that performs the
# numerical calculation; i.e. the `fib` subroutine in harvey.f90.


def parse_args():
    """Process command line options and arguments."""
    parser = argparse.ArgumentParser(description="Python/Fortran 1D diffusion code.")

    parser.add_argument("-i", "--input", default="harvin", help="Name of input file")
    parser.add_argument(
        "-o", "--output", default="harvey.out", help="Name of output file"
    )
    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="Enable debug mode",
    )

    return parser.parse_args()


# ------------------------------------------------------------------------------


def setup(input_file):
    """Set up calculation."""
    print("\nReading user input...")
    hvy_user_input.read(input_file)
    hvy_user_input.initialize_counts()
    hvy_user_input.echo()

    _validate_time_parameters()

    # -------------------------------------------------------------------------

    print("\nSetting up materials...")
    hvy_mats.setup()

    # -------------------------------------------------------------------------

    print("\nSetting up regions...")
    hvy_regs.setup()

    # -------------------------------------------------------------------------

    print("\nSetting up mesh...")
    hvy_mesh.setup()
    # hvy_mesh.printout()

    print("\nProcessing boundary conditions...")
    hvy_bcons.setup()


def _validate_time_parameters():
    """Validate time-stepping parameters before computation."""
    errors = []
    if time.dt <= 0.0:
        errors.append("time.dt must be greater than zero")

    if errors:
        print("    Error: invalid time parameters")
        for message in errors:
            print(f"        - {message}")
        raise SystemExit(1)

    if time.end <= 0.0:
        print("    Warning: time.end is non-positive; no time stepping will occur")


# ------------------------------------------------------------------------------

# Everything starts here...
# (Except in the QA test suite; this calls harvey.run directly)


def main(input_file, output_file, debug_mode):
    """
    @brief   Top-level function for harvey..

    @details Can be called within Python after importing, so has simple/flat signature.

    @param   input_file   Name of input file
    @param   output_file  Name of output file
    @param   debug_mode   Logical flag to turn on verbose logging
    """
    tm0 = pytime.perf_counter()

    ## @todo Add a debug mode.
    if debug_mode:
        print("Debug mode")

    setup(input_file)

    # Run main calculation
    harfort.main(
        mesh.ncells,
        mat.nmats,
        reg.nregs,
        mesh.geom,
        mesh.theta,
        mesh.dx,
        time.dt,
        time.end,
        bcon.inner["itype"],
        bcon.inner["value"],
        bcon.outer["itype"],
        bcon.outer["value"],
        mat.dcoeff,
        reg.bound,
        reg.matnum,
        reg.dcoeff,
        mesh.cellpos,
        mesh.nodepos,
        output_file,
        bcon.icon["itype"],
        bcon.icon["ival"],
    )

    tm1 = pytime.perf_counter()
    print("Time taken for calculation = {:10.2f} s".format(tm1 - tm0))


if __name__ == "__main__":

    # Process command line
    args = parse_args()

    main(args.input, args.output, args.debug)
