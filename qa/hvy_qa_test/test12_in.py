import numpy as np

import hvy_global_bcon_data as bcon
import hvy_global_mesh_data as mesh
import hvy_global_mat_data as mat
import hvy_global_reg_data as reg
import hvy_global_time_data as time


def define():
    # Specify the geometry (1D)
    # -------------------------

    # 0 = planar
    # 1 = cylindrical
    # 2 = spherical

    mesh.geom = 0

    # Specify the forward/backward Euler mixing coefficient
    # -----------------------------------------------------

    # 0.0 <= theta <= 1.0

    # Scheme stable for:
    # 0.0 <= theta <  0.5, if dt <= dx^2/(2*sigma)*(1 - 2*theta)
    # 0.5 <= theta <= 1.0, always

    # Special cases:
    # 0.0 = fully explicit
    # 0.5 = Crank and Nicolson (1947), implicit
    # 1.0 = Laasonen (1949), fully implicit

    mesh.theta = 0.0

    # Specify the size of the problem in cm
    # -------------------------------------

    mesh.xsize = np.pi

    # Specify the size of the mesh cells in cm
    # ----------------------------------------

    mesh.dx = 0.025 * np.pi

    mesh.ncells = int(mesh.xsize / mesh.dx)

    assert mesh.ncells == 40

    # Specify the time-step in ??
    # ---------------------------

    dcon = 1.0

    time.dt = 0.5 * (mesh.dx * mesh.dx) / (11.0 * dcon)
    time.end = 640.0 * mesh.dx * mesh.dx / dcon

    # Specify the boundary conditions
    # -------------------------------

    # Use "left" or "inner" to identify the boundary condition at j = 0
    # Use "right" or "outer" to identify the boundary condition at j = J

    # Specify dirichlet or neumann to indicate the boundary condition is a
    # value of the unknown, u, or of the derivative of the unknown, du/dx,
    # at the boundary (respectively)

    # Then give the numerical value

    bcon.inner = {"type": "dirichlet", "value": 0.0}
    bcon.outer = {"type": "dirichlet", "value": 1.0}
    bcon.icon = {"type": "constant", "value": 0.0}

    # Specify the materials
    # ---------------------

    # Material 1

    mat.material("Stuff", dcon)

    # Specify the regions
    # -------------------

    reg.region("Inner bit", "Stuff", mesh.xsize)
