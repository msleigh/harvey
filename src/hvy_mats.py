"""Materials processing."""

import numpy as np

import hvy_global_mat_data as mat


def setup():
    """
    Set up materials.

    More detailed information
    """
    if not mat.materials:
        print("    Error: no materials defined in user input")
        raise SystemExit(1)

    expected_nmats = len(mat.materials)
    if mat.nmats != expected_nmats:
        mat.nmats = expected_nmats

    # Assign unique integer index to each material and create numpy array of material
    # properties (so far only diffusion coefficient)
    mat.dcoeff = np.zeros(mat.nmats)
    for imat, matname in enumerate(mat.materials.keys()):
        mat.dcoeff[imat] = mat.materials[matname]["d"]
