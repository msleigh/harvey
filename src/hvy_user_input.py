"""User input functions."""

## @brief Process command-line arguments
##
## Process the command-line arguments

import importlib.util
import re
import sys
from pathlib import Path

import hvy_global_bcon_data as bcon
import hvy_global_mesh_data as mesh
import hvy_global_mat_data as mat
import hvy_global_reg_data as reg
import hvy_global_time_data as time


def _load_user_input(input_file):
    if not isinstance(input_file, str):
        print("    Error: input file name must be a string")
        sys.exit(1)

    input_name = input_file
    if input_name.endswith(".py"):
        input_name = Path(input_name).stem

    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", input_name):
        print(
            "    Error: input file name must be a valid module identifier (letters, "
            "numbers, underscores)"
        )
        sys.exit(1)

    search_paths = [Path.cwd(), Path(__file__).resolve().parent]
    input_path = None
    for candidate in search_paths:
        if (candidate / f"{input_name}.py").is_file():
            input_path = candidate
            break
    if input_path is None:
        print(
            "    Error: input file not found in current directory or source directory"
        )
        sys.exit(1)

    module_path = input_path / f"{input_name}.py"
    spec = importlib.util.spec_from_file_location(input_name, module_path)
    if spec is None or spec.loader is None:
        print("    Error: unable to load input module")
        sys.exit(1)

    module = importlib.util.module_from_spec(spec)
    sys.modules[input_name] = module
    spec.loader.exec_module(module)
    return module


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
    harvin = _load_user_input(input_file)
    print("    Running...")
    if not hasattr(harvin, "define") or not callable(harvin.define):
        print("    Error: input module must define a callable define() function")
        sys.exit(1)
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

    print(("    mat.nmats      ", mat.nmats))
    for matname in mat.materials.keys():
        print(("    mat.name    ", matname))
        print(("    mat.dcoeff  ", mat.materials[matname]["d"]))

    print(("    reg.nregs      ", reg.nregs))
    for regname in reg.regions.keys():
        print(("    reg.name   ", regname))
        print(("    reg.mat    ", reg.regions[regname]["mat"]))
        print(("    reg.xbound ", reg.regions[regname]["xbound"]))


def initialize_counts():
    """Initialize material and region counts after input definition."""
    mat.nmats = len(mat.materials)
    reg.nregs = len(reg.regions)
