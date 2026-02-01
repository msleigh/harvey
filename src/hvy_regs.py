"""Region processing."""

import sys

import numpy as np

import hvy_global_mat_data as mat
import hvy_global_mesh_data as mesh
import hvy_global_reg_data as reg


def setup():
    """Set up regions."""
    # Create numpy arrays for the region properties (material number, outer
    # boundary)
    reg.nregs = len(reg.regions)
    reg.bound = np.zeros(reg.nregs)
    reg.matnum = np.zeros(reg.nregs, dtype=np.uint64)
    reg.dcoeff = np.zeros(reg.nregs)
    for ireg, regname in enumerate(reg.regions.keys()):
        # If no outer boundary is specified then use a large value relative to
        # the mesh size.
        if reg.regions[regname]["xbound"] is None:
            reg.bound[ireg] = 10.0 * mesh.xsize
        else:
            reg.bound[ireg] = reg.regions[regname]["xbound"]
        mat_name = reg.regions[regname]["mat"]
        if mat_name not in mat.materials:
            print(f"    Error: material '{mat_name}' is not defined")
            sys.exit(1)
        reg.matnum[ireg] = mat.materials[mat_name]["id"]
        reg.dcoeff[ireg] = mat.materials[mat_name]["d"]

    for ireg, regname in enumerate(reg.regions.keys()):
        print(f"    Region name      = {regname} |")
        print(f"    Material number  = {reg.matnum[ireg]} |")
        print(f"    Material name    = {reg.regions[regname]['mat']} |")
        print(
            f"    Diffusion coeff. = {mat.materials[reg.regions[regname]['mat']]['d']} |"
        )
