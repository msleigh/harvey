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

    mesh.theta = 0.5

    # Specify the size of the problem in cm
    # -------------------------------------

    mesh.xmin = 0.0
    mesh.xsize = 0.5

    # Specify the size of the mesh cells in cm
    # ----------------------------------------

    mesh.dx = 0.01

    mesh.ncells = int(mesh.xsize / mesh.dx)

    # Specify the time-step in ??
    # ---------------------------

    dcon = 1.0

    time.dt = (mesh.dx * mesh.dx) / (6.0 * dcon)
    time.end = 1000 * time.dt

    # Specify the boundary conditions
    # -------------------------------

    # Use "left" or "inner" to identify the boundary condition at j = 0
    # Use "right" or "outer" to identify the boundary condition at j = J

    # Specify dirichlet or neumann to indicate the boundary condition is a
    # value of the unknown, u, or of the derivative of the unknown, du/dx,
    # at the boundary (respectively)

    # Then give the numerical value

    bcon.inner = {"type": "neumann", "value": 0.0}
    bcon.outer = {"type": "dirichlet", "value": 0.0}
    bcon.icon = {"type": "sin", "value": np.pi / (2.0 * mesh.xsize)}

    # Specify the materials
    # ---------------------

    # Material 1

    mat.material("Stuff", 1.0)

    # Specify the regions
    # -------------------

    reg.region("Inner bit", "Stuff", mesh.xsize)
