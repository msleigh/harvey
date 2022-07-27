"""Materials processing."""

import numpy as np

import hvy_global_mat_data as mat


def setup():
    """
    Set up materials.

    More detailed information
    """
    # Assign unique integer index to each material and create numpy array of material
    # properties (so far only diffusion coefficient)
    mat.dcoeff = np.zeros(mat.nmats)
    for imat, matname in enumerate(mat.materials.keys()):
        mat.dcoeff[imat] = mat.materials[matname]["d"]
