"""Region processing."""

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
        # If no outer boundary is specified then make it some large number (why
        # not just = xsize?)
        if reg.regions[regname]["xbound"] is None:
            reg.bound[ireg] = 10.0 * mesh.xsize
        else:
            reg.bound[ireg] = reg.regions[regname]["xbound"]
        reg.matnum[ireg] = mat.materials[reg.regions[regname]["mat"]]["id"]
        reg.dcoeff[ireg] = mat.materials[reg.regions[regname]["mat"]]["d"]

    for ireg, regname in enumerate(reg.regions.keys()):
        print(("    Region name      = ", regname, "|"))
        print(("    Material number  = ", reg.matnum[ireg], "|"))
        print(("    Material name    = ", reg.regions[regname]["mat"], "|"))
        print(("    Diffusion coeff. = ", mat.materials[reg.regions[regname]["mat"]]["d"], "|"))
